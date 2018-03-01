#encoding:utf-8
from flask import Flask
#导入配置文件
import config

app = Flask(__name__)
#引入配置文件
app.config.from_object(config)


@app.route('/')
def hello_world():
    return 'Hello World!公共够个带到公司'


if __name__ == '__main__':
    #debug=True debug模式，在app.run中传入一个关键参数debug app.run(debug=True)，就设置了debug模式。
    #debug的两大优点：
    #1.当程序出现问题时，可以在页面看到错误的位置
    #2.在修改了程序的文件，程序会自动加载不需要手动再次重启服务器
    app.run()
