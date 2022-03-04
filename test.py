from flask_sqlalchemy import SQLAlchemy
from flask import Flask , abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def home():
    return '<h1> Access granted </h1>'

@app.route('/d')
def denied():
    return abort(410,"Mooditu poda veliya")

if __name__ == "__main__":
    app.run(debug=True)
