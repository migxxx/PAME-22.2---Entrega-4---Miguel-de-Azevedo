from flask import Blueprint

from .controller import UserController, UserDetails, adminController, adminDetails

userAPI = Blueprint("userAPI", __name__)

userAPI.add_url_rule(                   # post,get usuario geral
    "/users",
    view_func= UserController.as_view("userController"),
    methods = ["POST", "GET"]
)

userAPI.add_url_rule(                   # post, get admin geral
    "/users/admin",
    view_func= adminController.as_view("adminController"),
    methods = ["POST","GET"]
)

userAPI.add_url_rule(                   # post,get, put, patch detalhes do user
    "/users/<int:id>",
    view_func= UserDetails.as_view("userDetails"),
    methods = ["GET","PUT","PATCH"]
)

userAPI.add_url_rule(                   # post,get, put, patch, delete detalhes do user
    "/users/admin/<int:id>",
    view_func= adminDetails.as_view("adminDetails"),
    methods = ["GET","PUT","PATCH","DELETE"]
)