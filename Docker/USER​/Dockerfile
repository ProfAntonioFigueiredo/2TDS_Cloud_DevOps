FROM node:alpine

RUN adduser -h /home/menk -s /bin/bash -D menk
USER menk
RUN whoami
RUN touch /home/menk/teste.txt

USER node

RUN whoami

RUN touch /home/node/teste.txt

#Executar mais de um comando com a instrução CMD​

CMD ls -l /home/menk; ls -l /home/node
docker build -t user-demo .
docker container run --rm user-demo
