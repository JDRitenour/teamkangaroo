# Team Kangaroo - USPS Weather Impact Challenge

### Table of Contents

1. [Installation](#installation)
2. [Project Goals](#goals)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)

## Installation <a name="installation"></a>

The following packages are required to run the files in this repository: Pandas, Numpy, Matplotlib, Seaborn, Polars, Sklearn, XGBoost, LightGBM, CATBoost, Pgmpy, shap

## Project Goals<a name="goals"></a>

The United States Postal Service (USPS) aims to increase knowledge about how weather events impact mail and package processing, transportation and delivery. The USPS has partnered with George Mason University students to build a machine learning model that will use publicly acquired weather data to predict if a piece of mail or a package will be late.

<strong> Can weather predict if a ​piece of mail or a package ​will be late? </strong>

## File Descriptions <a name="files"></a>

<strong>Package_Notebooks</strong>
<ol>
  <li>Package_EDA.ipynb - Exploratory Data Analysis on USPS Packages</li>
  <li>package_scans_cleaned.ipynb - Data Conditioning on the Package Scans Data</li>
  <li>package_data_final.ipynb - Data Conditioning to combine package and weather data</li>
  <li>MODEL_EXPLORATION.ipynb - Assesses a Random Forest, XGBoost, Gradient Boosting, LightGBM, CatBoost, Neural Network, and Naive Bayes model on the USPS Package Data</li>
  <li>RF&XG_REGRESSOR_MODEL.ipynb - Assesses a Random Forest Regressor and XGB Regressor Model on the USPS Package Data</li>
  <li>XGBOOST_USPS_Packages.ipynb - Assesses a XGBoost model on the USPS Package Data</li>
</ol>

<strong>Mail_Notebooks</strong>
<ol>
  <li>mail_data_cleaned.ipynb - Clean and pull the weather data for the USPS mail data</li>
  <li>xgboost_mail.ipynb - Assess the XGBoost Model on the USPS mail data</li>
</ol>

## Results<a name="results"></a>

We found that weather does play a key role in determining is a peice of mail or a package will be on time or late. The XGBoost model performed the best. The package data model had an accuracy of 0.894 and an AUC of 0.933. The mail data model had an accuracy of 0.93 and an AUC of 98.6%.

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

The data used in this project is the property of the United State Postal Service, and the National Oceanic & Atmospheric Administration. This project was completed by students of George Mason University.
