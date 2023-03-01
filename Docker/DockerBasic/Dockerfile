#FROM > Inicializa o build de uma imagem a partir de uma imagem base
#RUN > Executa um comando
#LABEL > Adiciona metadados a imagem
#CMD > Define o comndo e/ou os parametros padrao
#EXPOSE > Define que o container precisa expor a porta em questão
#ARG > Define um argumento para ser usado no processo de construcao
#ENV > Define variaveis de ambiente
#ADD > Copia arquivos ou diretorios ou arquivos remotos e adiciona ao sistema de arquivos da imagem
#COPY > Copia arquivos ou diretorios e adiciona ao sistema de arquivos da Imagem
#ENTRYPOINT > Ajuda voce a configurar um container que pode ser executado como um executavel
#VOLUME > DEfine volumes que devem ser definidos
#WORKDIR > Define o seu diretorio corrente

# docker image build -t ubuntu/dockerimage-basic:v1 .

FROM ubuntu
RUN apt-get update && apt-get install curl --yes && apt-get install vim --yes && apt-get install docker.io --yes

