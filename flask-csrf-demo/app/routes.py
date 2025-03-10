from flask import session, redirect, url_for, request, render_template
from app.models import get_db

def register_routes(app):
    @app.route('/')
    def home():
        if 'username' in session:
            return redirect(url_for('dashboard'))
        return redirect(url_for('login'))

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')
            db = get_db(app)
            user = db.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password)).fetchone()
            if user:
                session['username'] = user['username']
                session['email'] = user['email']
                return redirect(url_for('dashboard'))
            return "Invalid credentials!"
        return '''
            <form method="POST">
                <input type="text" name="username" placeholder="Username" required>
                <input type="password" name="password" placeholder="Password" required>
                <button type="submit">Login</button>
            </form>
        '''

    @app.route('/dashboard')
    def dashboard():
        if 'username' not in session:
            return redirect(url_for('login'))
        return render_template('dashboard.html', email=session.get('email', ''))

    @app.route('/update-email', methods=['POST'])
    def update_email():
        if 'username' not in session:
            return redirect(url_for('login'))
        new_email = request.form['new_email']
        db = get_db(app)
        db.execute('UPDATE users SET email = ? WHERE username = ?', (new_email, session['username']))
        db.commit()
        session['email'] = new_email
        return redirect(url_for('dashboard'))

    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('login'))