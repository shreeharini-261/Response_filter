from marshmallow import Schema, fields

class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Decimal(as_string=True)
    cost_price = fields.Decimal(as_string=True)
    category = fields.Str()
    created_at = fields.DateTime()

class PublicProductSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    #price = fields.Decimal(as_string=True)
    category = fields.Str()
    created_at = fields.DateTime()

class PrivateProductSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Decimal(as_string=True)
    cost_price = fields.Decimal(as_string=True)
    category = fields.Str()
    created_at = fields.DateTime()