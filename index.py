from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return 'hello_world'


if __name__ == '__main__':
    app.run()

    print(123)
