from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'C:\Users\NALBERTH1\To-Do-List\database.db'
db = SQLAlchemy

@app.route("/")

def home(db):
    return "Olá, Flask!"

if __name__ == "__main__":
    app.run(debug=True)