from flask import Flask, render_template, request

app = Flask(__name__)

#rutas
@app.route("/casa")
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/novo")

def nova():
    return "Nova pagina"


@app.route("/nome/<string:nom>")

def nome(nom):
    return f"Seu nome é {nom}"


@app.route("/valor")
def valor():
    valor = "Uma estringue"
    numerus = 1
    aranjo = [1, 2, 3, 4, 5]

    return render_template("seuvalor.html", val=valor, num=numerus, aranj=aranjo)


#************************** area de inputs
@app.route("/infos")
def infos():

    return render_template("inputs.html")

@app.route("/infos/show", methods=["POST"])
def infoss():
    nom = request.form.get('nomex') #pega o input com name='nomex'
    return render_template("valcolocado.html", nomes=nom)

# todo codigo fica acima
#serve para atualizar automaticamente o server ************************************
if __name__ == "__main__":
    app.run(debug=True)


