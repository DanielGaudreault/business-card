from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a secure secret key

# Dummy user database (replace with your actual database)
users = {'username': 'password'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            return render_template('register.html', error='Username already exists')
        users[username] = password
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users or users[username] != password:
            return render_template('login.html', error='Invalid username or password')
        session['username'] = username
        return redirect(url_for('profile'))
    return render_template('login.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'username' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']
        if users[session['username']] != current_password:
            return render_template('change_password.html', error='Current password is incorrect')
        if new_password != confirm_password:
            return render_template('change_password.html', error='New password and confirm password do not match')
        users[session['username']] = new_password
        return redirect(url_for('profile'))
    return render_template('change_password.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/profile')
def profile():
    if 'username' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', username=session['username'])

if __name__ == '__main__':
    app.run(debug=True)
