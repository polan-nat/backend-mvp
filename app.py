from flask import Flask, request, jsonify
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'projeto_crud'

mysql = pymysql.connect(
    host = app.config['MYSQL_HOST'],
    user = app.config['MYSQL_USER'],
    password = app.config['MYSQL_PASSWORD'],
    db = app.config['MYSQL_DB']
)

# Inicia a função para criar a tabela, caso ela não exista
# def create_table():
#     try:
#         print("Cria a tabela ===")
#         cur = mysql.cursor()
#         cur.execute(
#             '''
#             CREATE TABLE IF NOT EXISTS usuarios (
#             id INT AUTO_INCREMENT PRIMARY KEY,
#             nome VARCHAR(255) NOT NULL,
#             sobrenome VARCHAR(255) NOT NULL,
#             email VARCHAR(255)
#             )
#             '''
#         )
#         mysql.commit()
#         cur.close()
#         print('Tabela criada com sucesso ===')
#     except Exception as e:
#         print("Erro durante a criação da tabela", e)
        
@app.route('/')
def index():
    return 'Hello world!'

# Exibe lista de usuários
@app.route('/buscar_usuarios', methods=['GET'])
def buscar_usuarios():
    try:
        cur = mysql.cursor()
        cur.execute('SELECT * FROM usuarios')
        data = cur.fetchall()
        cur.close()
        
        items = [{'id': item[0], 'nome': item[1], 'sobrenome': item[2], 'email': item[3]} for item in data]
        
        response = {
            'error': False,
            'message': 'A busca pelos usuários foi bem-sucedida',
            'data': items
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'error': True,
            'message': f'Erro ao buscar os usuários: {e}',
            'data': None
        }
        return jsonify(response), 500

# Cadastra usuário  
@app.route('/cadastrar_usuario', methods=['POST'])
def cadastrar_usuario():
    try:
        data = request.get_json()
        
        nome = data['nome']
        sobrenome = data['sobrenome']
        email = data['email']
        
        cur = mysql.cursor()
        
        cur.execute('INSERT INTO usuarios(nome, sobrenome, email) VALUES(%s, %s, %s)', (nome, sobrenome, email))
        
        mysql.commit()
        cur.close()
        
        response = {
            'error': False,
            'message': 'Usuário adicionado com sucesso',
            'data': data
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'error': True,
            'message': f'Erro ao adicionar o usuário {e}',
            'data': None
        }
        return jsonify(response), 500

# Busca por usuário específico
@app.route('/buscar_usuario/<int:id>', methods=['GET'])
def buscar_usuario(id):
    try:
        cur = mysql.cursor()
        
        cur.execute('SELECT * FROM usuarios WHERE id = %s', (id, ))
        
        data = cur.fetchone()
        
        cur.close()
        
        if data is None: 
            response = {
                'error': True,
                'message': 'Usuário não encontrado',
                'data': None
            }
            return jsonify(response), 404
        
        response = {
            'error': False,
            'message': 'A busca pelo usuário foi bem sucedida',
            'data': data
        }
        return jsonify(response), 200   
    
    except Exception as e:
        response = {
            'error': False,
            'message': f'Erro ao buscar o usuário: {e}',
            'data': None    
        }
        return jsonify(response), 500
        
        
# Deleta usuário
@app.route('/deletar_usuario/<int:id>', methods=['DELETE'])
def deletar_usuario(id):
    try:
        cur = mysql.cursor()
        
        cur.execute("DELETE FROM usuarios WHERE id = %s", (id, ))

        mysql.commit()
        
        cur.close()
        
        response = {
            'error': False,
            'message': 'Usuário deletado com sucesso',
            'data': {'id': id}
        }
        return jsonify(response), 200
    except Exception as e:
        response = {
            'error': True,
            'message': f'Erro ao deletar o usuário: {e}',
            'data': None
        }
        return jsonify(response), 500
    
    
if __name__ == '__main__':
    # create_table() 
    app.run(debug=True)