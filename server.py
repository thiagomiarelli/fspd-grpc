import grpc
from concurrent import futures
import time
import database_pb2_grpc as pb2_grpc
import database_pb2 as pb2


class DatabaseService(pb2_grpc.DatabaseServicer):

    def __init__(self, *args, **kwargs):
        self.data = {}
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pb2_grpc.add_DatabaseServicer_to_server(self, self.server)
        self.server.add_insecure_port('[::]:50051')


    def Insert(self, request, context):
        """
        Insert data into database
        """
        print(f'Inserting {request.id} into database')
        exists = 0
        print("chegou aqui1 ")
        if request.id in self.data:
            exists = 1

        self.data[request.id] = (request.description, request.value)
        print(f"data {self.data}")
        print(f"exists {exists}")
        return pb2.InsertReturn(existed=exists)

    def Get(self, request, context):
        """
        Get data from database
        """
        print(f'Getting {request.id} from database')
        if request.id in self.data:
            return pb2.GetReturn(description=self.data[request.id][0], value=self.data[request.id][1])
        else:
            return pb2.GetReturn(description=None, value=0.0)

    def StopServer(self, request, context):
        """
        Stop server
        """
        numberOfEntries = len(self.data)
        print(f'Stopping server with {numberOfEntries} entries in database')
        return pb2.StopServerReturn(numOfKeys=numberOfEntries)

    def serve(self):
        self.server.start()
        self.server.wait_for_termination()


if __name__ == '__main__':
    server = DatabaseService()
    server.serve()