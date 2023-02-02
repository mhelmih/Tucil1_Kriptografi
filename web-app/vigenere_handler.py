import common
from flask import Flask, render_template, request, flash, redirect
from cipher_algo.vigenere_cipher import vigenere_standard_encrypt, vigenere_standard_decrypt
from cipher_algo.vigenere_cipher import vigenere_autokey_encrypt, vigenere_autokey_decrypt
from cipher_algo.vigenere_cipher import vigenere_extended_encrypt, vigenere_extended_decrypt


def vigenere_get(app: Flask):
    return render_template('vigenere_cipher.html')

def vigenere_post(app: Flask):
    data = dict(request.form)
    if data['input-type'] == 'write':
        if data['action-type'] == 'encrypt':
            ciphertext = vigenere_encrypt(data['text'], data['key'], data['vigenere-mode'])
            return render_template('vigenere_cipher.html', hasil_cipher_text=ciphertext, plain_text=data['text'])
        elif data['action-type'] == 'decrypt':
            plaintext = vigenere_decrypt(data['text'], data['key'], data['vigenere-mode'])
            return render_template('playfair_cipher.html', cipher_text=data['text'],hasil_plain_text=plaintext)
        
    elif data['input-type'] == 'file':
        if data['action-type'] == 'encrypt':
            if 'encode-file' not in request.files:
                flash('No file part')
                return redirect(request.url)

            filename, file_extension, file_payload = common.get_file_content(request.files['encode-file'])
            new_filename = filename + '_encrypted' + file_extension
            
            if data['vigenere-mode'] == 'extended':
                ciphertext = vigenere_encrypt(file_payload, data['key'], data['vigenere-mode'])
                destination_path = common.save_binary_result(ciphertext, app.config['UPLOAD_FOLDER'], new_filename)
            else:
                ciphertext = vigenere_encrypt(file_payload.decode('utf-8'), data['key'], data['vigenere-mode'])
                destination_path = common.save_result(ciphertext, app.config['UPLOAD_FOLDER'], new_filename)

            return render_template('vigenere_cipher.html', hasil_cipher_filepath=destination_path, hasil_cipher_filename=new_filename)
        
        elif data['action-type'] == 'decrypt':
            if 'decode-file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            
            filename, file_extension, file_payload = common.get_file_content(request.files['decode-file'])
            new_filename = filename + '_decrypted' + file_extension
            
            if data['vigenere-mode'] == 'extended':
                plaintext = vigenere_decrypt(file_payload, data['key'], data['vigenere-mode'])
                destination_path = common.save_binary_result(plaintext, app.config['UPLOAD_FOLDER'], new_filename)
            else:
                plaintext = vigenere_decrypt(file_payload.decode('utf-8'), data['key'], data['vigenere-mode'])
                destination_path = common.save_result(plaintext, app.config['UPLOAD_FOLDER'], new_filename)
                
            return render_template('vigenere_cipher.html', hasil_plain_filepath=destination_path, hasil_plain_filename=new_filename)

    return render_template('vigenere_cipher.html')

def vigenere_encrypt(plaintext, key, mode):
    if mode == 'standard':
        return vigenere_standard_encrypt(plaintext, key)
    elif mode == 'auto-key':
        return vigenere_autokey_encrypt(plaintext, key)
    elif mode == 'extended':
        return vigenere_extended_encrypt(plaintext, key)
    
def vigenere_decrypt(ciphertext, key, mode):
    if mode == 'standard':
        return vigenere_standard_decrypt(ciphertext, key)
    elif mode == 'auto-key':
        return vigenere_autokey_decrypt(ciphertext, key)
    elif mode == 'extended':
        return vigenere_extended_decrypt(ciphertext, key)
    