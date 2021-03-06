import os

from marshmallow import ValidationError

# import env

from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from flask_restful import Api

from resources.user import UserRegister, UserLogin, UserLogout, login_manager
from resources.confirmation import ConfirmationPage, Confirm
from resources.github_login import GithubLogin, GithubAuthorize
from resources.google_login import GoogleLogin, GoogleAuthorize
from resources.survey import Survey
from resources.map import Map
from resources.algorithm import Algorithms
from ma import ma
from oa import oauth
from db import mongo

# Settings
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
# For User Credentials:
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['JWT_SECRET_KEY'] = os.environ["JWT_SECRET_KEY"]
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['DEBUG'] = False
# For Suggested Questions:
app.config["MONGO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

api = Api(app)

Bootstrap(app)


# Login manager
login_manager.init_app(app)

# Register Resources
api.add_resource(Survey, '/')
api.add_resource(Map, '/map')

api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(Confirm, '/confirm')
api.add_resource(UserLogout, '/logout')
api.add_resource(ConfirmationPage, '/user_confirmation/<string:confirmation_id>')
api.add_resource(GithubLogin, '/login/github')
api.add_resource(GithubAuthorize, '/login/github/authorized', endpoint='github.authorize')
api.add_resource(GoogleLogin, '/login/google')
api.add_resource(GoogleAuthorize, '/login/google/authorized', endpoint='google.authorize')

api.add_resource(Algorithms, '/algorithms')



# Error Handlers
@app.errorhandler(404)
def error404(error):
    return render_template('404.html')


@app.errorhandler(500)
def error500(error):
    return render_template('500.html')


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(error):
    return jsonify(error.messages), 400


## APP INITIATION

if __name__ == '__main__':
    from db import db
    mongo.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    oauth.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    # app.run()

# Heroku
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
