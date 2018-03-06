#encoding:utf-8
from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def index():
    comment = [{'user': 'sjjsjdjk@132.com', 'content': 'jjjdjdjjdsdhjskhjkshfjksfhsjkfhds'},
        {'user': 'dffssfds@132.com', 'content': 'jjjdjdjjdsdhjfdsfsfsdfsdfsfsskhjkshfjksfhsjkfhds'}]
    return  render_template('filter_index.html',avatar='https://pic.cnblogs.com/face/981898/20170928195606.png',comment=comment)

@app.route('/1/')
def index1():
    comment=[
        {
            'user':'sjjsjdjk@132.com',
            'content':'jjjdjdjjdsdhjskhjkshfjksfhsjkfhds'
        },
        {   'user': 'dffssfds@132.com',
            'content':'jjjdjdjjdsdhjfdsfsfsdfsdfsfsskhjkshfjksfhsjkfhds'
        }
    ]
    return  render_template('filter_index.html',comment=comment)

if __name__ == '__main__':
    app.run(debug=True)