from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

## possibly error in URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost:3307/todoflaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))

    def __init__(self, task):
        self.task = task


@app.route('/')
def index():
    all_data = Data.query.all()

    return render_template("index.html", listedtask = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        task = request.form['task']

        my_data = Data(task)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))

@app.route('/edit', methods = ['GET', 'POST'])
def edit():

    if request.method == 'POST':
        my_data = Data.query.get(request.form.get('id'))
        my_data.task = request.form['task']

        db.session.commit()
        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect (url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
