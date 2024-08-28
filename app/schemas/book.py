from marshmallow import Schema, fields

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    date_publish = fields.DateTime(dump_only=True)
    author = fields.Str(required=True)
    rate = fields.Float(required=True)
    image = fields.Str(required=False)
