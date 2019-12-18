from __future__ import division, print_function
import numpy as np
import os
import librosa
import keras
from keras import backend as K
from keras.models import Sequential,load_model
from flask import Flask,jsonify,redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
from gevent.pywsgi import WSGIServer
from playsound import playsound

app = Flask(__name__)

def get_model():
    global model
    model=load_model('audio_classification_cnn.hdf5') 
    print("Model loaded")

get_model()

def get_file_path_and_save(request):
    # Get the file from post request
    f = request.files['file']   # Save the file to ./uploads
    basepath = os.path.dirname(__file__)
    file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
    fullfilepath=os.path.join(basepath, secure_filename(f.filename))
    f.save(file_path)
    print('filename is',f)
    return f
    

@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def running():
    return 'Hey there! Want to get some prediction results?'

@app.route("/predictResNet50",methods=['POST'])
def predictResNet50():
    if request.method == 'POST':
            
            filename = get_file_path_and_save(request)
            print(filename)
#            
#            features = np.empty((0,195))
#            X, sample_rate = librosa.load(filename)
#            stft = np.abs(librosa.stft(X))
#            mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T,axis=0)
#            chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T,axis=0)
#            mel = np.mean(librosa.feature.melspectrogram(X, sr=sample_rate).T,axis=0)
#            contrast = np.mean(librosa.feature.spectral_contrast(S=stft, sr=sample_rate).T,axis=0)
#            tonnetz = np.mean(librosa.feature.tonnetz(y=librosa.effects.harmonic(X), sr=sample_rate).T,axis=0)
#            zcrs = np.mean(librosa.feature.zero_crossing_rate(y=X).T,axis=0)
#            spectral_centroids = np.mean(librosa.feature.spectral_centroid(y=X, sr=sample_rate).T,axis=0)
#            ext_features = np.hstack([mfccs,chroma,mel,contrast,tonnetz,zcrs,spectral_centroids])
#            features = np.vstack([features,ext_features])
#            x = features
#            x = x.reshape(x.shape[0], x.shape[1],1)
#            noise_category = ["normal","klappern","schwirren"]
#            res_x = x
#            predictions = model.predict(res_x)
#            for i in range(len(predictions[0])):
#            
#                print( filename, "=", round(predictions[0,i] * 100, 1))
#             # get the indices of the top 2 predictions, invert into descending order
#            ind = np.argpartition(predictions[0], -2)[-2:]
#            ind[np.argsort(predictions[0][ind])]
#            ind = ind[::-1]
#            first_guess=round(predictions[0,ind[0]],3)
#            result= str(first_guess[0],[0],[1])
#            second_guess=round(predictions[0,ind[1]],3)
#            print("Top guess: ", noise_category[ind[0]], round(predictions[0,ind[0]],3))
#            print("2nd guess: ", noise_category[ind[1]], round(predictions[0,ind[1]],3))
#            if(noise_category[ind[0]]=="normal"):
#                print("Audio file is good")
#            else:
#                print("Audio file is not good")
#                
#            return result
    return None


if __name__ == "__main__":
    
    app.run(debug=True)
