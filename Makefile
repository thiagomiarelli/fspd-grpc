.PHONY: run_serv_dir run_cli_dir run_serv_int run_cli_int

run_serv_dir:
	python3 server.py $(arg)

run_cli_dir:
	python3 client.py $(arg)

run_serv_int:
	python3 integrationServer.py $(arg)

run_cli_int:
	python3 integrationClient.py $(arg)
