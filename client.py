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
        return result

    def stopServer(self):
        """
        Client function to call the rpc for StopServer
        """
        message = pb2.StopServerParams()
        result = self.stub.StopServer(message)
        return result


def handleUserInput():
    inputString = input("Enter your command: ")
    inputList = inputString.split(",")
    
    if(len(inputList) < 1):
        return -1
    
    command = inputList[0]
    if(command == "I"):
        if(len(inputList) != 4):
            return -1
        id = int(inputList[1])
        description = inputList[2]
        value = float(inputList[3])
        return (command, id, description, value)
    elif(command == "C"):
        if(len(inputList) != 2):
            return (-1)
        id = int(inputList[1])
        return (command, id)
    elif(command == "R"):
        if(len(inputList) != 3):
            return (-1)
        name = inputList[1]
        port = int(inputList[2])
        return (command, name, port)
    elif(command == "T"):
        if(len(inputList) != 1):
            return (-1)
        return (command)
    else:
        return (-1)

        

if __name__ == '__main__':
    client = DatabaseClient()
    treatedInput = handleUserInput()

    while(treatedInput[0] != "T"):
        if(treatedInput[0] == "I"):
            result = client.insert(treatedInput[1], treatedInput[2], treatedInput[3])
            print(result.existed)
        elif(treatedInput[0] == "C"):
            result = client.get(treatedInput[1])
            print(result[0], result[1])
        else:
            print("Invalid command")
            
        treatedInput = handleUserInput()

    if(treatedInput[0] == "T"):
        result = client.stopServer()
        print(result.numOfKeys)