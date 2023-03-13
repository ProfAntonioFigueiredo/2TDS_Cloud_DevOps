import os
import json
from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
from datetime import date, datetime

app = Flask(__name__)

# Configura as variáveis de ambiente para conexão com o banco de dados
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"]
AUTH_PLUGIN = os.environ["AUTH_PLUGIN"]

# Cria a conexão com o banco de dados
connection = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    auth_plugin=AUTH_PLUGIN,
    user=DB_USER,
    password=DB_PASSWORD,
    database=DB_NAME
)

# Cria a tabela 'out_stock' no banco de dados, caso ainda não exista
with connection.cursor() as cursor:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS out_stock (
            id INT NOT NULL AUTO_INCREMENT,
            codigo VARCHAR(255) NOT NULL,
            descricao VARCHAR(255) NOT NULL,
            data_solicitacao DATE NOT NULL,
            PRIMARY KEY (id)
        )
    """)

# Testar se o App está no ar: http://127.0.0.1:5000/
# Deve retornar: API is running! no Browser
@app.route("/")
def index():
    return "API is running!"

# Seleciona todos os registros da tabela 'out_stock'
# No Browser acesse: http://127.0.0.1:5000/out_stock
# para ver os produtos no navegador
@app.route("/out_stock", methods=["GET"])
def get_out_stock():
    try:
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM out_stock')
            records = cursor.fetchall()
            data = [{'id': record[0], 'code': record[1], 'description': record[2], 'date': record[3].strftime('%Y-%m-%d')} for record in records]
            return jsonify(data)
    except Error as e:
        print(e)
        return jsonify({'message': 'Erro ao buscar registros da tabela out_stock.'}), 500

# Insere registros no Banco (API)
@app.route("/out_stock", methods=["POST"])
def create_out_stock():
    # Obtém os dados enviados na requisição
    data = request.get_json()
    codigo = data["codigo"]
    descricao = data["descricao"]
    data_solicitacao = data["data_solicitacao"]

    # Insere os dados na tabela 'out_stock'
    with connection.cursor() as cursor:
        cursor.execute("""
            INSERT INTO out_stock (codigo, descricao, data_solicitacao)
            VALUES (%s, %s, %s)
        """, (codigo, descricao, data_solicitacao))
        connection.commit()

    # Retorna uma mensagem de sucesso como resposta
    return {"message": "Registro inserido com sucesso!"}

# Atualiza registros no Banco (API)
@app.route("/out_stock/<int:id>", methods=["PUT"])
def update_out_stock(id):
    # Obtém os dados enviados na requisição
    data = request.get_json()
    codigo = data["codigo"]
    descricao = data["descricao"]
    data_solicitacao = data["data_solicitacao"]

    # Atualiza os dados do registro com o ID especificado na tabela 'out_stock'
    with connection.cursor() as cursor:
        cursor.execute("""
            UPDATE out_stock
            SET codigo=%s, descricao=%s, data_solicitacao=%s
            WHERE id=%s
        """, (codigo, descricao, data_solicitacao, id))
        connection.commit()

    # Retorna uma mensagem de sucesso como resposta
    return {"message": "Registro atualizado com sucesso!"}

# Deleta registros no Banco (API)
@app.route("/out_stock/<int:id>", methods=["DELETE"])
def delete_out_stock(id):
    # Deleta o registro com o ID especificado na tabela 'out_stock'
    with connection.cursor() as cursor:
        cursor.execute("""
            DELETE FROM out_stock
            WHERE id=%s
        """, (id,))
        connection.commit()

    # Retorna uma mensagem de sucesso como resposta
    return {"message": "Registro deletado com sucesso!"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)