from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/affine_cipher/')
def affine_cipher():
    return render_template('affine_cipher.html')

if __name__ == '__main__':
    app.run(debug=True)