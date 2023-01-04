
from os import getenv


"""
The database credentials
should be created at a .env file and pass here.
"""

class Config(object):
    

    #create a secret key and stored here.
    SECRET_KEY = getenv("SECRET_KEY")


    
    #Database Credentials
    DB_NAME = getenv("DB_NAME")
    DB_USER = getenv("DB_USER")
    DB_PASSWORD = getenv("DB_PASSWORD")
    DB_HOST = getenv("DB_HOST")


    #setting the database engine.
    #SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"