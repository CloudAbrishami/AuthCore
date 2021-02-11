import grpc
import microservices_Auth_pb2
import microservices_Auth_pb2_grpc
invalid_token = "sample"
with grpc.insecure_channel('localhost:50051') as channel:
    stub = microservices_Auth_pb2_grpc.AccessControlStub(channel)
    ans = stub.Retrieve(microservices_Auth_pb2.AccessRequest(token=invalid_token, targetEndpoint="/list",
                                                             microServiceName="test"))
    print(ans)