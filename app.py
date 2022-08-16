from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

## possibly error in URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/todoflaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))

    def __init__(self, task):
        self.task = task


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        task = request.form['task']

        my_data = Data(task)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
