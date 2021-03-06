from flask import Flask, render_template, request, redirect, session, flash, url_for

class Produto:
    def __init__(self, nome, categoria, marca):
        self.nome = nome
        self.categoria = categoria
        self.marca = marca

produto1 = Produto('Builder Base', 'Gel', 'Unique Nail')
produto2 = Produto('Monomer', 'Acrílico', 'Psiu')
produto3 = Produto('Passo 5', 'Blindagem', 'Psiu')
lista = [produto1, produto2, produto3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("IgorCristian", "Igão", "uniqueadmin")
usuario2 = Usuario("Camila", "Mila", "paozinho")
usuario3 = Usuario("Guilherme", "Gui", "gui123")

usuarios = {usuario1.nickname : usuario1,
            usuario2.nickname : usuario2,
            usuario3.nickname : usuario3}

app = Flask(__name__)
app.secret_key = 'adminnunique'

@app.route("/")
def index():
    return render_template("lista.html", titulo="Unique Nail", produtos=lista)

# Renderiza página de formulário para adição de produtos caso o usuário esteja logado.
@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template("novo.html", titulo="Novo Produto")
# ----------------------------------------------------------------------

@app.route("/criar", methods = ['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    marca = request.form['marca']
    produto = Produto(nome, categoria, marca)
    lista.append(produto)
    return redirect(url_for('index'))

# Renderiza Formulário na página web
@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', titulo="Faça seu login", proxima=proxima)
# ---------------------------------------------------------------------

@app.route('/autenticar', methods = ['POST',])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nome + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuario não logado, tente novamente.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect(url_for('index'))

app.run(debug = True)