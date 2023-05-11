from flask import Flask, request, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gravar', methods=['POST', 'GET'])
def gravar():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    if nome and email and senha:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("insert into tbl_user (user_name, user_username, user_password) values (%s, %s, %s);", (nome, email, senha))
        conn.commit()
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)