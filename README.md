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
"""Test flask."""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Hello world."""
    html = render_template('index.html')
    return html

if __name__ == "__main__":
    app.run()

~~~

## Use variable

~~~
"""Test flask."""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Hello world."""
    html = render_template('index.html', text='text message')
    return html

if __name__ == "__main__":
    app.run()

~~~
