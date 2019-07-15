from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Cambios hechos por Gustavo'

#Presenta el parámetro
#http://localhost:8000/params?params1=Gustavo_Contreras 
#http://localhost:8000/params?params1=Gustavo_Contreras&params2=Test_dos

#En caso de que no lo tenga, muestra el mensaje
#http://localhost:8000/params

@app.route('/params')
def params():
    param = request.args.get('params1','No contiene este parámetro')
    param_dos = request.args.get('params2', 'No contiene este parámetro')
    return 'El parámetro es {}, {}'.format(param, param_dos)

if __name__ == '__main__':
    app.run(debug = True, port =  8000)