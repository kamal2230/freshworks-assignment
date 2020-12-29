from flask import Flask,render_template,request,redirect,url_for,session, send_file
from werkzeug.utils import secure_filename
import json
from flask_pymongo import pymongo
from bson.json_util import dumps, loads
from pathlib import Path 

app = Flask(__name__)
CONNECTION_STRING = "mongodb+srv://kamal:mongodb2000@kflix.iwot1.mongodb.net/test_crd?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)

user_db = client['test_crd']['users']
db = client['test_crd']['crd']

@app.route("/", methods = ["POST", "GET"])
def index():
    return render_template("index.html")
    
@app.route("/create", methods = ["POST", "GET"])
def create():
    k = request.form['key']
    value = request.files['value']
    if value.filename.split('.')[1] == 'json':
        value.save(secure_filename(value.filename))
        f = open(value.filename,)
        data = json.load(f)
        fin_value = {"key": k, "value": data}
        db.insert_one(fin_value)

        return "Key created"

    return "Wrong file format"



if __name__ == "__main__":
    app.run(debug=True)