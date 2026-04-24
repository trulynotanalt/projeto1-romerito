from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

cleylogs = False


pedidos = []

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login', methods=['POST'])
def login():
    global cleylogs
    cleylogs = request.form.get('usuario')
    return redirect(url_for('dash'))


@app.route('/dash')
def dash():
    if not cleylogs:
        return render_template('cadastro.html')
    return render_template('dash.html')

# @app.route('/pedido')
# def pedido():
#     valor = request.args.get('valor')
#     cidade = request.args.get('usuario')
#     bairro = request.args.get('usuario')
#     rua = request.args.get('usuario')
#     num_casa = request.args.get('usuario')
#     num_tel = request.args.get('num_tel')
#     num_ped = request.args.get('num_ped')
#     nome = request.args.get('nome')
#     nome_ped = request.args.get('nome')

#     return f''

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if not cleylogs:
        flash('Não tem usuario logado')
        return redirect(url_for('cadastro'))
    if request.method == 'POST':
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
            'valor': request.form['valor'],
            'endereco': [endereco]
        }
        pedidos.append(pedido)
        return redirect(url_for('mostrar'))
    
    # return render_template('rota pros pedidos')

@app.route('/pedidos') # tem q juntar ao de rotas
def mostrar():
    buscar = request.args.get('nome')
    
    if buscar:
        lista = []
        for p in pedidos:
            if buscar.lower() in p['nome'].lower():
                lista.append(p)
    else:
        lista = pedidos
    # return render_template('pedidos.html', pedidos=lista) esperar a rota e as paginas-web

@app.route('/editar/<int:id>', methods = ['GET','POST'])
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
    return redirect(url_for('pedido', pedido=pedido))

@app.route('/deletar/<int:id>')
def deletar(id):
    pedidos.pop(id)
    return redirect(url_for('mostrar'))
if __name__ == '__main__':
    app.run(debug=True)