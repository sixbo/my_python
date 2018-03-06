#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)

class Person(object):
    name=''
    age=0
class Student(Person):
    pass
@app.route('/')
def index():
    return render_template('index_block.html')
@app.route('/login')
def login():
    return render_template('block_login.html')

if __name__ == '__main__':
    app.run(debug=True)