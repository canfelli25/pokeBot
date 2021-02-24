import os, logging
from flask import Flask, abort, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import User
from modul.poke import PokeAPI, Pokemon

poke_api = PokeAPI()

@app.route('/pokemon/<name_or_id>', methods=['GET'])
def get_pokemon_info(name_or_id):
    pokemon = poke_api.get_info_pokemon(name_or_id)

    if pokemon is None:
        abort(404, description="Resource not found")

    return pokemon.to_dict()

@app.route('/register', methods=['POST'])
def register_user():
    name = request.form.get('name')
    user_id = request.form.get('user_id')

    user = User.query.get(user_id)

    if user is None:
        user = User(name=name, telegram_user_id=user_id)
        db.session.add(user)
        db.session.commit()

    return {
        name: user.name,
        user_id: user.telegram_user_id
    }

if __name__ == '__main__':
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)

    app.run()