from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Inventory model
class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

# Ensure the database is created within the application context
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    inventory = Inventory.query.all()
    return render_template('zadanie4.html', inventory=inventory)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        description = request.form['description']
        weight = float(request.form['weight'])
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        # Добавляем новый товар в базу данных
        new_item = Inventory(name=name, description=description, weight=weight, quantity=quantity, price=price)
        db.session.add(new_item)
        db.session.commit()

        # Перенаправляем на главную страницу
        return redirect(url_for('index'))
    return render_template('zadanie4additem.html')

if __name__ == '__main__':
    app.run(debug=True)
