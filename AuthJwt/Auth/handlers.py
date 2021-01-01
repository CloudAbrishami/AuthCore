from Auth.services import AuthService
from microservices_Auth_pb2_grpc import add_AccessControlServicer_to_server


def grpc_handlers(server):
    add_AccessControlServicer_to_server(AuthService.as_servicer(), server)