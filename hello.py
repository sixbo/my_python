#-*- coding:utf-8 -*-
#初始化
from flask import Flask,render_template
from  flask.ext.bootstrap import Bootstrap
from flask.ext.script import Manager
from flask.ext.moment import Moment
from datetime import datetime
from flask.ext.wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required


class NameForm(Form):
    name=StringField('What is your name?',validators=[Required()])
    submit=SubmitField('Submit')



app = Flask(__name__)
moment=Moment(app)
bootstrap=Bootstrap(app)
#路由器和视图函数
#@app.route("/")
#def index():
#    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

#自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

#@app.errorhandler(500)
#def internal_server_error(e):
  #  return render_template('500.html'),500

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500
#添加时间
@app.route('/')
def index():
    return render_template('index.html',current_time=datetime.utcnow())

#run方法启动flask集成开发web服务器
if __name__ == "__main__":
    app.run(debug=True)