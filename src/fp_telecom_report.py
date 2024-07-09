# -*- coding: utf-8 -*-
"""Copy of FP Telecom_Report.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mgmgNpVAeTptMYcVqvL60wQJY7uBw4wD

#**Project Summary Report: Analysis of Churn Customer**

##**Introduction**
Interconnect is a telecommunications company specializing in landline and internet services. Additionally, it offers services like Internet Security, Tech Support, Cloud Storage, Online Backup, and Streaming Services. To maintain profitability, Interconnect aims to predict customer churn rates accurately. By identifying potential churn clients, the company can offer promotional codes and special packages to retain these customers. The marketing team has gathered necessary data, including client information, contract details, and current services.

###**Goal**
The goals of this project are:

Develop a machine learning model to predict client churn with an AUC-ROC score of at least 0.88.
Utilize the F1 score as an additional evaluation metric.
Perform statistical calculations and visualize findings.
Compare the behavior of telephone and internet users.

###**Steps**
The steps of this project are:

1. Load and study the general information of the data.
2. Explore and analyze the data.
3. Prepare the data by addressing anomalies and checking class balance.
4. Create and train the machine learning model, aiming for an AUC-ROC score above or equal to 0.88.
5. Draw conclusions from the analysis.

###**Data List**
1. Contract Data
  - customerID: Unique identifier for each customer.
  - BeginDate: Contract start date.
  - EndDate: Contract end date (NaT for active customers).
  - Type: Contract type (e.g., month-to-month, one year, two years).
  - PaperlessBilling: Indicator for paperless billing.
  - PaymentMethod: Chosen payment method.
  - MonthlyCharges: Monthly charges for services.
  - TotalCharges: Total charges over the contract period.
2. Personal Data
  - customerID: Unique identifier for each customer.
gender: Customer's gender.
  - SeniorCitizen: Indicator for senior citizen status (1 for yes, 0 for no).
  - Partner: Indicator for having a partner or spouse.
  - Dependents: Indicator for having dependents.
3. Internet Data
  - customerID: Unique identifier for each customer.
  - InternetService: Type of internet service subscribed.
  - OnlineSecurity: Subscription to online security service.
  - OnlineBackup: Subscription to online backup service.
  - DeviceProtection: Subscription to device protection service.
  - TechSupport: Access to technical support.
  - StreamingTV: Subscription to TV streaming service.
  - StreamingMovies: Subscription to movie streaming service.
4. Phone Data
  - customerID: Unique identifier for each customer.
  - MultipleLines: Indicator for multiple phone lines.

##**Exploratory Data Analysis**

###**Findings**
1. Active customers generally have similar monthly spending but higher total spending compared to churned customers.
2. Churned customers tend to have higher monthly charges.
3. Monthly contract renewals correlate with higher churn rates.
4. Manual payment methods are more common among churned customers.
5. Gender, senior citizen status, partnership, dependents, and phone line type do not significantly affect churn rates.
6. Fiber optic users are more likely to churn compared to DSL users.
7. Lack of technical support and online security services correlate with higher churn rates.

###**Statistical Analysis**

1. Monthly Payment Distribution:


No significant difference in average monthly payments between churned and active customers. Churned customers have a smaller interquartile range, indicating less variability in monthly charges.
"""

import pandas as pd

# Data
data = {
    "Metric": ["Q1", "Q3", "IQR", "Lower Whisker", "Upper Whisker", "Average Monthly Charge"],
    "Churned": [72.21, 95.45, 23.24, 37.36, 130.31, 82.25],
    "Active": [68.15, 95.95, 27.80, 26.45, 137.65, 81.51]
}

# Create DataFrame
df_payment_distribution = pd.DataFrame(data)

# Display DataFrame
df_payment_distribution

