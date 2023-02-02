from flask import Flask, render_template, url_for, request, flash, redirect, send_file
import os
def get_input_text(data):
    return data['text']

def get_file_content(file):
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_payload = file.read()
    filename, file_extension = os.path.splitext(file.filename)

    return filename, file_extension, file_payload

def save_result(text, path, filename):
    hasil_bytes = bytes(text, encoding='utf-8')

    destination_path = os.path.join(path, filename)
    f = open(destination_path, "wb")
    f.write(hasil_bytes)
    f.close()
    return destination_path

def save_binary_result(text, path, filename):
    destination_path = os.path.join(path, filename)
    f = open(destination_path, "wb")
    f.write(text)
    f.close()
    return destination_path