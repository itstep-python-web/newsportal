
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home/index.html', data={
        'title': 'Главная'
    })


if __name__ == '__main__':
    app.run(debug=True)
