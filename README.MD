<h1>Recipe API</h1>
<p>A simple CRUD (Create, Read, Update, Delete) API for managing recipes, built with Flask and SQLAlchemy.</p>

<h2>Features</h2>
<ul>
  <li>Create, read, update, and delete recipes</li>
  <li>Recipe details include name, ingredients, instructions, cooking time, and dietary restrictions</li>
  <li>RESTful API for interacting with recipes</li>
</ul>

<h2>Getting Started</h2>
<ol>
  <li>Clone the repository: <code>git clone https://github.com/renatograsso10/recipe_api.git</code></li>
  <li>Install dependencies: <code>pip install -r requirements.txt</code></li>
  <li>Create a SQLite database: <code>sqlite3 recipe.db</code></li>
  <li>Run the application: <code>python app.py</code></li>
  <li>Open a web browser and navigate to <a href="http://localhost:5000">http://localhost:5000</a></li>
</ol>

<h2>API Endpoints</h2>
<ul>
  <li><code>GET /recipes</code>: Retrieve a list of all recipes</li>
  <li><code>GET /recipes/:id</code>: Retrieve a single recipe by ID</li>
  <li><code>POST /recipes</code>: Create a new recipe</li>
  <li><code>PUT /recipes/:id</code>: Update a recipe</li>
  <li><code>DELETE /recipes/:id</code>: Delete a recipe</li>
</ul>

<h2>Technologies Used</h2>
<ul>
  <li>Flask: A micro web framework for Python</li>
  <li>SQLAlchemy: A SQL toolkit for Python</li>
  <li>SQLite: A self-contained, file-based SQL database</li>
</ul>

<h2>License</h2>
<p>This project is licensed under the GNU General Public License version 3.0 (GPL-3.0). See <a href="LICENSE">LICENSE</a> for details.</p>

<h2>Contributing</h2>
<p>Contributions are welcome If you'd like to contribute to this project, please fork the repository and submit a pull request.</p>

<h2>Author</h2>
<p>Renato Grasso</p>

<h2>Repository</h2>
<p><a href="https://github.com/renatograsso10/recipe_api">https://github.com/renatograsso10/recipe_api</a></p>

<h2>Issues</h2>
<p>If you encounter any issues or have questions, please open an issue on the GitHub repository.</p>

<h2>Acknowledgments</h2>
<ul>
  <li><a href="https://flask.palletsprojects.com/">Flask</a></li>
  <li><a href="https://www.sqlalchemy.org/">SQLAlchemy</a></li>
  <li><a href="https://www.sqlite.org/">SQLite</a></li>
</ul>