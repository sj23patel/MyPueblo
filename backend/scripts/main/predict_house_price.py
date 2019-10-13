from keras.models import load_model
import pandas as pd
import numpy
from sklearn.impute import SimpleImputer
from sklearn import preprocessing

def data_process(pre_all_data):
    '''
    '''
    # convert the dataframe to numpy array
#   pre_all_data = pre_all_data.convert_objects(convert_numeric=True)
    pre_all_data = pre_all_data.fillna(0)
    # all_data_np = pre_all_data.values

    # drop numeric columns
    temp = pre_all_data.apply(pd.to_numeric,errors='coerce').isnull().any()
    numeric_error_columns = [pre_all_data.columns[i] for i in range(len(temp)) if temp[i] == True]
    print('Below are the numeric Error Columns. Convert to numerical values. ')
    print(numeric_error_columns)
    pre_values_df = pre_all_data.drop(columns=numeric_error_columns)
    text_df = pre_all_data[numeric_error_columns]

    # convert textual data frame to numerical data frame
    numeric_df = convert_text_numeric(text_df)

    all_df = pd.concat([pre_values_df, numeric_df], axis=1, sort=False)
    # preprocess data for features with original values, normalize columns
    imputer    = SimpleImputer()
    scaler     = preprocessing.MinMaxScaler()
    values_df   = scaler.fit_transform(imputer.fit_transform(all_df))

    print("values_df :", values_df.shape)

    return values_df

def convert_text_numeric(df):
    headers = df.columns.tolist()
    for each in headers:
        unique = list(set(df[each].values.tolist()))
        actual_list = df[each].values.tolist()
        num_categories = [j for j in range(len(unique))]
        text_num_dict = dict(zip(unique, num_categories))
        numerized_list = [text_num_dict[i] for i in actual_list]
#         print(numerized_list)
        df[each]=numerized_list
    return df

def main():
    path = 'G:/My Drive/NCSU/Hackathons/HackNC2019/MyPueblo/backend/'

    model = load_model(path+'model/house_price.h5')

    df = pd.read_csv(path + 'data/house_price/train.csv')
    IDs     = df[['Id']]
    pre_data    = df.drop(columns=['Id','SalePrice'])

    data = data_process(pre_data)
    predictions = model.predict(data)
    predictions_list  = numpy.concatenate(predictions, axis=0).tolist()

    df['pred_value'] = predictions_list

    ids = df.Id.values.tolist()
    values = df.pred_value.values.tolist()
    for j in range(len(ids)):
        print('Estimated value for rental ID ' + str(ids[j]) + ' is $' + str(values[j]))

    df.to_csv(path + 'pricepredictions/train_pred.csv')

main()
