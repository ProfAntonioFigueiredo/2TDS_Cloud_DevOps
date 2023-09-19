FROM debian
     LABEL maintainer 'Juracy Filho <juracy at gmail.com>'
     ARG S3_BUCKET=files
     ENV S3_BUCKET=${S3_BUCKET}

#docker image build -t ex-build-arg .
#docker container run ex-build-arg bash -c 'echo $S3_BUCKET' # Saída esperada: files

docker image build --build-arg S3_BUCKET=myapp -t ex-build-arg .
docker container run ex-build-arg bash -c 'echo $S3_BUCKET' # Saída esperada: myapp


Exemplo de uso das instruções: FROM, LABEL, ARG e ENV.

Os labels podem ser extraídos futuramente da imagem, o comando abaixo extrai o
mantenedor da imagem que acabamos de criar.


docker image inspect --format="{{index .Config.Labels \"maintainer\"}}"
ex-build-arg

