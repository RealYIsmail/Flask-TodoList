from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Secret Key"

## possibly error in URI
app.config['SQLALCHEMY DATABASE_URI'] = 'mysql://root:''@localhost/todoflaskdb'
app.config['SQLALCHEMY TRACK MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(100))

    def __init__(self, task):
        self.task = task


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
