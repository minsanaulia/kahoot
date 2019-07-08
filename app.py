from flask import Flask, jsonify
from src.models.models import db
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
                                                     #username:password@host:port/db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:musafirakhirzaman@localhost:5432/kahoot'

db.init_app(app)

# todo: use blueprint router
from src.routes.usersRoutes import get_all_users
from src.routes.quizzesRoutes import get_all_quizzess
from src.routes.questionsRoutes import get_all_questions
from src.routes.optionsRoutes import get_all_options
from src.routes.gamesRoutes import get_all_games

@app.route('/')
def main():
    return 'tes koneksi'