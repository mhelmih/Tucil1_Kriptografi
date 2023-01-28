from flask import Flask, render_template, url_for, request, flash, redirect, send_file
from werkzeug.datastructures import ImmutableMultiDict
from cipher_algo.affine_cipher import affine_encrypt, affine_decrypt
import os

UPLOAD_FOLDER = './uploads' 
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download/<path>')
def download_file(path):
    print(path)
    return send_file(path, as_attachment=True)

@app.route('/affine_cipher/', methods=['GET','POST'])
def affine_cipher():
    if request.method == 'GET':
        return render_template('affine_cipher.html')
    if request.method == 'POST':
        data = dict(request.form)
        if data['action-type'] == 'encrypt':
            if data['input-type'] == 'write':
                plain_text = data['text']
                coprime = int(data['coprime'])
                pergeseran = int(data['koefisien-pergeseran'])
                hasil_cipher_text = affine_encrypt(plain_text, pergeseran, coprime)
                return render_template('affine_cipher.html', hasil_cipher_text=hasil_cipher_text,plain_text=plain_text)
            
            if data['input-type'] == 'file':
                if 'encode-file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['encode-file']
                # If the user does not select a file, the browser submits an
                # empty file without a filename.
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                file_payload = file.read()
                filename, file_extension = os.path.splitext(file.filename)
                new_filename = filename + '_encrypted' + file_extension

                coprime = int(data['coprime'])
                pergeseran = int(data['koefisien-pergeseran'])

                hasil_cipher_text = affine_encrypt(file_payload.decode("utf-8"),pergeseran,coprime)

                hasil_cipher_bytes = bytes(hasil_cipher_text, encoding='utf-8')

                destination_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                f = open(destination_path, "wb")
                f.write(hasil_cipher_bytes)
                f.close()
                return render_template('affine_cipher.html', hasil_cipher_filepath=destination_path, hasil_cipher_filename=new_filename)

        elif data['action-type'] == 'decrypt':
            if data['input-type'] == 'write':
                cipher_text = data['text']
                coprime = int(data['coprime'])
                pergeseran = int(data['koefisien-pergeseran'])
                hasil_plain_text = affine_decrypt(cipher_text, pergeseran, coprime)
                return render_template('affine_cipher.html', cipher_text=cipher_text,hasil_plain_text=hasil_plain_text)

            if data['input-type'] == 'file':
                if 'decode-file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['decode-file']
                # If the user does not select a file, the browser submits an
                # empty file without a filename.
                if file.filename == '':
                    flash('No selected file')
                    return redirect(request.url)
                file_payload = file.read()
                filename, file_extension = os.path.splitext(file.filename)
                new_filename = filename + '_decrypted' + file_extension

                coprime = int(data['coprime'])
                pergeseran = int(data['koefisien-pergeseran'])

                hasil_plain_text = affine_decrypt(file_payload.decode("utf-8"),pergeseran,coprime)

                hasil_plain_bytes = bytes(hasil_plain_text, encoding='utf-8')

                destination_path = os.path.join(app.config['UPLOAD_FOLDER'], new_filename)
                f = open(destination_path, "wb")
                f.write(hasil_plain_bytes)
                f.close()
                return render_template('affine_cipher.html', hasil_plain_filepath=destination_path, hasil_plain_filename=new_filename)
        
        return render_template('affine_cipher.html')


if __name__ == '__main__':
    app.run(debug=True)