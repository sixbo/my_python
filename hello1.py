#-*- coding:utf-8 -*-
#初始化
from flask import Flask

app = Flask(__name__)

#路由器和视图函数，是使用程序实例提供的 app.route 修饰器，把修
#饰的函数注册为路由。下面的例子说明了如何使用这个修饰器声明路由
@app.route("/")
def index():
    return "<h1>hello world</h1>"
#动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>hello,%s!</h1>'% name

#run方法启动flask集成开发web服务器
if __name__ == '__main__':
    app.run(debug=True)