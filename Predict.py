import subprocess
import pandas as pd
import xgboost as xgb


def run():
    subprocess.call ("/Users/hlabs/Desktop/hoop/voicebot/gendervoice/ExtractFeatures.R", shell=True)

    features_to_use = ["meanfreq","sd","median","Q25","Q75","IQR","skew","kurt","sp.ent","sfm","mode","centroid","meanfun","minfun","maxfun","meandom","mindom","maxdom","dfrange","modindx"]

    test_df = pd.read_csv('/Users/hlabs/Desktop/hoop/voicebot/gendervoice/test.csv')

    test_X = test_df[features_to_use]
    xgtest = xgb.DMatrix(test_X)

    model = xgb.Booster({'nthread':4})
    model.load_model("/Users/hlabs/Desktop/hoop/voicebot/gendervoice/voice-gender.model")

    pred_test_y = model.predict(xgtest)

    if pred_test_y >= 0.5:
        gender1= "male"
    else:
        gender1= "female"
    
    print(gender1)

    # import mysql.connector

    # db = mysql.connector.connect(
    #     host="127.0.0.1",
    #     user = "root",
    #     passwd = "hoopproj1",
    #     database = "store"
    # )

    # mycursor = db.cursor()
    # mycursor.execute("INSERT INTO store (gender) VALUES (%s)", (gender1,))
    # db.commit()


run()