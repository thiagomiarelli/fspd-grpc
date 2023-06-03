import grpc
import sys
from concurrent import futures
import integration_pb2_grpc as pb2_grpc
import integration_pb2 as pb2
from client import DatabaseClient

class IntegrationService(pb2_grpc.IntegrationServicer):

    def __init__(self, *args, **kwargs):
        self.data = {
            1: ("localhost", 4000),
        }
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_IntegrationServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:{}'.format(args[0]))
        print("Server started on port {}".format(args[0]))

    def serve(self):
        self.server.start()
        self.server.wait_for_termination()

    def GetIntegration(self, request, context):
        """
        GetIntegration data from database
        """
        if request.id in self.data:
            databaseServer = DatabaseClient(f'{self.data[request.id][0]}:{self.data[request.id][1]}')
            result = databaseServer.get(request.id)
            databaseServer.channel.close()

            return pb2.GetIntegrationReturn(description=result[0], value=result[1])
        else:
            return pb2.GetIntegrationReturn(description="NA", port=value)

    def RegisterIntegration(self, request, context):
        """
        Register server
        """
        address = request.address
        port = request.port
        ids = request.ids

        for id in ids:
            self.data[id] = (address, port)
        
        return pb2.RegisterIntegrationReturn(numOfIds=len(ids))

    def StopIntegrationServer(self, request, context):
        """
        Stop server
        """
        numberOfEntries = len(self.data)
        self.stopConnection()
        return pb2.StopIntegrationServerReturn(numOfIds=numberOfEntries)

    def stopConnection(self):
        """
        Stops connection after a period of time to let the server answer the client before it closes
        """
        self.server.stop(5)

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: python3 integrationServer.py <port>")
        exit(1)
    port = sys.argv[1]
    server = IntegrationService(port)
    server.serve()