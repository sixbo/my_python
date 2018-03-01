#encoding:utf-8
from flask import Flask

app = Flask(__name__)

#参数的作用：可以在相同的url，但是指定不同的参数，来加载不同的数据。
#在flask怎么使用参数
#注意：参数要放在尖括号总监

@app.route('/user/<id>')
#注意：视图函数中需要放和url中参数同名的参数
def hello_world(id):
    return 'Hello World!%s'%id


if __name__ == '__main__':
    app.run(debug=True)
