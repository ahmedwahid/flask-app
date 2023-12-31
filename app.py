from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "123"

# Dummy user credentials for example purposes
users = {
    "admin": "password123",
    "user1": "password456"
}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect('/dashboard')
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')

@app.route('/dashboard', methods=['GET'])
def dashboard():
    if 'username' in session:
        return render_template('dashboard.html')
    else:
        return redirect('/login')

@app.route('/logout', methods=['GET'])
def logout():
    session.pop('username', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
