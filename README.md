# titanic_ticket_checker
Should you get onboard the Titanic? Simple project demonstrating putting a sklearn model inside of a flask application.

Some shortcuts were taken:
* No Exploratory Data Analysis
* No Model Selection (went straight to a Random Forrest)
* No Model Parameter Tuning

# Overview

* `notebooks/00_Preprocessing.ipynb` loads in the source data and preprocesses it
* `model/train.py` can be called from the root directory to train and save the model
* `app.py` houses the flask app that will a guest can check their ticket for potential peril

# Potential Improvements

## Preprocessing
- [ ] Impute the missing values in the `age` column

## Web
- [ ] Better validation of inputs from form
- [ ] Use appropriate controls for data types (numbers, money, selections)
- [ ] Generally make it less fugly