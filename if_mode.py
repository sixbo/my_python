#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/<is_login>/')
def index(is_login):
    if is_login=='1':
        user={
            'username':u'刘波',
            'age':18
        }
        return render_template('index2.html',user=user)
    else:
        return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
