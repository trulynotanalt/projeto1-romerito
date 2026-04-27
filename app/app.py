from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "chave_secreta"

usuario = {}
cleylogs = False
pedidos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    global usuario, cleylogs

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')

        if not nome or not email or not senha or not telefone:
            flash("Preencha todos os campos")
            return redirect(url_for('cadastro'))

        usuario.update({
            "nome": nome,
            "email": email,
            "senha": senha,
            "telefone": telefone
        })

        cleylogs = True
        return redirect(url_for('criacao'))

    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    global cleylogs
    cleylogs = False
    return redirect(url_for('index'))

@app.route('/criacao')
def criacao():
    if not cleylogs:
        return redirect(url_for('cadastro'))
    return render_template('criacao.html', pedidos=pedidos)

@app.route('/base')
def base():
    if not cleylogs:
        return redirect(url_for('index'))
    return render_template('base.html')

@app.route('/criar', methods=['POST'])
def criar():
    global pedidos

    if not cleylogs:
        flash('Não tem usuario logado')
        return redirect(url_for('cadastro'))

    endereco = {
        'cidade': request.form['cidade'],
        'bairro': request.form['bairro'],
        'rua': request.form['rua'],
        'numero_casa': request.form['num_casa'],
    }

    pedido = {
        'id': len(pedidos),
        'nome': request.form['nome'],
        'comida': request.form['comida'],
        'quantidade': request.form['quantidade'],
        'tamanho' : request.form['tamanho'],
        'metodo_pagamento' : request.form['met_pagamento'],
        'valor': request.form['valor'],
        'endereco': endereco
    }

    pedidos.append(pedido)
    return redirect(url_for('criacao'))

@app.route('/pedidos')
def mostrar():
    buscar = request.args.get('nome')

    if buscar:
        lista = [p for p in pedidos if buscar.lower() in p['nome'].lower()]
    else:
        lista = pedidos

    return render_template('pedidos.html', pedidos=lista)

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    pedido = pedidos[id]

    if request.method == 'POST':
        pedido['nome'] = request.form['nome']
        pedido['comida'] = request.form['comida']
        pedido['quantidade'] = request.form['quantidade']
        pedido['valor'] = request.form['valor']
        pedido['endereco'] = {
            'cidade': request.form['cidade'],
            'bairro': request.form['bairro'],
            'rua': request.form['rua'],
            'numero_casa': request.form['num_casa']
        }
        return redirect(url_for('mostrar'))

    return render_template('editar.html', pedido=pedido)

@app.route('/deletar/<int:id>')
def deletar(id):
    if id < len(pedidos):
        pedidos.pop(id)
    return redirect(url_for('criacao'))

@app.route('/perfil')
def perfil():
    if not cleylogs:
        return redirect(url_for('cadastro'))
    return render_template('perfil.html', usuario=usuario)

if __name__ == '__main__':
    app.run(debug=True)