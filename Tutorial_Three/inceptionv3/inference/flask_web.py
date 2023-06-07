from flask import Flask, request, redirect, url_for, flash
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.inception_v3 import *
from tensorflow.keras import backend as K
from werkzeug.utils import secure_filename

import json
import numpy as np
import os

UPLOAD_FOLDER = './image_sets/'
if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def InceptV3(img):
    # Load InceptionV3 Image
    model = InceptionV3(include_top=True, weights='imagenet')
    # Resize the image
    img = image.load_img(img, target_size=(299, 299))
    # Change the image to array
    x = image.img_to_array(img)
    # Add dimension to image
    x = np.expand_dims(x, axis=0)
    # Normalize the data between 0 to 1
    x = preprocess_input(x)
    # Get prediciton
    preds = model.predict(x)
    result = dict((key, str(value)) for (_,key, value) in decode_predictions(preds)[0])
    K.clear_session()
    return json.dumps(result)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    global model
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            predict_results = InceptV3(img)
            return predict_results
    return  '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=input name=epoch>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/train',methods = ['GET','POST'])
def training():
    if request.method == "POST":

        return "This is inceptionV3 return"
    return '''
    <!doctype html>
    <title>Training</title>
    <h1>Training Custom data</h1>
    <form method=post enctype=mulitpart/form-data>
    Bucket Name:<br>
    <input name=bucket><br>
    Bucket Access Key:<br>
    <input name=bkey><br>
    Bucket Secret Key:<br>
    <input name=skey><br>
    Epoch:<br>
    <input name=epoch><br>
    Batch:<br>
    <input name=lr><br>
    Learning Rate:<br>
    <input name=lr><br>
    Decay:<br>
    <input name=decay><br>
    Momentum:<br>
    <input name=mm><br>
    <input type=submit value=Start>
    </form>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001,debug=True,threaded=False)
