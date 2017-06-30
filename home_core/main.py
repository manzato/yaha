from kivy.logger import Logger
from mongoengine import connect
from .models import Category, Light

def startup():
    Logger.info("Application: Starting...")
    connect('mydb')
