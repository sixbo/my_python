#encoding:utf-8
#从flask这个框架中导入flask这个类
from flask import Flask
#初始化一个flask对象
#flask（）
#需要传递一个参数——name——
#1.方便flask框架寻找资源
#2.方便flask插件比如 flask-sqlalchemy出现错误的时候，好去寻找问题所在的位置

app = Flask(__name__)

#app.route 一个装饰器
#@开头，并在函数的上面说明是装饰器
#这个装饰器的作用，是做一个url与视图函数的映射
#127.0.0.1:5000/去请求hello_workd这个函数，然后将结果返回给浏览器
@app.route('/')
def hello_world():
    return '我是第一个Python  flask程序'

#如果当前这个文件事做为入口程序运行，那么就执行app,run()
if __name__ == '__main__':
    #app.run()
    #启动一个应用服务器，来接受用户的请求
    #while True:
    # listen监听。
    app.run()
