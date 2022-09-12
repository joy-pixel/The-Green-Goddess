from peewee import *
from os import path
connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection,"chrome_shop.db"))
#create the user table
class Users(Model):
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    class Meta:
        database = db
Users.create_table(fail_silently=True)
#create the requests table
class Requests(Model):
    content = CharField()
    class Meta:
        database = db
Requests.create_table(fail_silently=True)