import grpc
import database_pb2_grpc as pb2_grpc
import database_pb2 as pb2


class DatabaseClient(object):
    """
    Client for gRPC functionality
    """

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        # instantiate a channel
        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        # bind the client and the server
        self.stub = pb2_grpc.DatabaseStub(self.channel)

    def get(self, id):
        """
        Client function to call the rpc for Get
        """
        message = pb2.GetParams(id=id)
        result = self.stub.Get(message)
        return (result.description, result.value)


    def insert(self, id, description, value):
        """
        Client function to call the rpc for Insert
        """
        message = pb2.InsertParams(id=id, description=description, value=value)
        result = self.stub.Insert(message)
        return result.existed


if __name__ == '__main__':
    client = DatabaseClient()
    result = client.insert(2, 'test', 1.0)
    ask = client.get(1)
    print(f'Result: {result}')
    print(f'Get: {ask}')