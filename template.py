from flask import Flask
from flask import render_template

app = Flask(__name__)

#todos los templates van en la carpeta templates
#el archivo .py que ejecuta y llama a los templates
#debe de estar un nivel por fuera de la carpeta templates
#si quiero usar una carpeta diferente para los templates, entonces
#app = Flask(__name__, template_folder='carpeta_nueva_templates')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, port =  8000)