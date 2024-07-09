#**Customer Churn Prediction**

Machine learning project to predict customer churn using Python

**Introduction**

Interconnect is a telecommunications company that focuses on landline and internet services. Besides these two core services, it also offers additional services such as Internet Security, Tech Support, Cloud Storage, Online Backup, and Streaming Services.

To ensure the business remains profitable, the company has decided to conduct a deeper analysis of their customers by forecasting their churn rate. Potential churn clients will be offered promotion codes and special packages to retain their usage of the services.

The marketing team has gathered the necessary data for this analysis, including client information, contract details, and current service usage.

**Goal**

The goals of this project are as follows:

1. Develop a robust machine learning model to predict client churn with an AUC-ROC score of 0.88 or higher.
2. Evaluate the model using the F1 score as an additional metric.
3. Perform statistical calculations and visualize the findings.
4. Compare the behavior of telephone and internet users.

**Steps**

The steps for this project are outlined below:

1. Load and Inspect Data: Load the data and examine the general information.
2. Data Exploration and Analysis: Explore and analyze the data to understand patterns and insights.
3. Data Preparation: Address any anomalies found and check for class balance.
4. Model Development and Training: Develop a machine learning model and train it, ensuring the AUC-ROC score is maintained at or above 0.88.
5. Conclusion and Reporting: Draw conclusions from the analysis and modeling results, and document the findings.

**Results**

The performance of various machine learning models for predicting customer churn was evaluated based on ROC AUC, precision, and F1 scores. The Gradient Boosting Classifier emerged as the top performer with an ROC AUC of 85.88% and an F1 score of 57.04% on the test set. The CatBoost Classifier followed closely with an ROC AUC of 85.85% and an F1 score of 56.74%.

The Gradient Boosting Classifier achieved a strong ROC AUC score of 85.88%, indicating good discrimination between churn and non-churn customers. However, its F1 score of 57.04% suggests that while it performs well overall, its balance between precision and recall needs improvement. This performance is particularly notable given the imbalanced dataset, where only 1 in 4 customers are churners.

**Conclusion**

This project successfully developed and evaluated machine learning models to predict customer churn for Interconnect. The Gradient Boosting Classifier was identified as the most effective model based on its ROC AUC score. Despite the challenges posed by an imbalanced dataset, the model demonstrated strong potential for identifying at-risk customers, allowing the marketing team to target these customers with retention strategies.

Future work could involve further tuning of the models, exploring additional features, and implementing techniques to handle the class imbalance more effectively.
