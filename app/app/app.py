from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cleylogs = False



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
    return redirect('dash')


@app.route('/dash', methods=[ 'POST'])
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


if __name__ == '__main__':
    app.run(debug=True)