import urllib.request, json

# primeiro criamos uma variavel que receberá o caminho a ser consumido.
#utilizamos a urllib para fazer a requisição a API, e JSON para que o retorno seja convertido em JSON
#requisição via cliente feita ao servidor, com retorno de uma resposta com http response

url = "https://api.hgbrasil.com/weather?woeid=455827"
resposta = urllib.request.urlopen(url)

#metodo read serve para que leia a resposta do http response
dados = resposta.read()
#metodo loads ele irá carregar os dados chamados pelo http response e transforma-lo em json
jsondata = json.loads(dados)

print(jsondata)