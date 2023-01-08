from flask_restful import Resource
from flask import request,make_response
from api.common.Classes.User import User
from jwt import encode,decode


    
def generateJWT(payload):
    return encode(payload,"secret",algorithm="HS256")


def validateJWT(jwt):
    return decode(jwt,"secret",algorithms=["HS256"])

class Auth(Resource):
    def get(self):
        try:
            token = request.headers['Authorization'].split(" ")[1]
            jwt = validateJWT(token)
            user = User.getUserById(jwt['user_id'])
            if user is not None:
                user['created_at'] = str(user['created_at'])
                return user,200
            return {"message":"User doesn't exists"},404
                
        except Exception as e:
            print(e)
            return {"message":"JSON format invalid"},400

    def post(self):
        try:
            data = request.get_json()
            if not "username" in data:
                return {"message":"Username field missing"},415
            elif not "password" in data:
                return {"message":"Password field missing"},415
            else:
                username = data['username']
                password = data['password']

                user  = User.authenticateUser(username,password)
                if user is not None:
                    token = generateJWT(user)
                    return {"message":"","token":token},200
                return {"message":"Invalid credentials"},401
        except Exception as e:
            return {"message":"JSON format invalid"},400