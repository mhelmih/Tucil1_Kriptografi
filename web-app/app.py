from flask import Flask, render_template, url_for, request, flash, redirect, send_file
from werkzeug.datastructures import ImmutableMultiDict
import os
import affine_handler, playfair_handler, hill_handler, vigenere_handler

UPLOAD_FOLDER = './uploads' 
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<path>')
def download_file(path):
    return send_file(path, as_attachment=True)

@app.route('/vigenere_cipher/', methods=['GET','POST'])
def vigenere_cipher():
    if request.method == 'GET':
        return vigenere_handler.vigenere_get(app)
    if request.method == 'POST':
        return vigenere_handler.vigenere_post(app)
    return render_template('vigenere_cipher.html')

@app.route('/playfair_cipher/', methods=['GET','POST'])
def playfair_cipher():
    if request.method == 'GET':
        return playfair_handler.playfair_get(app)
    if request.method == 'POST':
        return playfair_handler.playfair_post(app)
    return render_template('playfair_cipher.html')
        

@app.route('/affine_cipher/', methods=['GET','POST'])
def affine_cipher():
    if request.method == 'GET':
        return affine_handler.affine_get(app)
    if request.method == 'POST':
        return affine_handler.affine_post(app)
    return render_template('affine_cipher.html')

@app.route('/hill_cipher/', methods=['GET','POST'])
def hill_cipher():
    if request.method == 'GET':
        return hill_handler.hill_get(app)
    if request.method == 'POST':
        return hill_handler.hill_post(app)
    return render_template('hill_cipher.html')

if __name__ == '__main__':
    app.run(debug=True)