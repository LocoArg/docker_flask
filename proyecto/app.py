from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from data import Articles
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_mongoengine import MongoEngine

app = Flask(__name__)

Articles = Articles()
db = MongoEngine()
app.config['MONGODB_SETTINGS'] ={
    'db': 'prueba',
    'host':'172.20.0.2',
    'port': 27017
}
db.init_app(app)

@app.route('/')
def index():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)
@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html', id=id)

class RegisterForm(Form):
    name = StringField('Name',[validators.Length(min=1,max=50)])
    username = StringField('Username',[validators.Length(min=4,max=25)])
    email = StringField('Email',[validators.Length(min=6,max=50)])
    password = PasswordField('Password',[
        validators.DataRequired(),
        validators.EqualTo('confirm',message='Password do not match')
    ])
    confirm = PasswordField('Confirmar Password')

class user(db.Document):
    name = db.StringField()
    username = db.StringField()
    email = db.StringField()
    password = db.StringField()



@app.route('/register', methods=['GET','POST'])
#crea los campos para registrar
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        username = form.username.data
        password = sha256_crypt.encrypt(str(form.password.data))
        usuario = user(name=name,username=username,email=email,password=password).save()
        flash('Estas Registrado y ya puedes usar el sitio','success')
        redirect(url_for('index'))
    return render_template('register.html',form=form)
if __name__ == '__main__':
    app.secret_key='secreto123'
    app.run(debug=True,host='0.0.0.0',port=5000)
