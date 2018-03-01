#encoding:utf-8
from flask import Flask,render_template


app = Flask(__name__)


@app.route('/')
def index():
    class Person(object):
        name=u'刘波'
        age=19
    p=Person()
    context={
        'username':u'刘波',
        'gender':u'男',
        'age':19,
        'Person':p,
        'websites':{
            'baidu':'www.baidu.com',
            'google':'www.google.com'
        }




    }
    return  render_template('index1.html',**context)


if __name__ == '__main__':
    app.run()