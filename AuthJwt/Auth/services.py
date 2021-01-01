import grpc
from django_grpc_framework.services import Service

from Auth.serializers import AccessProtoSerializer

from Auth.authentication import SafeJWTAuthentication
from Auth.models import User, AccessControl


class AuthService(Service):
    def get_payload(self, token):
        try:
            return SafeJWTAuthentication.extract_auth(token)
        except:
            self.context.abort(grpc.StatusCode.NOT_FOUND, 'token:%s not found!' % token)

    def Retrieve(self, request, context):
        payload = self.get_payload(request.token)
        user = User.objects.filter(id=payload['user_id']).first()
        role = user.role
        try:
            access_control = AccessControl.objects.filter(role=role, targetEndpoint=request.targetEndpoint,
                                                          microServiceName=request.microServiceName).first()
            access = access_control.access
            access = str(access)
            return AccessProtoSerializer(retrieve=bool(access[4]), list=bool(access[3]), create=bool(access[2]),
                                         update=bool(access[1]), delete=bool(access[0]),
                                         user_id=user.pk).message
        except:  ## access not found or have error
            return AccessProtoSerializer(retrieve=False, list=False, create=False, update=False, delete=False,
                                         user_id=user.pk).message
