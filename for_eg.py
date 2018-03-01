#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    user={
        'username':u'刘波',
        'age':18
    }
    websites=['baidu.com','google.com']
    return render_template('indexfor.html',user=user,websites=websites)

    book=[]




if __name__ == '__main__':
    app.run(debug=True)
#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    user={
        'username':u'刘波',
        'age':18
    }
    websites=['baidu.com','google.com']
    #return render_template('indexfor.html',user=user,websites=websites)

    books=[
        {
            'name':u'西游记',
            'author':u'吴承恩'
        },
        {
            'name':'红楼梦',
            'author':'曹雪芹'
        }

    ]


    return render_template('indexfor.html', user=user, websites=websites,books=books)

if __name__ == '__main__':
    app.run(debug=True)
