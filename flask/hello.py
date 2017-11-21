from flask import Flask, jsonify, json
from employee import Employee
from flask.ext.mysql import MySQL
import names
import MySQLdb as mdb


app = Flask(__name__)

# MySQL configurations
con = mdb.connect(host="localhost",user="joebob",
                  passwd="moonpie",db="thangs")

@app.route("/mysql")
def mysql():
    cur = con.cursor()
    cur.execute("SELECT * FROM Writers")

    rows = cur.fetchall()

    for row in rows:
        print row

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

@app.route("/jsonlist")
def jsonlist():
    list = []
    employee = Employee('Queenie','Santos')
    list.append(employee)
    employee = Employee("Alex", "Arvedahl")
    list.append(employee)
    return json.dumps([employee.__dict__ for employee in list])



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
