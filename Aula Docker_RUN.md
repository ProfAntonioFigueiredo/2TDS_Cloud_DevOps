
-- Slide 13

https://linuxways.net/centos/what-is-the-difference-between-lxc-lxd-and-docker-containers/
https://www.educba.com/lxc-vs-docker/
https://www.upguard.com/blog/docker-vs-lxc
https://medium.com/@harsh.manvar111/lxc-vs-docker-lxc-101-bd49db95933a



-- Slide 26
https://docs.docker.com


-- Slide 27
https://github.com/docker


-- Slide 28
https://www.docker.com/products/docker-hub



-- Slide 34
https://www.docker.com/products/docker-hub



-- Slide 36
https://docs.docker.com/engine/reference/commandline/pull/



-- Slide 39

docker pull ubuntu


-- Slide 41

docker image ls

ou antigo: docker images



-- Slide 42

docker container run ubuntu

ou antigo: docker run ubuntu


-- Slide 43

docker container run ubuntu echo "Rodando Ubuntu"

docker container run -it ubuntu /bin/bash
#apt-get update
#apt-get install curl
#apt-get install ifconfig 
#curl https://www.google.com

#sudo docker container run nginx ( Rodando continuamente )
#sudo docker container run -d nginx ( Rodando contunuamente e liberar o Terminal)
[operacoes@OracleLinux FIAP - DEVOPS TOOLS  CLOUD COMPUTING-2]$ sudo docker container run -d nginx
4e853fe1fa99ed539a0be6f1419a436ff2ba6fafcdca978000743128aa5b681d

#Expondo o Container através do Container -P 
sudo docker container run --name mynginx -d -p 8080:80 nginx 
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                                   NAMES
526982f4320a   nginx     "/docker-entrypoint.…"   6 seconds ago    Up 4 seconds    0.0.0.0:8080->80/tcp, :::8080->80/tcp   nifty_merkle
4e853fe1fa99   nginx     "/docker-entrypoint.…"   3 minutes ago    Up 3 minutes    80/tcp                                  exciting_dubinsky
ac0f2a2490c3   ubuntu    "/bin/bash"              16 minutes ago   Up 16 minutes                                           zealous_perlman

# Rodando o MongoDB com Docker  - p 27017:27017 
sudo docker container run --name bd_mongo -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=admin mongo

#Robot 3T - Conexão Mongo DB Data Base
https://studio3t.com/download-thank-you/?OS=osx

#Troubleshooting 
#- Conectando no Terminal do Container 
#sudo docker container exec -it 7027c7b29db6 /bin/bash

sudo docker container logs
sudo docker container logs -n 5 236ba7d4b8ae
sudo docker container logs -f (Following)
sudo docker container logs -t (Timming)




-- Slide 46

docker image ls

docker container ls

docker container ls -a


-- Slide 47

docker info

docker version

docker --help

docker search <img>

Ex.: 
docker search ubuntu



-- Slide 49

docker pull centos

docker image list


-- Slide 50

docker container run --name linux_mobile -it -e TZ=America/Sao_Paulo centos /bin/bash

date
pwd
whoami
ls


-- Slide 51

mkdir arq_transf

cd arq_transf

touch primeiro_arq.txt 

vi primeiro_arq.txt

exit


-- Slide 52

docker container start linux_mobile -i


-- Slide 54

docker container run --name bd_portalweb -e MYSQL_ROOT_PASSWORD=@Fiap2tds2023 -d mysql/mysql-server:latest



-- Slide 56

docker container exec -it bd_portalweb bash

mysql -u root -p

Senha: 
@Fiap2tds2023



-- Slide 57

select @@version;

create database bdfiap;

create user 'fiap'@'localhost' IDENTIFIED BY '@Fiap2tds2023';​

grant all on bdfiap.* TO 'fiap'@'localhost’;

flush privileges;

show databases;


-- Slide 58


exit;

mysql -u fiap -p

Senha: 
@Fiap2tds2023

use bdfiap;

create table t_aluno ( rm_aluno varchar(07), nm_aluno varchar(80), dt_nascimento date );

insert into t_aluno (rm_aluno, nm_aluno, dt_nascimento) values ("RM3344", "Maria Linda", "2000-03-19");

select * from t_aluno;

exit


-- Slide 59

Para entrar novamente no Container:
docker container exec -it bd_portalweb bash

Parando o Container:
docker container stop bd_portalweb



-- Slide  61

docker volume ls

docker volume create logdata


-- Slide 62

docker volume ls


Windows:

Se for Docker Engine v20.10.16:
\\wsl$\docker-desktop-data\data\docker\volumes

Se for Docker Engine v19.03:
\\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes\


Mac Linux:
/var/lib/docker/volumes


*** ATENÇÃO ***
No Mac o Docker roda em ema pequena máquina Virtual, então para acessar o /var/lib/docker/volumes rode esse comando em um Terminal:

nc -U ~/Library/Containers/com.docker.docker/Data/debug-shell.sock

ou

screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty

Depende da Versão do Docker e da versão do SO do Mac


 
-- Slide 63

docker container run -it --name apl_web_dimdim -v logdata:/volumedimdim alpine

ls -l



-- Slide 64

cd volumedimdim

pwd

echo Ola do Container > arquivo_linux_alpine.txt

ls -l


-- Slide 66

docker container inspect linux_mobile


-- Slide 67

docker container stop apl_web_dimdim


-- Slide 68

docker container start apl_web_dimdim

