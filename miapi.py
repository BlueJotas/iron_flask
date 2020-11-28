from flask import Flask, request
#instalar librería md ojito
import markdown.extensions.fenced_code
import random
import json
import tools.getdata as get
import tools.postdata as pos

app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("README.md","r")
    md_template_string = markdown.markdown(readme_file.read(), extensions = ["fenced_code"])
    return md_template_string



@app.route("/ejemplo1")
def datitos():
    diccionario = { "Nombre" : "Fer",
    "Amigos" : ["Dobby", "Ras","Sheriff","Ignacio"],
    "Edad" : 28
    }
    return diccionario

@app.route("/tiraeldado")
def dados():
    dato = str(random.choice(range(1,7)))
    dato_pars = { "Has sacado un " : f"{dato}"

    }
    return f"{dato}"

@app.route("/frases/<personaje>")
def frasepersonaje(personaje):
    #la función get.pensajepersonaje viene de tools getdata.py
    frases = get.mensajepersonaje(personaje)
    return json.dumps(frases)


"""
Revisad esta documentación para métodos post y tal
https://flask.palletsprojects.com/en/1.1.x/quickstart/#the-request-object
"""

@app.route("/nuevafrase",methods=["POST"])
def insertamensaje():
    escena = request.form.get("scene")
    personaje = request.form.get("character_name")
    frase = request.form.get("dialogue")
    pos.insertamensaje(escena,personaje,frase)
    return "Mensaje introducido correctamente en la base de datos"

























app.run(debug=True)