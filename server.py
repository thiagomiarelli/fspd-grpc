import grpc
from concurrent import futures
import time
import sys
import database_pb2_grpc as pb2_grpc
import database_pb2 as pb2


class DatabaseService(pb2_grpc.DatabaseServicer):

    def __init__(self, *args, **kwargs):
        self.data = {}
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_DatabaseServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:{}'.format(args[0]))
        print("Server started on port {}".format(args[0]))


    def Insert(self, request, context):
        """
        Insert data into database
        """
        exists = 0
        if request.id in self.data:
            exists = 1

        self.data[request.id] = (request.description, request.value)
        return pb2.InsertReturn(existed=exists)

    def Get(self, request, context):
        """
        Get data from database
        """
        if request.id in self.data:
            return pb2.GetReturn(description=self.data[request.id][0], value=self.data[request.id][1])
        else:
            return pb2.GetReturn(description=None, value=0.0)

    def StopServer(self, request, context):
        """
        Stop server
        """
        numberOfEntries = len(self.data)
        self.stopConnection()
        return pb2.StopServerReturn(numOfKeys=numberOfEntries)

    def stopConnection(self):
        """
        Stops connection after a period of time to let the server answer the client before it closes
        """
        self.server.stop(5)

    def Register(self, request, context):
        """
        Register server
        """
        return pb2.RegisterReturns(numOfIds=4)

    def serve(self):
        self.server.start()
        self.server.wait_for_termination()

    def connectAsClient(self, address):
        """
        Connects to another server as a client
        """
        channel = grpc.insecure_channel(address)
        stub = pb2_grpc.DatabaseStub(channel)
        return stub

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: python3 server.py <port>")
        exit(1)
    port = sys.argv[1]
    server = DatabaseService(port)
    server.serve()