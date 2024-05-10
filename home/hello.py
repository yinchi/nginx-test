from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''\
<h1>Hello, Worlds! (Homepage)</h1>
<ul>
    <li><a href='/app1'>App 1</a></li>
    <li><a href='/app2'>App 2</a></li>
</ul>
'''
