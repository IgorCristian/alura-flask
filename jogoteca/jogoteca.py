from flask import Flask, render_template

class Produto:
    def __init__(self, nome, categoria, marca):
        self.nome = nome
        self.categoria = categoria
        self.marca = marca

app = Flask(__name__)

@app.route("/inicio")
def ola():
    produto1 = Produto('Builder Base', 'Gel', 'Unique Nail')
    produto2 = Produto('Monomer', 'Acrílico', 'Psiu')
    produto3 = Produto('Passo 5', 'Blindagem', 'Psiu')

    lista = [produto1, produto2, produto3]
    return render_template("lista.html", titulo="Unique Nail", produtos=lista)

app.run()