from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    secret = "[letmein]+"
    app.secret_key = secret
    app.run(host='192.168.146.134', port=8084, debug=True)


# , template_folder='templates'
