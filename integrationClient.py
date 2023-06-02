import grpc
import sys
import integration_pb2_grpc as pb2_grpc
import integration_pb2 as pb2

class IntegrationClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self, address):

        # instantiate a channel
        self.channel = grpc.insecure_channel(address)

        # bind the client and the server
        self.stub = pb2_grpc.IntegrationStub(self.channel)

    def get(self, id):
        """
        Client function to call the rpc for Get
        """
        message = pb2.GetParams(id=id)
        result = self.stub.Get(message)
        return (result.address, result.port)

    def registerIntegration(self, address, port, ids):
        """
        Client function to call the rpc for Register
        """
        message = pb2.RegisterIntegrationParams(address=address, port=port, ids=ids)
        result = self.stub.RegisterIntegration(message)
        return result


if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: python3 client.py <address:port>")
        exit(1)
    address = sys.argv[1]
    client = IntegrationClient(address)
    client.get(1)
    print(client.get(1))
    client.registerIntegration("localhost", 5000, [2,3,4])
    print(client.get(2))