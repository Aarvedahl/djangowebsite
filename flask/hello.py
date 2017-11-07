from flask import Flask, jsonify
from employee import Employee

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World! here is flask"

@app.route("/today")
def today():
    return "It is tuesday today"

@app.route("/json")
def test():
    employee = Employee('first name','last name')
    return employee.toJson()

@app.route("/list")
def list():
    return jsonify([1,2,3,4,5,6,7,8,9,10])

@app.route('/user/<username>')
def show_user_profile(username):
    return "User %s" %username

@app.route('/user/<int:user_id>')
def show_user_id(user_id):
    return 'User id is %d' % user_id


#export FLASK_APP=hello.py python -m flask run


