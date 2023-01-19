from app.extensions import ma

class ProductSchema(ma.Schema):
    nome = ma.String(required = True)
    id = ma.Integer(dump_only = True)
    tipo = ma.String(required = True)
    preco = ma.Float(required = True)
    tamanho = ma.String(required = True)
    quantidade = ma.Integer(required = True)