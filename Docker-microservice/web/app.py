from flask import Flask
import logging
import psycopg2
import redis
import sys

app = Flask(__name__)

# Coenxão com o Redis - Procure pela palavra "cache" no fonte para verificar as operações
cache = redis.StrictRedis(host='redis', port=6379)

# Configura o Logging
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

# Procure pela palavra "PgFetch" para ver as operações no Postgres
def PgFetch(query, method):

    # Realiza a conexão com o Postgres
    conn = psycopg2.connect("host='postgres' dbname='admdimdim' user='postgres' password='admdimdim'")

    # Abre o cursor para realizar as operações
    cur = conn.cursor()

    # Executa o comando para selecionar ou manipular dados no Banco Postgres
    dbquery = cur.execute(query)

    if method == 'GET':
        result = cur.fetchone()
    else:
        result = ""

    # Realiza o commit
    conn.commit()

    # Fecha a comunicação com o banco
    cur.close()
    conn.close()
    return result

# Rota para a página principal do Contador de Visitas
@app.route('/')
def hello_world():

    # Nome da Chave a ser criada no Redis: visitor_count 
    if cache.exists('visitor_count'):
        cache.incr('visitor_count')
        count = (cache.get('visitor_count')).decode('utf-8')
        update = PgFetch("UPDATE visitors set visitor_count = " + count + " where site_id = 1;", "POST")
    else:
        cache_refresh = PgFetch("SELECT COALESCE(visitor_count,0) FROM visitors where site_id = 1;", "GET")

        if cache_refresh == None:
          count = 0
        else:
           count = int(cache_refresh[0])

        cache.set('visitor_count', count)
        cache.incr('visitor_count')
        count = (cache.get('visitor_count')).decode('utf-8')
    return 'Olá!  Essa página já foi visistada %s vez(es).' % count

# Rota para zerar o contador de visitas
@app.route('/resetcounter')
def resetcounter():
    cache.delete('visitor_count')
    PgFetch("UPDATE visitors set visitor_count = 0 where site_id = 1;", "POST")
    app.logger.debug("reset visitor count")
    return "A contagem foi reiniciada com a limpeza de dados dos Bancos: Redis e Postgres"