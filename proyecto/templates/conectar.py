from mongoengine import *

connect (db='prueba',host='172.20.0.2',port=27017)
db = connect('flask')
#db.drop_database('tumblelog') 


##################

#la clase hace referencia a la coleccion
class flask(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)  


##################

class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)    
    
##################

class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(flask)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))

    meta = {'allow_inheritance': True}

class TextPost(Post):
    content = StringField()

class ImagePost(Post):
    image_path = StringField()

class LinkPost(Post):
    link_url = StringField()
    
    
##################
    
    
    
ross = flask(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
ross['last_name'] = 'chaves'
print(ross.id)
ross.save()

