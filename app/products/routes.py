from flask import Blueprint
from .controller import *

productsAPI = Blueprint("productsAPI", __name__)

productsAPI.add_url_rule(
    "/products",
    view_func= ProductController.as_view("productsControllerUSER"),
    methods = ["GET"]
)

productsAPI.add_url_rule(
    "/products/admin",
    view_func= AdminController.as_view("productsControllerADMIN"),
    methods = ["POST","GET"]
)

productsAPI.add_url_rule(
    "/products/<int:id>",
    view_func= UserProductDetails.as_view("productsDetailsUSER"),
    methods = ["GET"]        
)

productsAPI.add_url_rule(
    "/products/<int:id>",
    view_func= BuyProducts.as_view("buyProducts"),
    methods = ["PATCH"]        
)

productsAPI.add_url_rule(
    "/products/<tipo>",
    view_func= FilterProductType.as_view("filterProducts"),
    methods = ["GET"]
)

productsAPI.add_url_rule(
    "/products/admin/<int:id>",
    view_func= AdminProductDetails.as_view("productDetailsADMIN"),
    methods = ["PUT","PATCH","DELETE"]
)

