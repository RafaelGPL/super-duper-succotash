from flask import (
    Flask,
    request
)

from datetime import datetime

from app.database import user

app = Flask(__name__)
VERSION = "1.0.0"


@app.get("/version")
def get_version():
    out = {
        "server_time": datetime.now().strftime("%F %H:%M:%S"),
        "version": VERSION
    }
    return out

@app.get("/users/")
def get_all_users():
    user_list = user.scan()
    resp = {
        "status": "ok",
        "message": "success",
        "users": user_list
    }
    return resp

@app.get("/users/<int:pk>/")
def get_user_by_id(pk):
    target_user = user.select_by_id(pk)
    resp = {
        "status": "ok",
        "message": "success",
    }
    if target_user:                     # If "target_user" is not empty
        resp["user"] = target_user
        return resp                     # Flask will return an HTTP status code of 200 by default.
    else:
        resp["status"] = "error"
        resp["message"] = "User not found"
        return resp, 404                # We can explicitly set a different status code like this.

@app.post("/users/")
def create_user():
    user_data = request.json            # request is a Flask context object
    user.insert(user_data)
    return "", 204                      # No content status code; The operation was succesful but there is
                                        # no content to display or return.

@app.put("/users/<int:pk>/")
def update_user(pk):
    user_data = request.json
    user.update(pk, user_data)
    return "", 204

@app.delete("/users/<int:pk>/")
def deactivate_user(pk):
    user.deactivate(pk)         # soft delete
    return "", 204
