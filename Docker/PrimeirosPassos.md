Docker container run –name –hello world  

Docker container run –it ubuntu /bin/bash ( INTERATIVO ) - SIMPLES
docker container run -it --name MyfirstConatiner  ubuntu /bin/bash (Nomeando)

Removendo Container 
Docker container rm ( Nome ou ID)

Declarar para criar e excluir apos o uso

docker container run --name meucontainer --rm hello-world

sudo docker container run -d -p 8080:80 --name wiseti_nginx nginx 

sudo docker container run -d -p 27017:27017 --name wise_mongo -e MONGO_INITDB_ROOT_USERNAME=mongouser -e MONGO_INITDB_ROOT_PASSWORD=mongopwd mongo 

Troubleshotting  

sudo docker container inspect ad730c0fa96e 
sudo docker container inspect ad730c0fa96e |grep -i mem 
sudo docker container inspect ad730c0fa96e |grep -i cpu 
sudo docker container exec -it ad730c0fa96e /bin/bash 
sudo docker container logs ad730c0fa96e 
sudo docker container logs -n 5 ad730c0fa96e 
sudo docker container logs –f  ad730c0fa96e 
sudo docker container logs –t  ad730c0fa96e 

 