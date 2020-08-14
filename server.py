#!/usr/bin/env python3
import os
from flask import Flask, render_template, request, redirect,url_for, session
from werkzeug.utils import secure_filename
import utils

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
app.config['SECRET_KEY'] = '\x9f\xce\x1d/\xcf2{Ud\x06\x05R\xc5Z\x062\xd8Y\x86gzq\xa9U'


@app.route('/song/<name>/<genre>')
def song_info(name, genre):
    
    return render_template('song_info.html', name=name, genre=genre)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/sendfile", methods=["POST"])
def send_file():
    #save the file
    fileob = request.files["audio"]
    filename = fileob.filename
    fileob.save(filename)

    genre = utils.get_genre(filename)
    os.remove(filename)

    return {"name": filename, "genre": genre}
   
    





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)