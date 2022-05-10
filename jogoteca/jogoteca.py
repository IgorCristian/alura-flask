from flask import Flask, render_template, request, redirect

class Produto:
    def __init__(self, nome, categoria, marca):
        self.nome = nome
        self.categoria = categoria
        self.marca = marca

produto1 = Produto('Builder Base', 'Gel', 'Unique Nail')
produto2 = Produto('Monomer', 'Acrílico', 'Psiu')
produto3 = Produto('Passo 5', 'Blindagem', 'Psiu')
lista = [produto1, produto2, produto3]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("lista.html", titulo="Unique Nail", produtos=lista)

@app.route("/novo")
def novo():
    return render_template("novo.html", titulo="Novo Produto")

@app.route("/criar", methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    marca = request.form['marca']
    produto = Produto(nome, categoria, marca)
    lista.append(produto)
    return redirect('/')

app.run(debug = True)