
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/demo_1'
app.secret_key = 'many random bytes'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash('User created successfully', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('create_user'))
    return render_template('create_user.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_user(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        try:
            user.name = request.form['name']
            user.email = request.form['email']
            db.session.commit()
            flash('User updated successfully', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
            return redirect(url_for('update_user', id=id))
    return render_template('update_user.html', user=user)

@app.route('/delete/<int:id>', methods=['GET'])
def delete_user(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully', 'success')
    except Exception as e:
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
