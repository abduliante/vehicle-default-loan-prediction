# Vehicle Loan Default Prediction

## Abstract:
In our project we seek to predict vehicle loan defaults on customers to determine whether a subject of given criteria is receptive to defaulting their loan or not. Data was fetched from Kaggle as a part of FinHack competition by Analytics Vidhya. Our XGBoost model achieved better results in this binary class problem. Lastly, we created a simple interface (that takes input from users and predicts the outcome) and deployed our refined model on Heroku.
 
## Design: 

Our data target consists of two classes, default and not default. Being able to predict people defaulting would help commercial banks to carefully choose who to give loans to. 

## Data:

Our dataset consists of 270,000 rows and 41 columns. Features that influence our target intuitively are taken; in addition to, in-depth analysis to build our models and compare it to our baseline.

## Algorithms

* Feature Engineering:

1. Performed binning on nominal credit score to have 5 labels (Very low, Low, Medium, High, Very high)
2. Creation of new feature called loan to asset ratio where we divide the disbursed amount by the cost of asset

* Models:
Logistics regression, K-nearest neighbors, Random forest, XGBoost, and voting classifier that combines all were used. Our data is imbalance; thus, we used SMOTE oversampling technique. GridSearchCV was used on each model to decide on best parameters. We decided on XGBoost that yielded best results

* Model evaluation and selection:
Data is splitted into train and test from source. In our approach, we splitted our train data into train and validation 80/20 and later on evaluated our chosen model (XGBoost) on test data. All scores below are on weighted average:



|Split|Precision                    |Recall|F1-score                                     |Accuracy|
|-----|-----------------------------|------|---------------------------------------------|--------|
|Training|0.93                         | 0.93 | 0.93                                        | 0.93   |
|Validation|0.68                         |0.63  |0.63                                         |0.63    |
|Test | 0.67                        |0.67  |0.67                                         |0.67    |


# Tools 
* Pandas and Numpy for data manipulation
* Scikit-learn for modeling
* Matplotlib, Seaborn, Tableau for data visualization
	
# Communication
Along with slides, our model is deployed on heroku and can be found [here](HEROKU LINK)
