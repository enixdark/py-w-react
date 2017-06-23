import os
from flask import Flask
from flask_script import Manager
from flask_debugtoolbar import DebugToolbarExtension
from flask_restful import Api


#
application = Flask(__name__)


application.config.from_pyfile('config/development.cfg')


from api.util_service import UtilService

# register for debugging
toolbar = DebugToolbarExtension(application)

# register script command
manager = Manager(application)

# wrap to api
api = Api(application)
api.add_resource(UtilService, '/parse')
