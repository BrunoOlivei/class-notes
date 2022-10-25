# Docker

No git bash ou ubuntu:

Dentro do diretório do projeto o comando para atualizar a imagem do docker:

`$ ./deploy-prod.sh — dev`

Após atualização e criação da imagem, se for necessário, podemos executar o comando para verificar o status:

`$ docker ps`

Run direto no terminal

`docker-compose up --build`

Rodando o terminal da imagem do Docker:

`docker exec -it '<nome-do-container>' /bin/sh`

Limpando dados Docker

`wsl --unregister docker-desktop-data`

`wsl --unregister docker-desktop`