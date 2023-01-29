from flask import Flask, render_template, url_for, request, flash, redirect, send_file
import common
from cipher_algo.playfair_cipher import playfair_encrypt, playfair_decrypt
def playfair_get(app: Flask):
    return render_template('playfair_cipher.html')

def playfair_post(app: Flask):
    data = dict(request.form)
    key = get_key(data)
    if data['input-type'] == 'write':
        text = common.get_input_text(data)
        if data['action-type'] == 'encrypt':
            hasil_cipher_text = playfair_encrypt(key, text)
            return render_template('playfair_cipher.html', hasil_cipher_text=hasil_cipher_text,plain_text=text)
        elif data['action-type'] == 'decrypt':
            hasil_plain_text = playfair_decrypt(key, text)
            return render_template('playfair_cipher.html', cipher_text=text,hasil_plain_text=hasil_plain_text)
    elif data['input-type'] == 'file':
        if data['action-type'] == 'encrypt':
            if 'encode-file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['encode-file']
            filename, file_extension, file_payload = common.get_file_content(file)
            new_filename = filename + '_encrypted' + file_extension
            hasil_cipher_text = playfair_encrypt(key, file_payload.decode("utf-8"))
            destination_path = common.save_result(hasil_cipher_text,app.config['UPLOAD_FOLDER'],new_filename)
            return render_template('playfair_cipher.html', hasil_cipher_filepath=destination_path, hasil_cipher_filename=new_filename)

        elif data['action-type'] == 'decrypt':
            if 'decode-file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['decode-file']
            filename, file_extension, file_payload = common.get_file_content(file)
            new_filename = filename + '_decrypted' + file_extension
            hasil_plain_text = playfair_decrypt(key, file_payload.decode("utf-8"))
            destination_path = common.save_result(hasil_plain_text,app.config['UPLOAD_FOLDER'],new_filename)   
            return render_template('playfair_cipher.html', hasil_plain_filepath=destination_path, hasil_plain_filename=new_filename)

    return render_template('playfair_cipher.html')
        

            

    return 

def get_key(data):
    return data['key']
    