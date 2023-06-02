import grpc
import sys
from concurrent import futures
import integration_pb2_grpc as pb2_grpc
import integration_pb2 as pb2

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

    def Get(self, request, context):
        """
        Get data from database
        """
        if request.id in self.data:
            return pb2.GetReturn(address=self.data[request.id][0], port=self.data[request.id][1])
        else:
            return pb2.GetReturn(address=None, port=0)

if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: python3 integrationServer.py <port>")
        exit(1)
    port = sys.argv[1]
    server = IntegrationService(port)
    server.serve()