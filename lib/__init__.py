# Author: Sakthi Santhosh
# Created on: 22/04/2023
from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

from lib.constants import LOG_FILE, SQLITE_DB_URI
from lib.log import Logger

app_handle = Flask(__name__)

app_handle.config["SQLALCHEMY_DATABASE_URI"] = SQLITE_DB_URI
app_handle.config["SECRET_KEY"] = str(uuid4())

db_handle = SQLAlchemy(app_handle)
socket_handle = SocketIO(app_handle)

log_handle = Logger(LOG_FILE).get_log_handle()

from lib.routes import devices, main, responders

log_handle.info("Flask app started running.")
