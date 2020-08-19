# Shell reverso

Um simples shell reverso feito em python, fiz seguindo as dicas [deste tutorial](https://www.thepythoncode.com/article/create-reverse-shell-python), e com o tempo irei adicionando recursos por conta própria.

- `client.py` é enviado para a vítima
- `server.py` recebe a conexão reversa

## Parâmetros

É necessário criar um arquivo `.env` nessa mesma pasta, contendo os seguintes parâmetros:

|Parâmetro|Descrição|
|--|--|
|`URL`|Endereço de host do server|
|`PORT`|Porta|
