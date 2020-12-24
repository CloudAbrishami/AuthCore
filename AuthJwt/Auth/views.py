from django.contrib.auth import get_user_model, authenticate
from rest_framework import permissions
from rest_framework import views
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

from Auth.authentication import OwnProfilePermission
from Auth.serializers import UserLoginSerializer, UserSerializer
from Auth.utils import generate_access_token


class LoginApi(views.APIView):
    permission_classes = (permissions.AllowAny,)
    http_method_names = ["POST"]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, HTTP_400_BAD_REQUEST)

        user = authenticate(username=serializer.validated_data["username"],
                            password=serializer.validated_data["password"])
        if not user:
            return Response({'error': 'Invalid Credentials'},
                            status=HTTP_404_NOT_FOUND)
        else:
            # user password correct create token

            # template for future update
            access_dic = {
                "user_id": user.id
            }
            access_token = generate_access_token(access_dic)
            return Response({
                'access_token': access_token,
            })


class RegisterApi(CreateAPIView, UpdateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            permission_classes = (permissions.AllowAny,)
        else:
            permission_classes = (OwnProfilePermission,)
        return [permission() for permission in permission_classes]


class ProfileApi(RetrieveAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = OwnProfilePermission
