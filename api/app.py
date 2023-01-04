from flask import Flask
from flask_restful import Api
from api.config import Config
from api.database.database import init_app
from api.resources.Todo import Todo
from dotenv import load_dotenv

def create_app():
    

    #initializing app.
    app = Flask(__name__)
    app.config.from_object(Config)  
    init_app(app)
    load_dotenv()
    api = Api(app)


    @app.route("/")
    def index():
        return "Flask resftul API."

    #initializing the api framework.


    #resources.
    api.add_resource(Todo,"/todo/<todo_id>","/todo")


    return app 