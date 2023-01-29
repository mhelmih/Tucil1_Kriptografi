from cipher_algo.affine_cipher import affine_encrypt, affine_decrypt
from flask import Flask, render_template, url_for, request, flash, redirect, send_file
import os, common



def affine_get(app):
    return render_template('affine_cipher.html')

def affine_post(app):
    data = dict(request.form)
    coprime = get_coprime(data)
    pergeseran = get_pergeseran(data)
    if data['action-type'] == 'encrypt':
        if data['input-type'] == 'write':
            plain_text = common.get_input_text(data)
            hasil_cipher_text = affine_encrypt(plain_text, pergeseran, coprime)
            return render_template('affine_cipher.html', hasil_cipher_text=hasil_cipher_text,plain_text=plain_text)
        
        if data['input-type'] == 'file':
            if 'encode-file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['encode-file']

            filename, file_extension, file_payload = common.get_file_content(file)
            
            new_filename = filename + '_encrypted' + file_extension

            hasil_cipher_text = affine_encrypt(file_payload.decode("utf-8"),pergeseran,coprime)

            destination_path = common.save_result(hasil_cipher_text,app.config['UPLOAD_FOLDER'],new_filename)            

            return render_template('affine_cipher.html', hasil_cipher_filepath=destination_path, hasil_cipher_filename=new_filename)

    elif data['action-type'] == 'decrypt':
        if data['input-type'] == 'write':
            cipher_text = common.get_input_text(data)
            hasil_plain_text = affine_decrypt(cipher_text, pergeseran, coprime)
            return render_template('affine_cipher.html', cipher_text=cipher_text,hasil_plain_text=hasil_plain_text)

        if data['input-type'] == 'file':
            if 'decode-file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['decode-file']

            filename, file_extension, file_payload = common.get_file_content(file)

            new_filename = filename + '_decrypted' + file_extension

            hasil_plain_text = affine_decrypt(file_payload.decode("utf-8"),pergeseran,coprime)

            destination_path = common.save_result(hasil_plain_text,app.config['UPLOAD_FOLDER'],new_filename)            
            return render_template('affine_cipher.html', hasil_plain_filepath=destination_path, hasil_plain_filename=new_filename)

def get_coprime(data):
    return int(data['coprime'])

def get_pergeseran(data):
    return int(data['koefisien-pergeseran'])