"""2. Service Usage:

- Internet Service:
  - 21.7% of customers do not use internet service.
  - 78.3% use internet service.
- Phone Service:
  - 9.7% of customers do not use phone service.
  - 90.3% use phone service.

##**Results**

###**Machine Learning Model Development**

Feature engineering is a crucial step in the data preprocessing phase of building a machine learning model. It involves transforming raw data into features that better represent the underlying problem to the predictive models, resulting in improved model performance. Here are the detailed steps we will follow:

1. Merge All Data into One Dataset
- Given multiple datasets (e.g., personal data, contract data, internet data), we need to combine them into a single cohesive dataset for analysis and modeling. This can be done using the common customerID column as the key for merging.

2. Drop Unnecessary Column(s)
- Certain columns may not provide useful information for predicting churn or might introduce noise into the model. For example, customerID, BeginDate, and EndDate are typically not useful for prediction and can be dropped.

3. One-Hot Encoding to Turn Categorical Data into Boolean
- Machine learning algorithms require numerical input, so categorical variables need to be converted. One-hot encoding is a method to convert categorical variables into a series of binary columns. For instance, a column with values "Month-to-Month", "One Year", and "Two Year" would be converted into three separate columns with binary values.

4. Split the Data into Feature and Target
- Separate the dataset into the features (predictor variables) and the target variable (what we are trying to predict). In this case, the target variable is churn.

5. Split the Data into Train Set and Test Set
- To evaluate the performance of the machine learning model, we need to split the data into training and testing sets. The training set is used to train the model, while the test set is used to evaluate its performance on unseen data.


Models tested:
- Logistic Regression
- Random Forest Classifier
- Decision Tree Classifier
- XGBoost Classifier
- LightGBM Classifier
- CatBoost Classifier
- Gradient Boosting Classifier

###**Model Performance**
"""

import pandas as pd

# Data
results = {
    "model": ["GradientBoostingClassifier", "CatBoostClassifier", "XGBClassifier",
              "LGBMClassifier", "RandomForestClassifier", "DecisionTreeClassifier",
              "LogisticRegression"],
    "roc_auc_train": [86.98, 85.85, 86.36, 86.01, 85.54, 84.35, 83.34],
    "roc_auc_test": [85.88, 85.85, 85.53, 85.50, 85.12, 85.02, 83.95],
    "precision_train": [71.52, 69.63, 70.35, 69.17, 71.23, 63.50, 64.46],
    "precision_test": [66.39, 64.52, 66.96, 66.10, 69.39, 60.15, 63.91],
    "f1_score_train": [60.63, 61.33, 59.59, 60.07, 53.74, 55.14, 57.29],
    "f1_score_test": [57.04, 56.74, 55.56, 56.52, 53.12, 54.98, 58.42]
}

# Create DataFrame
df_results = pd.DataFrame(results)

# Display DataFrame
df_results

"""The Gradient Boosting Classifier achieved the highest ROC AUC score, indicating good discrimination between churn and non-churn customers. Its F1 score suggests a need for better balance between precision and recall.

##**Difficulties Occured During Project**

1. The data distribution of churn customer is imbalance that cause,
2. Difficulty on finding the right hyperparameter and machine learning model to achieved 88% score at ROC AUC.
3. Trial and error has been conducted during one-hot-encoding that leads to re-run the machine learning model.

##**Summary**
The project successfully developed a machine learning model to predict customer churn for Interconnect, achieving an AUC-ROC score of 85.88% with the Gradient Boosting Classifier. Although this did not meet the goal of 0.88, it still represents a strong performance. The analysis revealed that churned customers typically have higher monthly charges and that factors such as contract type, payment method, and lack of technical support or online security services contribute to churn. These insights can help Interconnect in strategizing retention efforts and improving customer satisfaction.

Recommendations to Treat Potential Churn Customers

1. Targeted Promotions and Discounts:
Offer incentives for customers with month-to-month contracts to switch to longer-term contracts.
Provide personalized discounts to customers with high monthly charges. Create attractive service bundles at competitive prices. Implement loyalty programs to reward long-term customers with discounts and exclusive offers.

2. Improve Customer Service and Technical Support:
Enhance the visibility and value of tech support and online security services.
Regularly check in with customers to ensure their issues are resolved satisfactorily.

3. Enhanced Communication and Engagement:
Conduct regular customer satisfaction surveys to identify and address pain points.
Use data analytics for personalized communication based on customer usage patterns.

4. Flexible Payment Options:
Encourage customers to set up auto-debit payments by offering incentives.
Provide flexible billing cycles to accommodate customer preferences.

5. Monitor and Respond to Competitor Actions:
Regularly monitor competitors' offers to ensure competitive pricing and services.
Implement win-back campaigns targeting former customers with exclusive deals or upgrades.

6. Service Quality Improvements:
Invest in improving the reliability and speed of services.
Establish feedback loops to promptly analyze and act on customer feedback.

7. Predictive Analytics for Proactive Interventions:
Use predictive analytics to identify at-risk customers early and intervene with targeted actions.
Continuously monitor and update the predictive model with new data to maintain its accuracy.
"""

