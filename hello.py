#-*- coding:utf-8 -*-
#初始化
from flask import Flask,render_template
from  flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager



app = Flask(__name__)

#路由器和视图函数
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#run方法启动flask集成开发web服务器
if __name__ == "__main__":
    app.run(debug=True)