docker container restart apl_web_dimdim


-- Slide 69

docker container ls -a

docker container rm linux_mobile


-- Slide 70

docker container stop $(docker container ls -q)

docker container rm $(docker container ls -aq)

docker image rm $(docker image ls -aq)

docker volume rm $(docker volume ls -q)


-- Slide 71

docker system prune -a -f --volumes


Dockerfile


-- Slide 75


Arquivo:
Dockerfile


FROM ubuntu

RUN apt-get -y update
RUN apt-get -y install python3


-- Slide 76

https://hub.docker.com/_/scratch



-- Slide 77

docker build .



-- Slide 78

docker image ls

docker image rm <ID>

docker build -t ubuntu_python .


-- Slide 79

docker image ls


-- Slide 80

docker container run -it ubuntu_python /bin/bash

python3 -V


-- Slide 81

FROM ubuntu
RUN apt-get -y update
RUN apt-get -y install python3
RUN touch arquivo-de-boas-vindas.txt


docker build -t ubuntu_python .


-- Slide 83

docker container run -it ubuntu_python /bin/bash

python3 -V

ls /


-- Slide 84

FROM ubuntu

RUN apt-get update -y
RUN apt-get install openjdk-8-jdk –y

ADD Dockerfile /root/arquivo-host-transferido.txt


docker build -t teste .


docker container run --name testeadd -it teste /bin/bash


-- Slide 85


FROM ubuntu

EXPOSE 80/tcp
EXPOSE 80/udp


docker build -t teste .

docker container run --name testeexpose -it teste bash

docker image inspect --format='' teste



-- Slide 87


docker run -d --name nginx-server -p 80:80 nginx

localhost:80

docker container stop nginx-server

docker container rm nginx-server


-- Slide 88

Crie o arquivo no seu Host, no Terminal execute:

echo { "nome": "Robert Plant",  "banda": "Led Zeppelin" } > arquivo-host.json



FROM ubuntu:18.04

WORKDIR /app-java 

ADD arquivo-host.json arquivo-host-transferido.json

docker build -t teste .

docker container run --name testeworkdir -it teste bash

Ao sair do terminal:
docker container start testeworkdir -i


-- Slide 89

FROM alpine
CMD ["echo","Rodei na execução"]

docker build -t testecmd .

docker container run --rm testecmd


-- Slide 90

git clone https://github.com/profjoaomenk/Docker-NodeJs-HelloWorld.git

cd Docker-NodeJs-HelloWorld

docker build -t nodehelloworld .

docker container run -d -p 3030:3030 --name apphello nodehelloworld

http://localhost:3030

docker container stop apphello

docker container start apphello


-- Slide 91

FROM alpine
ENTRYPOINT exec top -b

docker build -t ptoentrada .

docker container run --rm ptoentrada


-- Slide 93

FROM alpine
ENTRYPOINT ["echo", "Helo,"]
CMD ["World"]

docker build -t teste .

docker container run --name appentryecmd teste

docker container rm appentryecmd

docker container run --name appentryecmd teste "João"


-- Slide 95

FROM alpine
ARG nome=João
RUN echo "Olá! Bem-vinde $nome" > bem-vinde.txt
ENTRYPOINT cat bem-vinde.txt


docker build -t arg-demo .

docker container run --rm arg-demo


docker build -t arg-demo --build-arg nome=Maria .

docker container run --rm arg-demo


-- Slide 96

FROM ubuntu
ARG PYTHON_VERSION
RUN apt-get update -y
RUN apt-get install python${PYTHON_VERSION} -y


docker build -t arg-version --build-arg PYTHON_VERSION="2" .

docker container run --rm -it  arg-version bash

python2 -v


docker build -t arg-version --build-arg PYTHON_VERSION="3" .

docker container run --rm -it  arg-version bash

python2 -v
python3 -v



-- Slide 97


FROM ubuntu

ENV hey="Olá"
ENV dir="/"

# O ENV também pode ser utilizado na construção
ADD ./Dockerfile ${dir}

CMD echo $hey


docker build -t env-demo .

docker container run --rm env-demo


ocker container run --rm -e hey="Salve" env-demo

docker container run --rm -it env-demo bash


-- Slide 98

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





--- Desafio



1) Primeiro crie um Volume Nomeado com o comando

docker volume create nginx-data

-- Verificar o Volume criado (Verifique a propriedade Mountpoint)
docker volume inspect nginx-data


2) Rode o Container

docker run --name nginx -d -v nginx-data:/usr/share/nginx/html -p 80:80 nginx


3) Acesse seu Web Browser em localhost:80 e verifique se o servidor funciona


4) Altere os arquivos solicitados na pasta que é mostrada em Mountpoint no Volume nomeado em seu Host

50x.html
index.html



Windows
------------

Se for Docker Engine v20.10.16:
\\wsl$\docker-desktop-data\data\docker\volumes


Se for Docker Engine v19.03:
\\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes\



MacOS
----------

No Mac o Docker roda em ema pequena máquina Virtual, então para acessar o /var/lib/docker/volumes rode:

nc -U ~/Library/Containers/com.docker.docker/Data/debug-shell.sock

ou
screen ~/Library/Containers/com.docker.docker/Data/vms/0/tty

Depende da Versão do Docker e Mac


Diretório Mac e Linux:

/var/lib/docker/volumes



5) Rode o Container e teste as alterações




-- Limpar Lab
docker system prune -a -f --volumes

