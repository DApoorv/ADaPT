"""
Created by Rachita Mishra
Last updated on 25 August 2021
Project encoding type: UTF-8
"""


from flask import Flask, current_app
from flask_cors import CORS

from user import user
# from user.helpers.login_manager import login_manager
from db import dbf_obj
from configuration import default
from execution import execution
from flask_migrate import Migrate
from utils.background_sched import BackgroundScheduler
from utils.bg_tasks import status_check, val_status_check


# initialising the flask app
app = Flask(__name__)

# CORS(app, resources={r"/*": {"origins": "http://localhost:3000,https://tesseract-stg.eng.vmware.com,https://tesseract.eng.vmware.com/"}})

# @app.after_request
# def after_request(response):
#   response.headers.add('Access-Control-Allow-Origin', '*')
#   response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
#   response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#   return response

# loading configs to the flask app from the pyfile
app.config.from_pyfile('config.py')
# registering blueprints
app.register_blueprint(user)
app.register_blueprint(default)
app.register_blueprint(execution)

# getting database object; sqlalchemy instance
db = dbf_obj.get_dbase()
# registering sqlalchemy instance with the app to run migrates
db.init_app(app)
# creating migrate object that registers the app and the db instance
# which will be helpful in creating migrations.
migrate = Migrate(app, db)

#login_manager.init_app(app)

sched = BackgroundScheduler(daemon=True)
# sched.add_job(status_check, 'interval', seconds=10, args=[app])
# sched.add_job(val_status_check, 'interval', seconds=30, args=[app])
sched.start(app)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=34569)
