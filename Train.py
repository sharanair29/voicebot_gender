import numpy as np
import pandas as pd
from scipy import sparse
import xgboost as xgb
from sklearn import model_selection, preprocessing, ensemble
from sklearn.metrics import log_loss
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from termcolor import colored

def runXGB(X, y):
    param = {}
    param['objective'] = 'binary:logistic'
    param['eta'] = 0.01                     #default: 0.3
    param['max_depth'] = 6                  #default: 6
    param['silent'] = 1
    param['gamma'] = 0                      #default: 0
    param['eval_metric'] = "logloss"
    param['min_child_weight'] = 4           #default: 1
    param['max_delta_step'] = 4             #default: 0
    param['subsample'] = 0.7                  #default: 1
    param['colsample_bytree'] = 0.7           #default: 1
    param['seed'] = 0
    num_rounds = 2500

    plst = list(param.items())
    #label y and data is x

    data_train, data_cv, labels_train, labels_cv = train_test_split(X, y, test_size=0.20, random_state=42)
    #train
    xgtrain = xgb.DMatrix(data_train, label = labels_train)
    #test
    xgcv = xgb.DMatrix(data_cv, label = labels_cv)
    print(labels_cv)
    print(data_cv)

    evallist = [(xgcv,'eval')]
    model = xgb.train(plst, xgtrain, num_rounds, evallist, early_stopping_rounds = 100)

    model.save_model('/Users/hlabs/Desktop/hoop/voicebot/gendervoice/voice-gender.model')
    #Prediction on validation set
    y_pred = model.predict(xgcv)

    # Making the Confusion Matrix
    cm = confusion_matrix(labels_cv, (y_pred>0.5))
    print(colored('The Confusion Matrix is: ', 'red'),'\n', cm)
    # Calculate the accuracy on test set
    predict_accuracy_on_test_set = (cm[0,0] + cm[1,1])/(cm[0,0] + cm[1,1]+cm[1,0] + cm[0,1])
    print(colored('The Accuracy on Test Set is: ', 'blue'), colored(predict_accuracy_on_test_set, 'blue'))
     
train_df = pd.read_csv('/Users/hlabs/Desktop/hoop/voicebot/gendervoice/voice.csv')

X = train_df.iloc[:, 0:20]
y = train_df["label"]
y = y.replace({'male':1,'female':0})

runXGB(X, y)





