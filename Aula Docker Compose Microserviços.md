

-- Slide 8


git clone https://github.com/profjoaomenk/flask-microservice.git

cd flask-microservice



-- Slide 11

docker-compose up -d --build



-- Slide 13

docker-compose ps

docker-compose logs

docker network ls



-- Slide 14

http://localhost



-- Slide 15

docker exec -it flask-microservice-postgres-1 psql -U postgres

\c admdimdim

select * from visitors;



-- Slide 16

docker exec -it flask-microservice-redis-1 redis-cli

ou
docker exec -it flask-microservice-redis-2 redis-cli

select 0

KEYS *

get visitor_count



-- Slide 17

http://localhost/resetcounter



-- Slide 18

Postgres:

docker exec -it flask-microservice-postgres-1 psql -U postgres

\c admdimdim

select * from visitors;


Redis:

docker exec -it flask-microservice-redis-1 redis-cli

ou
docker exec -it flask-microservice-redis-2 redis-cli

select 0

KEYS *

get visitor_count




-- Slide 19

docker logs --follow flask-microservice-flaskapp-1



-- Slide 20

docker logs --follow flask-microservice-postgres-1

docker exec -it flask-microservice-postgres-1 psql -U postgres

/c admdindin



-- Slide 21

docker run --name teste -d ubuntu sleep 1d

Windows: 
docker inspect teste | findstr /i "mem"
docker inspect teste | findstr /i "cpu"

Linux / Mac:
docker inspect teste | grep -i mem
docker inspect teste | grep -i cpu




-- Slide 22

docker run --name teste-ctrl -m 1G --cpus=1 -d ubuntu sleep 1d

Windows:
docker inspect teste-ctrl | findstr /i "mem"
docker inspect teste-ctrl | findstr /i "cpu"


Linux / Mac:
docker inspect teste-ctrl | grep -i mem
docker inspect teste-ctrl | grep -i cpu




-- Slide 24

docker-compose down

docker container stop teste teste-ctrl 

docker system prune -a -f --volumes

