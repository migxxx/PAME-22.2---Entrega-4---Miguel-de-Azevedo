from flask import request
from flask.views import MethodView

from .models import my_products as products

from .schemas import ProductSchema

def getLastID():
    lastProduct = products[-1]
    return lastProduct["id"]


class ProductController(MethodView):
    def get(self):
        schema = ProductSchema()
        return schema.dump(products, many = True), 200


class AdminController(MethodView):
    def post(self):
        schema = ProductSchema()
        data = request.json

        data["id"] = getLastID() + 1

        try:
            product = schema.dump(data)
            products.append(product)
        except:
            print("Erro")
            return {}, 400

        return product, 201

    def get(self):
        schema = ProductSchema()
        return schema.dump(products, many = True), 200


class FilterProductType(MethodView):
    def get(self,tipo):
        schema = ProductSchema()

        productsList = []
        for product in products:
            if product["tipo"] == tipo:
                productsList.append(product)
        if len(productsList) > 0:
            return schema.dump(productsList, many=True), 200
        return {}, 400

class UserProductDetails(MethodView):
    def get(self,id):
        schema = ProductSchema()

        for product in products:
            if product["id"] == id:
                return schema.dump(product), 200
        return {}, 404

class BuyProducts(MethodView):
    def patch(self, id):
        schema = ProductSchema()

        productIndex = -1

        for product in products:
            if product["id"] == id:
                productIndex = products.index(product)
        if productIndex == -1:
            return {}, 404

        product = products[productIndex]

        newQtd = {}
        newQtd["nome"] = product["nome"]
        newQtd["id"] = product["id"]
        newQtd["tipo"] = product["tipo"]
        newQtd["preco"] = product["preco"]
        newQtd["tamanho"] = product["tamanho"]
        newQtd["quantidade"] = product["quantidade"] - 1

        if newQtd["quantidade"] == 0:
            for product in products:
                if product["id"] == id:
                    products.remove(product)
                    return {}, 204

        produto = schema.dump(newQtd)
        products[productIndex] = produto

        return produto, 200


class AdminProductDetails(MethodView):
    def put(self,id):
        schema = ProductSchema()
        data = request.json

        productIndex = -1

        for product in products:
            if product["id"] == id:
                productIndex = products.index(product)
        if productIndex == -1:
            return {}, 404

        data["id"] = id
        newProduct = schema.dump(data)
        products[productIndex] = newProduct
        return newProduct, 201

    def patch(self,id):
        schema = ProductSchema()
        data = request.json

        productIndex = -1
        for product in products:
            if product["id"] == id:
                productIndex = products.index(product)
        if productIndex == -1:
            return {}, 404
        
        product = products[productIndex]

        nome = data.get("nome", product["nome"])
        tipo = data.get("tipo", product["tipo"])
        preco = data.get("preco", product["preco"])
        tamanho = data.get("tamanho", product["tamanho"])
        quantidade = data.get("quantidade", product["quantidade"])

        data["nome"] = nome
        data["id"] = id
        data["tipo"] = tipo
        data["preco"] = preco
        data["tamanho"] = tamanho
        data["quantidade"] = quantidade

        product = schema.dump(data)
        products[productIndex] = product

        return product, 201

    def delete(self, id):
        for product in products:
            if product["id"] == id:
                products.remove(product)
                return {}, 204
        return {}, 404