from flask import Blueprint, render_template, send_file
import os
from flask import Flask, flash, request, redirect, url_for
#from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, abort, session, redirect, \
    request, current_app as app
#import matplotlib.pyplot as plt 
from pandas.plotting import table 
import pandas as pd


import website_package.static.RNN_weigth.rnn_model as model


from flask import current_app
pred = Blueprint("pred", __name__)

ALLOWED_EXTENSIONS = {'csv'}
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@pred.route('/pred', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #filename = secure_filename(file.filename)
            #print("uploadbutton pushed")
            #file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
            data = pd.read_csv(file)[:10]
            
            #path1 = os.path.dirname(os.path.abspath(__file__))


            #----------------------- PREDICTION---------------------
            data = model.pipeline(data, "./MyFlaskWebsite/website_package/static/RNN_weigth/RNN_V2_RNN_V2_14")
            #-------------------------------------------------------
            path = "MyFlaskWebsite/website_package/uploadfile/data.csv"
            data.to_csv(path)
            
            #uploads = os.path.join(current_app.root_path, app.config['UPLOAD_FOLDER'])
            return send_file("./uploadfile/data.csv" , as_attachment=True)
            
    #os.remove("MyFlaskWebsite/website_package/uploadfile/data.csv")
    return render_template("pred.html")
