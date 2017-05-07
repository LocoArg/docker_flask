from flask import Flask, render_template
from flask_mongoengine import MongoEngine


db = MongoEngine()
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] ={
    'db': 'prueba',
    'host':'172.20.0.2',
    'port': 27017
}

#mongo = MongoEngine(app)
db.init_app(app)

class flask(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)  

@app.route('/crear')
def add():
    flask(email='nuevo@hotmail.com',first_name='German',last_name='Rodriguez').save()
    return 'Se creo el usuario'



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
