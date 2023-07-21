# compilação dos protos
stubs:
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/database.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/integration.proto

# execução do servidor da parte 1, com a compilação, caso ainda não tenha sido feita
run_serv_dir: 
ifeq ($(wildcard ./protofiles/*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/database.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/integration.proto
	python3 server.py $(arg)
else
	python3 server.py $(arg)
endif

# execução do cliente da parte 1, com a compilação, caso ainda não tenha sido feita
run_cli_dir:
ifeq ($(wildcard ./protofiles/*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/database.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/integration.proto
	python3 client.py $(arg)
else
	python3 client.py $(arg)
endif

# execução do servidor da parte 2, com a compilação, caso ainda não tenha sido feita
run_serv_int:
ifeq ($(wildcard ./protofiles/*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/database.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/integration.proto
	python3 integrationServer.py $(arg)
else
	python3 integrationServer.py $(arg)
endif

# execução do cliente da parte 2, com a compilação, caso ainda não tenha sido feita
run_cli_int: 
ifeq ($(wildcard ./protofiles/*pb2*.py),)
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/database.proto
	python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./protofiles/integration.proto
	python3 integrationClient.py $(arg)
else
	python3 integrationClient.py $(arg)
endif

clean:
	rm -f protofiles/*pb2*.py