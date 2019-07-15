from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = 'Gustavo'
    return render_template('index.html', nombre = name)

@app.route('/cliente')
def cliente():
    lista_nombres = ['Test1', 'Test2', 'Test3']
    return render_template('cliente.html', lista = lista_nombres)

if __name__ == '__main__':
    app.run(debug = True, port =  8000)