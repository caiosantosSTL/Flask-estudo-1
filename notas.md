# Introducao em flask

comecamos instalando com o comando abaixo

    pip install Flask

Depois criamos uma pasta para o projeto, e quando criar um arquivo <br>
`arquivo.py` vamos fazer as importacoes dos modulos de flask.

***
No arquivo `app.py` vamos colocar tais codigos principais:
    
    from flask import Flask

    app = Flask(__name__)

Podemos ver que o `from flask import Flask` vai importar tudo que precisamos e <br>
`app = Flask(__name__)`  para saber se a aplicacao esta sendo executada num arquivo principal ou exportada.

    #rutas
    @app.route("/")

    def index():
        return "Oi oi "

Acima vemos que colocamos um metodo que retorna um texto e acima do metodo, vemos a rota 
onde levara para o metodo criado.

***
## Conectar o servidor

Para conectar temos que salvar o arquivo criado:

    $export FLASK_APP=app.py
    $flask run
>Usamos o bash do git para fazer isso pois no terminal win nao funciona direito

E depois disso, fazemos um flask run, no qual vai dar a rota para abrir o app web no navegador. `Running on http://127.0.0.1:5000/`

Neste codigo abaixo, podemos colocar informacoes em uma uri:

    @app.route("/nome/<string:nom>")

    def nome(nom):
        return f"Seu nome é {nom}"

Notemos que em return tem um f ao lado da string, para fazer funcionar a aparicao da variavel colocada na uri. Fazemos muito isso para ligar um id, e esse id ser levado para o metodo e entao, liberar uma pagina mostrando as informacoes deste id.

>Num formulario html, levamos os dados para a uri, e da uri leva para o metodo do controlador e com isso, o metodo retorna um valor para o usuario.

    if __name__ == "__main__":
        app.run(debug=True)
    
>Esse codigo ajuda a atualizar o servidor automatico

No terminal colocamos `python app.py`

Esse é o modo desenvolvimento, onde temos atualizacao automatica, no 
modo de producao, nao é recomendado. Modo producao é quando queremos ligar um servidor para disponibilizar o serviço e somente isso.
***
## Templates
Podemos criar uma pasta de para os templates e em `app.py` importamos o `render_template`
com isso podemos em return colocar isso:

    @app.route("/casa")
    @app.route("/")

    def index():
        return render_template("index.html")

Onde vai pegar o arquivo html e renderizar na tela.

Para passa um dado do controller para a vista, fazemos isso:

    @app.route("/valor")

    def valor():
        valor = "Uma estringue"

        return render_template("seuvalor.html", val=valor)

Notemos o `val=valor` onde val é a variavel que vai ter que aparecer na pagina html para 
revelar o valor.

No html usamos um render `jinja` no qual criamos tags deste tipo `{{ var }}` ou `{% x %}`

```html

    {% if num == 1%}
        <p>Valor unitario</p>
    {% else %}
        <p>Valor nao é nitario</p>
    {% endif %}

```
>podemos usar if sistema usandos tais tags 

## Heranças html
Podemos tambem fazer heranças de html.

    {% block body %} {% endblock %}

>Usamos para indicar que tal area vai ser extendida de outro lugar

    {% extends "nome.html" %}

>Indica que tal arquivo atual vai extender o arquivo

## Inputs

    #************************** area de inputs
    @app.route("/infos")
    def infos():

        return render_template("inputs.html")

    @app.route("/infos/show", methods=["POST"])
    def infoss():
        nom = request.form.get('nomex') #pega o input com name='nomex'
        return render_template("valcolocado.html", nomes=nom)

Na area de inputs com form, criamos duas rotas, uma para levar a pagina html que
tem o formulario, e a segunda rota leva a pagina que mostra a informacao colocada no
formulario.

Podemos ver que a rota 1, leva somente para uma vista, enquanto a rota 2, tem que pegar o 
dado enviado pelo formulario, e mostrar na nova vista.
