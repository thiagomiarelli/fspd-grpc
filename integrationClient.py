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
        Client function to call the rpc for GetIntegration
        """
        message = pb2.GetIntegrationParams(id=id)
        result = self.stub.GetIntegration(message)
        return (result.address, result.port)

    def registerIntegration(self, address, port, ids):
        """
        Client function to call the rpc for Register
        """
        message = pb2.RegisterIntegrationParams(address=address, port=port, ids=[1,2,3])
        result = self.stub.RegisterIntegration(message)
        print(result)
        return result

    def stopServer(self):
        """
        Close the gRPC channel
        """
        message = pb2.StopIntegrationServerParams()
        result = self.stub.StopIntegrationServer(message)
        return result

def handleUserInput():
    inputString = input("Enter your command: ")
    inputList = inputString.split(",")
        
    try:
        if(len(inputList) < 1):
            return [-1]
        
        command = inputList[0]
        if(command == "C"):
            if(len(inputList) != 2):
                return [-1]
            id = int(inputList[1])
            return (command, id)
        elif(command == "T"):
            if(len(inputList) != 1):
                return [-1]
            return (command)
        else:
            return [-1]
    except EOFError:
        return ["EOF"]


        



if __name__ == '__main__':
    if(len(sys.argv) != 2):
        print("Usage: python3 client.py <address:port>")
        exit(1)
    address = sys.argv[1]
    client = IntegrationClient(address)
    client.registerIntegration("localhost", 50051, [])
    treatedInput = handleUserInput()

    while(treatedInput[0] != "T"):
        if(treatedInput[0] == "C"):
            result = client.get(treatedInput[1])
            print(result)
        elif(treatedInput[0] == "EOF"):
            exit(0)
        else:
            print("Invalid command")

        treatedInput = handleUserInput()
    
    if(treatedInput[0] == "T"):
        client.stopServer()
        exit(0)
