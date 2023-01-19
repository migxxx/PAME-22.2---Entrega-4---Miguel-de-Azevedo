from app.extensions import ma

class UserSchema(ma.Schema):
    id = ma.Integer(dump_only = True)
    username = ma.String(required = True)
    tipo = ma.Integer(required = True)