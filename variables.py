from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/user/<name>')
def user(name='Gustavo'):
    edad = 30
    mi_lista = [1, 2, 3, 4]
    return render_template('user.html', nombre = name, edad = edad, lista = mi_lista)

if __name__ == '__main__':
    app.run(debug = True, port =  8000)