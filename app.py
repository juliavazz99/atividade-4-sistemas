from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, Flask !!"

@app.route('/versao')
def versao():
    versao = "1.1.0"
    return f"App v{versao}"

@app.route('/saudar/<nome>')
def saudar(nome):
    nome_formatado = nome.capitalize()
    return f"Olá, {nome_formatado}!", 200

@app.route('/quadrado/<int:n>')
def quadrado(n):
    resultado = n ** 2
    return f"{n}² = {resultado}", 200 

@app.route('/home')
def home():
    return redirect('/'), 302 

@app.route('/pagina')
def pagina():
    return render_template('pagina.html'), 200

@app.route('/buscar/<item>')
def buscar(item):
    itens = ['julia', 'marcos', 'ana', 'pedro', 'laura']
    item = item.lower()

    if item in itens:
        return f"'{item.capitalize()}' foi encontrado na lista!"
    else:
        return f"'{item.capitalize()}' não foi encontrado."
