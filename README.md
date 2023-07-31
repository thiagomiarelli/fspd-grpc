# TP2 Fundamentos de Sistemas Paralelos e Distribuídos
Essa aplicação implementa dois servidores e dois clientes utilizando gRPC. O primeiro par de servidor e cliente são os diretórios locais. O servidor de diretório armazena chaves com valores e descrições que podem ser criados e consultados pelo cliente do diretório local. O segundo par de cliente e servidor são os de integração. Eles recebem informação sobre os dados que estão em cada servidor e direcionam a busca do cliente para obter o dado no servidor correto. 

### Requisitos

- Python 3.4 ou superior
- Biblioteca gRPC instalada

### Como executar?

1. Executar o servidor de diretórios com o comando `make run_serv_dir arg=<port>`, passando a porta que deseja inicializar o servidor. Exemplo:
```bash
make run_serv_dir arg=3000
```
2. Executar o cliente do servidor de diretórios com o comando `make run_cli_dir arg=<address><port>`, passando o endereço e porta. Exemplo:
```bash
make run_cli_dir arg=localhost:3000
```
3. Executar o servidor de integração com o comando `make run_serv_int arg=<port>`, passando a porta. Exemplo:
```bash
make run_serv_int arg=3001
```
4. Executar o cliente do servidor de integração com o comando `make run_cli_int arg=<address><port>`, passando o endereço e porta. Exemplo:
```bash
make run_cli_int arg=localhost:3001
```

## Comandos
### Servidor de Diretórios
1. Inserir: insere um valor e descrição associado a uma chave com o comando `I,<chave>,<descricao>,<valor>`
```bash
I,3,chave 1,3.4
```
2. Consultar: busca um valor e descrição utilizando uma chave `C,<chave>`
```bash
C,3
```
3. Registrar: envia informações para o servidor de integração sobre suas chaves utilizando `R,<endreco>,<porta>`
```bash
R,localhost,3001
```
4. Terminar: encerra a conexão entre servidor e cliente, encerrando ambos com o comando `T`

### Servidor de Integração
1. Consultar: busca o servidor em que a chave está no servidor de integração e, em seguida, busca o valor no servidor de diretórios com o comando `C,<chave>`
```bash
C,3
```
2. Terminar: encerra a conexão entre servidor e cliente, encerrando ambos com o comando `T`

