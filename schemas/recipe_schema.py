from marshmallow import Schema, fields

class RecipeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    ingredients = fields.Str(required=True)
    instructions = fields.Str(required=True)
    cooking_time = fields.Int(required=True)
    dietary_restriction = fields.Str(required=True)