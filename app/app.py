from flask import Flask, render_template, request, redirect

app = Flask(__name__)

cleylogs = False



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    global cleylogs
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')
    
    
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST' and usuario and senha :
        return render_template('login.html')
    
    if request.method == 'POST' and not usuario and not senha :
        return render_template('index.html')

    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)