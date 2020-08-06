# Keylogger

Um keylogger simples, registra todas as teclas digitadas pelo usuário, e a cada X segundos faz um POST em um endpoint enviando os dados.

Os dados são recebidos pelo `receiver.py`, que o armazena em formato de log.
