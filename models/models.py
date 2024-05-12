from extensions import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(200), nullable=False)
    instructions = db.Column(db.String(200), nullable=False)
    cooking_time = db.Column(db.Integer, nullable=False)
    dietary_restriction = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'Recipe {self.name}'