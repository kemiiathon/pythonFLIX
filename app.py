from flask import Flask, render_template
import urllib.request,json
from flask_sqlalchemy import SQLAlchemy

###Documentation#####

# https://www.themoviedb.org/documentation/api

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cursos.sqlite3"

db = SQLAlchemy(app)

#ORM -mapeamento de objeto relacional
class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Float)
    
    def __init__(self, nome, descricao, ch) -> None:
        self.nome = nome
        self.descricao =descricao
        self.ch = ch
        

@ app.route('/', methods = ['GET','POST'])
def inicio():
    url_principal = "https://api.themoviedb.org/3/discover/movie/?certification_country=US&certification=R&sort_by=vote_average.desc&api_key=352d670ec2702131d20c69d910d8b598"
    resposta = urllib.request.urlopen(url_principal)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template('index.html', inicio = jsondata['results'])

@app.route('/series', methods = ['GET', 'POST'])
def series():
    url_series = "https://api.themoviedb.org/3/discover/tv?with_people=108916,7467&sort_by=popularity.desc&api_key=352d670ec2702131d20c69d910d8b598"
    resposta = urllib.request.urlopen(url_series)
    dados = resposta.read()
    jsondata = json.loads(dados)
    return render_template('series.html', series = jsondata['results'])

# primeiro criamos uma variavel que receberá o caminho a ser consumido.
#utilizamos a urllib para fazer a requisição a API, e JSON para que o retorno seja convertido em JSON
#requisição via cliente feita ao servidor, com retorno de uma resposta com http response
#rota dinamica usamos o <>

@app.route('/filmes/<propriedade>')
def filmes(propriedade):
    if propriedade == 'populares':
        url = "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=352d670ec2702131d20c69d910d8b598"
    elif propriedade == 'kids':
        url = 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=352d670ec2702131d20c69d910d8b598'
    elif propriedade == 'filmes_2010':
        url = 'https://api.themoviedb.org/3/discover/movie?/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=352d670ec2702131d20c69d910d8b598'
    elif propriedade == 'drama':
        url = 'https://api.themoviedb.org/3/discover/movie?/discover/movie?with_genres=18&primary_release_year=2014.desc&api_key=352d670ec2702131d20c69d910d8b598'
        
    resposta = urllib.request.urlopen(url)
    #metodo read serve para que leia a resposta do http response
    dados = resposta.read()
    #metodo loads ele irá carregar os dados chamados pelo http response e transforma-lo em json
    jsondata = json.loads(dados)
    return render_template("filmes.html", filmes = jsondata['results'])
    
if __name__ == "__main__":
    app.run(debug=True)

