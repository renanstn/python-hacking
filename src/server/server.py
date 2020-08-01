import socket


SERVER_HOST = '0.0.0.0'
SERVER_PORT = 5003
BUFFER_SIZE = 1024 # Envia 1024 bytes (1 kb) por vez

s = socket.socket()

# Escutar
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
print(f"Escutando em {SERVER_HOST}:{SERVER_PORT} ...")

# Receber conexão
client_socket, client_address = s.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")
message = "Hello and Welcome".encode()
client_socket.send(message)

while True:
    try:
        command = input("\nDigite o comando que deseja executar:\n>")
        client_socket.send(command.encode())
        if command.lower() == "exit":
            break
        # Recebe o resultado do comando
        print("Aguardando resposta...")
        response = client_socket.recv(BUFFER_SIZE).decode()
        print(response)
    except KeyboardInterrupt:
        print("Servidor finalizado")
        client_socket.close()
        s.close()
    except Exception as e:
        print("Deu ruim...")
        print(e)
        client_socket.close()
        s.close()

# Fecha a conexão com o client
client_socket.close()
# Fecha a conexão do server
s.close()
