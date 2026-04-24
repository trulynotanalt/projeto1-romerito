from flask import Flask, render_template,request, redirect, url_for

app=Flask(__name__)

usuario= {}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():

    global usuario
    if usuario:
        return redirect(url_for('index'))
    
    if request.method == 'POST':

        email = request.form.get('email')
        senha = request.form.get('senha')
        telefone = request.form.get('telefone')

        if not email or not senha or not telefone:
            return redirect(url_for('cadastro'))
        
        
        usuario.update({"email": email, 
                        "senha": senha, 
                        "telefone": telefone})

        return redirect(url_for('index'))
    
    return render_template("cadastro.html")


@app.route("/perfil")
def perfil():
    global usuario
    if usuario:
        return redirect(url_for('index'))
    
    return render_template("perfil.html")

@app.route("/ciriaca")
def criacao():
    global usuario
    if usuario:
        return redirect(url_for('cadastro'))
    return render_template("criacao.html")


    


