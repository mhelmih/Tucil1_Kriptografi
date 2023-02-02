from flask import Flask, render_template, url_for, request, flash, redirect, send_file
import common
from cipher_algo.hill_cipher import hill_encrypt, hill_decrypt

def hill_get(app: Flask):
    return render_template('hill_cipher.html', n=3)

def hill_post(app:Flask):
    data = dict(request.form)
    matrix = get_matrix(data)
    print(matrix)
    n = int(data['dimension'])
    if data['action-type'] == 'resize':
        text=''
        if data['input-type'] == 'write':
            text = common.get_input_text(data)
        return render_template('hill_cipher.html',n=n,plain_text=text, matrix=matrix)
    else:
        if data['input-type'] == 'write':
            text = common.get_input_text(data)
            if data['action-type'] == 'encrypt':
                hasil_cipher_text = hill_encrypt(text,n,matrix)
                return render_template('hill_cipher.html', hasil_cipher_text=hasil_cipher_text,plain_text=text,matrix=matrix,n=n)
            elif data['action-type'] == 'decrypt':
                hasil_plain_text = hill_decrypt(text,n,matrix)
                return render_template('hill_cipher.html', hasil_plain_text=hasil_plain_text,cipher_text=text,matrix=matrix,n=n)
        elif data['input-type'] == 'file':
            if data['action-type'] == 'encrypt':
                if 'encode-file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['encode-file']
                filename, file_extension, file_payload = common.get_file_content(file)
                new_filename = filename + '_encrypted' + file_extension
                hasil_cipher_text = hill_encrypt(file_payload.decode("utf-8"),n,matrix)
                destination_path = common.save_result(hasil_cipher_text,app.config['UPLOAD_FOLDER'],new_filename)
                return render_template('hill_cipher.html', hasil_cipher_filepath=destination_path, hasil_cipher_filename=new_filename,matrix=matrix,n=n)

            elif data['action-type'] == 'decrypt':
                if 'decode-file' not in request.files:
                    flash('No file part')
                    return redirect(request.url)
                file = request.files['decode-file']
                filename, file_extension, file_payload = common.get_file_content(file)
                new_filename = filename + '_decrypted' + file_extension
                hasil_plain_text = hill_decrypt(file_payload.decode("utf-8"),n,matrix)
                destination_path = common.save_result(hasil_plain_text,app.config['UPLOAD_FOLDER'],new_filename)   
                return render_template('hill_cipher.html', hasil_plain_filepath=destination_path, hasil_plain_filename=new_filename,matrix=matrix,n=n)


def get_matrix(data):
    matrix = []
    dimension = int(data['dimension'])
    for i in range(dimension):
        row = []
        for j in range(dimension):
            name = "cell-" + str(i) + "-" + str(j)
            try:
                el = data[name]
            except:
                el = ''
            if el == '':
                row.append(el)
            else:
                row.append(int(el))
        matrix.append(row)
    return matrix