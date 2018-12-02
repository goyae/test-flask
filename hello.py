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
