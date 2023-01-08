from flask_restful import Resource
from flask import request


class UserResource(Resource):

    def get(self):

        try:
            json = request.get_json()
            if "user" in json and "password" in json:
                return {"message":""}

        except Exception as e:
            return {"message":"JSON format invalid"},415

        