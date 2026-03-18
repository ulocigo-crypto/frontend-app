import logging
import os
import uuid

from flask import current_app
from werkzeug.utils import secure_filename

def generate_uuid():
    return str(uuid.uuid4())

def get_logger():
    logger = logging.getLogger('frontend-app')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    return logger

def get_config(key, default=None):
    return current_app.config.get(key, default)

def is_safe_filename(filename):
    return secure_filename(filename)

def is_allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']

def get_upload_folder():
    return os.path.join(current_app.root_path, current_app.config['UPLOAD_FOLDER'])

def get_temp_folder():
    return os.path.join(current_app.root_path, current_app.config['TEMP_FOLDER'])