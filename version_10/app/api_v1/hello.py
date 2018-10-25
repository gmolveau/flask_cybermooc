# app/api_v1/hello.py

import os
from flask import (
    request, render_template
)
from werkzeug.utils import secure_filename
from . import root_blueprint
from .decorators import login_required, roles_required


@root_blueprint.route('/', methods=['GET'])
def index():
    return render_template("index.html")


@root_blueprint.route('/upload', methods=['POST'])
def upload_route():
    # myFile is the name of the key in the body of the request
    if 'myFile' in request.files:
        file = request.files['myFile']
        if file.filename != '':
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join("uploads", filename))
                return ('', 204)
    return ('', 400)


@root_blueprint.route('/need_login', methods=['GET'])
@login_required
def route_need_login(current_user):
    return "if you see this, that means your token is valid"


@root_blueprint.route('/admin', methods=['GET'])
@login_required
@roles_required('admin')
def route_admin_only(current_user):
    return "if you see this, that means you are an admin"
