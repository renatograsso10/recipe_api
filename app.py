from flask import Flask
from extensions import db
from models.models import Recipe
from routes.recipe_routes import recipe_blueprint

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/test.db"
app.config["PROPAGATE_EXCEPTIONS"] = True

db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

app.register_blueprint(recipe_blueprint)

if __name__ == "__main__":
    app.run(debug=True, port=5000)