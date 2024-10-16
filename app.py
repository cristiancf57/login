from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Datos de ejemplo para usuarios
users = {
    "admin": "admin",
    "cristian": "usuario"
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Verificar si las credenciales son correctas
        if username in users and users[username] == password:
            session['username'] = username 
            return redirect(url_for('welcome'))
        else:
            flash('Nombre de usuario o contraseña incorrectos')

    return render_template('login.html')

@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/vaciar')
def vaciar():
    session.pop('username', None) 
    flash('Has cerrado sesión correctamente')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)