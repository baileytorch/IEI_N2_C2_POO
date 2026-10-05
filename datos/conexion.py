from decouple import config
from peewee import MySQLDatabase

def conectar():
    database = MySQLDatabase(config('db'), **{
    'charset': 'utf8mb4', 
    'host': config('host'), 
    'port': config('port',cast=int), 
    'user': config('user'), 
    'password': config('password')})
    return database