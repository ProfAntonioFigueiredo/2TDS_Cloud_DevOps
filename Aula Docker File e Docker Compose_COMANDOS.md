
--- DOCKER FILE ---


-- Slide 6


Arquivo:
Dockerfile


FROM ubuntu

RUN apt-get -y update
RUN apt-get -y install python3


-- Slide 7

https://hub.docker.com/_/scratch



-- Slide 8

docker build .



-- Slide 9

docker image ls

docker image rm <ID>

docker build -t ubuntu_python .


-- Slide 10

docker image ls


-- Slide 11

docker container run -it ubuntu_python /bin/bash

python3 -V

exit


-- Slide 12


FROM ubuntu
RUN apt-get -y update
RUN apt-get -y install python3
RUN touch arquivo-de-boas-vindas.txt


docker build -t ubuntu_python .


-- Slide 14

docker container run -it ubuntu_python /bin/bash

python3 -V

ls /


-- Slide 15

FROM ubuntu

RUN apt-get update -y
RUN apt-get install openjdk-8-jdk –y

ADD Dockerfile /root/arquivo-host-transferido.txt


docker build -t teste .


docker container run --name testeadd -it teste /bin/bash

npm –v

exit


-- Slide 16


FROM ubuntu

EXPOSE 80/tcp
EXPOSE 80/udp


docker build -t teste .

docker image inspect --format='' teste

docker container run --name testeexpose -it teste bash

Em outro Terminal execute: 

docker ps



-- Slide 18


docker run -d --name nginx-server -p 80:80 nginx

localhost:80

docker container stop nginx-server

docker container rm nginx-server


-- Slide 19


Crie o arquivo no seu Host, no Terminal execute:

echo { "nome": "Robert Plant",  "banda": "Led Zeppelin" } > arquivo-host.json



FROM ubuntu:18.04

WORKDIR /app-java 

ADD arquivo-host.json arquivo-host-transferido.json


docker build -t teste .


docker container run --name testeworkdir -it teste bash

Ao sair do terminal:
docker container start testeworkdir -i


-- Slide 20

FROM alpine
CMD ["echo","Rodei na execução"]

docker build -t testecmd .

docker container run --rm testecmd


-- Slide 21

git clone https://github.com/profjoaomenk/Docker-NodeJs-HelloWorld.git

cd Docker-NodeJs-HelloWorld

docker build -t nodehelloworld .

docker container run -d -p 3030:3030 --name apphello nodehelloworld

http://localhost:3030

docker container stop apphello

docker container start apphello

docker container stop apphello


-- Slide 22

FROM alpine
ENTRYPOINT exec top -b

docker build -t ptoentrada .

docker container run --rm ptoentrada

docker container run --rm ptoentrada -n 3


Documentação Linux:  -n N -> Exit after N iterations



-- Slide 24

FROM alpine
ENTRYPOINT ["echo", "Helo,"]
CMD ["World"]

docker build -t teste .

docker container run --name appentryecmd teste

docker container rm appentryecmd

docker container run --name appentryecmd teste "João"


-- Slide 26

FROM alpine
ARG nome=João
RUN echo "Olá! Bem-vinde $nome" > bem-vinde.txt
ENTRYPOINT cat bem-vinde.txt


docker build -t arg-demo .

docker container run --rm arg-demo


docker build -t arg-demo --build-arg nome=Maria .

docker container run --rm arg-demo


-- Slide 27

FROM ubuntu
ARG PYTHON_VERSION
RUN apt-get update -y
RUN apt-get install python${PYTHON_VERSION} -y


docker build -t arg-version --build-arg PYTHON_VERSION="2" .

docker container run --rm -it  arg-version bash

python2 -V



docker build -t arg-version --build-arg PYTHON_VERSION="3" .

docker container run --rm -it  arg-version bash

python2 -V

python3 -V



-- Slide 28


FROM ubuntu

ENV hey="Olá"
ENV dir="/"

# O ENV também pode ser utilizado na construção
ADD ./Dockerfile ${dir}

CMD echo $hey


docker build -t env-demo .

docker container run --rm env-demo


docker container run --rm -e hey="Salve" env-demo

docker container run --rm -it env-demo bash


-- Slide 29

FROM node:alpine

RUN adduser -h /home/menk -s /bin/bash -D menk

USER menk
RUN whoami
RUN touch /home/menk/teste.txt

USER node
RUN whoami
RUN touch /home/node/teste.txt

#Executar mais de um comando com a instrução CMD
CMD ls -l /home/menk; ls -l /home/node


docker build -t user-demo .

docker container run --rm user-demo


-- Slide 31

docker system prune -a -f --volumes




--- DOCKER COMPOSE ---


-- Slide 41

docker-compose --version


-- Slide 42

git clone https://github.com/profjoaomenk/out_stock.git

cd out_stock


-- Slide 45

docker-compose up -d --build


-- Slide 49

mysql -u admdimdim -p


-- Slide 50

show databases;

use out_stock;

SELECT * FROM out_stock;

DESCRIBE out_stock;

SHOW TABLES;

SHOW GRANTS FOR admdimdim;

exit


-- Slide 51

http://127.0.0.1:5000/


-- Slide 52

docker-compose ps

docker-compose logs


-- Slide 53

docker network ls

docker network inspect out_stock_outstock_network


-- Slide 54

docker volume ls

docker volume inspect out_stock_db_data


-- Slide 56

docker exec -it db mysql -uadmdimdim -p

show databases;
use out_stock;
SELECT * FROM out_stock;


docker exec -it outstock /bin/bash
cat /etc/os-release


-- Slide 57

** Para quem irá executar via Terminal (Linux / Mac)

Select:
curl http://localhost:5000/out_stock

Insert:
curl -X POST -H "Content-Type: application/json" -d '{"codigo": "001", "descricao": "Produto 1", "data_solicitacao": "2022-03-10"}' http://localhost:5000/out_stock
curl -X POST -H "Content-Type: application/json" -d '{"codigo": "002", "descricao": "Produto 2", "data_solicitacao": "2022-03-10"}' http://localhost:5000/out_stock
curl -X POST -H "Content-Type: application/json" -d '{"codigo": "003", "descricao": "Produto 3", "data_solicitacao": "2022-03-10"}' http://localhost:5000/out_stock

Update:
curl -X PUT -H "Content-Type: application/json" -d '{"codigo": "001", "descricao": "Produto 1 atualizado", "data_solicitacao": "2022-03-09"}' http://localhost:5000/out_stock/1
curl -X PUT -H "Content-Type: application/json" -d '{"codigo": "001", "descricao": "Produto dois", "data_solicitacao": "2022-03-10"}' http://localhost:5000/out_stock/2


Delete:
curl -X DELETE http://localhost:5000/out_stock/003


-- Slide 58

http://localhost:5000/out_stock


-- Slide 60

http://localhost:5000/out_stock

{"codigo": "001", "descricao": "Produto 1", "data_solicitacao": "2022-03-10"}
{"codigo": "002", "descricao": "Produto 2", "data_solicitacao": "2022-03-10"}
{"codigo": "003", "descricao": "Produto 3", "data_solicitacao": "2022-03-10"}


-- Slide 61

URL
http://localhost:5000/out_stock/1

Linha
{"codigo": "001", "descricao": "Produto 1 atualizado", "data_solicitacao": "2022-03-09"}


URL
http://localhost:5000/out_stock/2

Linha
{"codigo": "002", "descricao": "Produto dois", "data_solicitacao": "2022-03-10"}


-- Slide 62

http://localhost:5000/out_stock/3


-- Slide 65

docker-compose down

docker system prune -a -f --volumes

