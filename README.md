# Estimating the probabiliy of financial distress for borrowers using different models in Machine Learning

This was a free assignment in an introductory course in Machine Learning. We chose the competition [Give me some Credit](https://www.kaggle.com/c/GiveMeSomeCredit) on [kaggle.com](https://www.kaggle.com). 

We built three estimators with `sklearn`:
- Logistic Regression
- Support Vector Machine
- Random Forest

We tested different methods of data preprocessing by filling nan-values with the columns means or throwing them out. Also outliers were manually eliminated by checking against multiples of the standard deviation. 
Due to an imbalanced dataset, we tried to maintain am evened out set by either _Oversampling_ or _Undersampling_ respectively.

Also, in regard to the data imbalance we found the ROC-AUC score to be more descriptive than the classic accuracy. 

The different steps of preprocessing and the three models can be found in the seperate _ipython notenooks_.

As of writing this, the code runs with the following versions:

- Python 2.7.10
- ipython notebook 3.2.1
- SciKitLearn 0.16.1
- Pandas 0.16.2

