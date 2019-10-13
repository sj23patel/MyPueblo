from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble

import pandas as pd
import numpy, textblob, string, random
from keras.preprocessing import text, sequence
from keras import layers, models, optimizers

from sklearn.externals import joblib
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.ticker as mtick

def predict_categories(path):

    original_df = pd.read_csv(path + 'data/categorize_transactions/train_data.csv')
    bank_df = pd.read_csv(path+'data/sample_user/bankstatement.csv')

    text= original_df['Description']
    encoder = preprocessing.LabelEncoder()
    final_y =  encoder.fit_transform(original_df['Category'])

    # create a count vectorizer object
    count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
    count_vect.fit(original_df['Description'])
    final_count = count_vect.transform(bank_df['Description'])
    filename = path + 'model/finalized_model.sav'

    final_NB_model = joblib.load(filename)
    NB_final_model_predictions = final_NB_model.predict(final_count)
    category_predictions = encoder.inverse_transform(NB_final_model_predictions)

    # cost = bank_df['Cost']
    bank_df['pred_categories']=category_predictions
    return bank_df
def main():
    path = 'G:/My Drive/NCSU/Hackathons/HackNC2019/MyPueblo/backend/'
    predicted_df = predict_categories(path)
    predicted_df.to_csv(path+'rentclassification/bankstatement_classification.csv',index=False)

main()
