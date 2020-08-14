from keras.models import model_from_json
import librosa
import librosa.feature
import glob
import numpy as np


def load_model():
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()

    loaded_model = model_from_json(loaded_model_json)
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    return loaded_model


def extract_features_song(src):
    y, _ = librosa.load(src)
    #get mfcc
    mfcc = librosa.feature.mfcc(y)
    #normalize between -1 and 1
    mfcc /= np.amax(np.absolute(mfcc))
    
    return np.ndarray.flatten(mfcc)[:25000]



def get_genre(fname):
    genres = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
    model  = load_model()
    features = extract_features_song(fname)
    try:
        features = np.reshape(features, (1,25000))
        prediction = model.predict(features)
        genre_idx = np.argmax(prediction)
        return genres[genre_idx]

    except:
        return "File too short. Not enough features to predict."


