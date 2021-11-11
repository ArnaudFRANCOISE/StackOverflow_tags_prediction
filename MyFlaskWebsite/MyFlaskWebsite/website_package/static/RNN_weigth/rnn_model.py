from tensorflow import keras
import website_package.static.RNN_weigth.preprocess_tools as pts
import pandas as pd
#!pip install dataframe-image
#import dataframe_image as dfi
import pickle
import numpy as np

def pipeline(data, path_to_model):
    """
    load model cand compute prediction
    """
    data["Body"]  = data["Title"] + data["Body"]
    data = data.drop(["Title", "CreationDate"], axis=1)
    print("input data shape\n",data.head())
    
    
    data['Body'] = data['Body'].apply(pts.preprocess) 
    
    #text to sequence
    print("...preprocessed")
    path_to_tokenizer = "./website_package/static/RNN_weigth/top11_tokenizer.pickle"
    pickle_in = open(path_to_tokenizer,"rb")
    tokenizer = pickle.load(pickle_in)
    print("...word to sequence")
    X_unknown = tokenizer.texts_to_sequences(data["Body"])
    X_unknown = keras.preprocessing.sequence.pad_sequences(X_unknown)
    
    
    #path_to_model = "./SavedModel/RNN_V2_nb_epochs_30/"
    model = keras.models.load_model(path_to_model)
    print("... model sucessfully loaded")
    y = model.predict(X_unknown)

    #cleaning prediction 
    predictions = np.round(y)
    for i in range(predictions.shape[0]):
        arr = predictions[i]
        if sum(arr) == 0:
            predictions[i,np.argmax(y[i])] =1

    #print(predictions.shape)
    predictions_df = pd.DataFrame(predictions,
                   columns=['<android>', '<c#>', '<c++>', '<css>', '<html>', '<java>', '<javascript>',
                    '<python>', '<r>', '<sql>'])
    
    #dfi.export(predictions_df, 'dataframe.png')
    return predictions_df
