from flask import request
from flask.views import MethodView

from .models import my_users as users

from .schemas import UserSchema

def getLastID():
    lastUser = users[-1]
    return lastUser["id"]

class UserController(MethodView):
    def post(self): 
        schema = UserSchema()
        data = request.json

        data["id"] = getLastID() + 1
        data["tipo"] = 1                # coloca o tipo sempre como 1, pois e um cliente \
                                        # criando um novo usuario

        try:
            user = schema.dump(data)
            users.append(user)
    
        except:
            print("Erro")
            return {}, 400

        return user, 201

    def get(self):
        schema = UserSchema()
        return schema.dump(users, many = True), 200


class adminController(UserController, MethodView):
    def post(self): 
        schema = UserSchema()
        data = request.json

        data["id"] = getLastID() + 1            # admin, nao possui o filtro de tipo

        try:
            user = schema.dump(data)
            users.append(user)
    
        except:
            print("Erro")
            return {}, 400

        return user, 201


class UserDetails(MethodView):
    def get(self,id):
        schema = UserSchema()

        for user in users:
            if user["id"] == id:
                return schema.dump(user), 200
        return {}, 404

    def put(self, id):
        schema = UserSchema()
        data = request.json

        userIndex = -1

        for user in users:
            if user["id"] == id:
                userIndex = users.index(user)
        if userIndex == -1:
            return {}, 404

        data["id"] = id
        data["tipo"] = 1                # mantem o user como um cliente
        newUser = schema.dump(data)
        users[userIndex] = newUser
        return newUser, 201

    def patch(self,id):
        schema = UserSchema()
        data = request.json

        userIndex = -1
        for user in users:
            if user["id"] == id:
                userIndex = users.index(user)
        if userIndex == -1:
            return {}, 404
        
        user = users[userIndex]

        username = data.get("username", user["username"])

        data["username"] = username
        data["tipo"] = 1                # mantem o user como um cliente
        data["id"] = id

        user = schema.dump(data)
        users[userIndex] = user

        return user, 201

class adminDetails(UserDetails, MethodView):
    def put(self, id):
        schema = UserSchema()
        data = request.json

        userIndex = -1

        for user in users:
            if user["id"] == id:
                userIndex = users.index(user)
        if userIndex == -1:
            return {}, 404

        data["id"] = id               # admin, nao possui o filtro de tipo
        newUser = schema.dump(data)
        users[userIndex] = newUser
        return newUser, 201

    def patch(self,id):
        schema = UserSchema()
        data = request.json

        userIndex = -1
        for user in users:
            if user["id"] == id:
                userIndex = users.index(user)
        if userIndex == -1:
            return {}, 404
        
        user = users[userIndex]

        username = data.get("username", user["username"])
        tipo = data.get("tipo", user["tipo"])

        data["username"] = username
        data["tipo"] = tipo             # admin, nao possui o filtro de tipo
        data["id"] = id

        user = schema.dump(data)
        users[userIndex] = user

        return user, 201

    def delete(self, id):
        for user in users:
            if user["id"] == id:
                users.remove(user)
                return {}, 204
        return {}, 404