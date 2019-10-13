"MyPueblo" 

Rental Managment Made Easy.

The major backend components of this web-based applications are:

- Predicting the values of real-estate properties using Deep Neural Nets
- Reading bank statements and classifying textual information (merchant names) with multinomial naive bayes algorithm into useful categories such as pest control, home repair, rent, utilities.

These information are incorporated into the web application where users will manage different rental properties with DNN-estimated worth, assess the cost breakdown via automatic classification of rental categories from bank statement (business account), and visualize the sum totals for each category.

##########################################################################################

main backend functions with loaded trained models and sample data: \backend\scripts\main\
classify_bankstatement.py
- loads trained classification model and sample data
- makes category predictions based on the names of merchants -> categories: rent, utilities, home repair, pest control
- outputs csv file with predicted categories in "\backend\rentclassification\bankstatement_classification.csv"

predict_house_price.py
- loads trained classification model and sample data
- estimates property value predictions based on 79 features of the real-estate property
- outputs csv file with estimated values in "\backend\pricepredictions\train_pred.csv"


visualize_totalcosts.py
- loads sample output data from the script classify_bankstatement.py
- clusters and sums all total costs for each category
- visualize the results in bar plot in "\backend\Figure\total_cost.png"

##########################################################################################

scripts related to building backend model for bank statement classification can be found in "\backend\scripts\"

category_class_model_building.ipynb: the entire pipeline of dataprocessing, training NB_based textual multiclassification model and evaluation
accuraccy: 88% on external test set
resulting textual classification model can be located in "\backend\model\finalized_model"


scripts related to building backend model for estimating real estate property value can be found in "\backend\scripts\HousePricePrediction\"
dnn_model_houseprice.ipynb: the entire pipeline of dataprocessing, cleaning up textual data, 'new' algorithm for converting textual data into unique numerical categories, training DNN based regression model and evaluation
rmse: $1983 on training set
resulting house price estimation model can be located in "\backend\model\house_price.h5"
