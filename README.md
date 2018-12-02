# test-flask

ref: [samurai python flask](https://www.sejuku.net/blog/55507)

OS: Windows7
python: Python 3.6.5

## Installation

cmd:
~~~
# py -m pip install Flask
~~~

## Hello world

hello.py
~~~
"""Test fdlask."""
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    """Hello world."""
    hello = "Hello world"
    return hello

if __name__ == "__main__":
    app.run()

~~~

cmd
~~~
# py hello.py
~~~

[Show page for Hello world of flask.](http://127.0.0.1:5000/)

## Apply HTML template

hello.py
~~~
@app.route('/')
def hello():
    """Hello world."""
    html = render_template('index.html')
    return html

~~~

templates/index.html
~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>HELLO</title>
</head>
<body>
    <p>Sayhello</p>
</body>
</html>
~~~

## Use variable

hello.py
~~~
@app.route('/')
def hello():
    """Hello world."""
    html = render_template('index.html', text='text message')
    return html

~~~

templates/index.html
~~~
<p>{{text}}</p>
~~~

## Use static file

templates/index.html
~~~
<link rel="stylesheet" href="/static/style.css">
~~~

static/style.css
~~~
.static {
    color: #ff0000;
}
~~~
