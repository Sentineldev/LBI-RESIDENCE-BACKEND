from flask_restful import Resource
from flask import request
from api.common.Classes.Todo import TodoModel


class Todo(Resource):

    #handles the get request
    def get(self):

        #checks if the url contains an ID param to filter the data.
        #if it doesn't it will not retrieve anything.
        if not "id" in request.args:
            return {"message":"Invalid field"},404
        result = TodoModel.getTodoById(request.args.get('id'))
        if result is None:
            return {"message":"resource not found"},404
        return result,200

    #handles the post request.
    def post(self):

        #gets the json data if it doesn't contain any json will return and invalid format message.
        #Also checks if the json contains both title and body to create the resource.
        try:
            json_data = request.get_json()
            if "title" in json_data and "body" in json_data:
                TodoModel.createTodo(json_data['title'],json_data['body'])
                return {"message":"Resource created successfully"},201
            return {"message":"Missing title or body fields."},422
        except Exception as e:
            return {"message":"JSON format invalid"},415

    #handle the delete request.
    def delete(self,todo_id):

        #check if there's any todo with the given ID.
        #if it does it will deleted.
        #else it will just sent 404 code.
        todo = TodoModel.getTodoById(todo_id)
        if todo is not None:
            TodoModel.deleteTodo(todo_id)
            return {"message":"Resource deleted"},200
        return {"message":"Resource not found"},404


    #handles the put request.
    def put(self,todo_id):
        #gets the json data if it doesn't contain any json will return and invalid format message.
        #checks if there's any todo with the given ID.
        #also checks if the JSON data contais both title and body.
        #then it will update the todo with the given data.
        
        try:
            json_data = request.get_json()
            todo = TodoModel.getTodoById(todo_id)
            if not ("title" in json_data and "body" in json_data):
                return {"message":"Missing fields"},422
            elif todo is None:
                return {"message":"Resource not found"},404
            else:
                TodoModel.updateTodo(todo_id,json_data['title'],json_data['body'])
                return {"message":"Resource updated successfully"},200
                
        except Exception as e:
            return {"message":"JSON format invalid"},415

