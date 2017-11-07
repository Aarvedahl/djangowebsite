from flask import Flask, jsonify
from employee import Employee

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World! here is flask"

@app.route("/tuesday")
def tuesday():
    return "It is tuesday today"

@app.route("/json")
def test():
    employee = Employee('first name','last name')
    return employee.toJson()

@app.route("/list")
def list():
    return jsonify([1,2,3,4,5,6,7,8,9,10])

#export FLASK_APP=hello.py python -m flask run


