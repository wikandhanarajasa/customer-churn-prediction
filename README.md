**Customer Churn Prediction for Interconnect**

**Introduction**

Interconnect is a telecommunications company specializing in landline and internet services. Additionally, it offers services like Internet Security, Tech Support, Cloud Storage, Online Backup, and Streaming Services. To maintain profitability, Interconnect aims to predict customer churn rates accurately. By identifying potential churn clients, the company can offer promotional codes and special packages to retain these customers. The marketing team has gathered necessary data, including client information, contract details, and current services.

**Goal**

The goals of this project are:

1. Develop a machine learning model to predict client churn with an AUC-ROC score of at least 0.88.
2. Utilize the F1 score as an additional evaluation metric.
3. Perform statistical calculations and visualize findings.
4. Compare the behavior of telephone and internet users.

**Steps**

The steps of this project are:

1. Load and study the general information of the data.
2. Explore and analyze the data.
3. Prepare the data by addressing anomalies and checking class balance.
4. Create and train the machine learning model, aiming for an AUC-ROC score above or equal to 0.88.
5. Draw conclusions from the analysis.

**Data List**

1. Contract Data
   
customerID: Unique identifier for each customer.
BeginDate: Contract start date.
EndDate: Contract end date (NaT for active customers).
Type: Contract type (e.g., month-to-month, one year, two years).
PaperlessBilling: Indicator for paperless billing.
PaymentMethod: Chosen payment method.
MonthlyCharges: Monthly charges for services.
TotalCharges: Total charges over the contract period.

2. Personal Data
   
customerID: Unique identifier for each customer.
gender: Customer's gender.
SeniorCitizen: Indicator for senior citizen status (1 for yes, 0 for no).
Partner: Indicator for having a partner or spouse.
Dependents: Indicator for having dependents.

3. Internet Data
   
customerID: Unique identifier for each customer.
InternetService: Type of internet service subscribed.
OnlineSecurity: Subscription to online security service.
OnlineBackup: Subscription to online backup service.
DeviceProtection: Subscription to device protection service.
TechSupport: Access to technical support.
StreamingTV: Subscription to TV streaming service.
StreamingMovies: Subscription to movie streaming service.

4. Phone Data
   
customerID: Unique identifier for each customer.
MultipleLines: Indicator for multiple phone lines.

**Exploratory Data Analysis**

**Findings**

1. Active customers generally have similar monthly spending but higher total spending compared to churned customers.
2. Churned customers tend to have higher monthly charges.
3. Monthly contract renewals correlate with higher churn rates.
4. Manual payment methods are more common among churned customers.
5. Demographic factors such as gender, senior citizen status, partnership, dependents, and phone line type do not significantly affect churn rates.
6. Fiber optic users are more likely to churn compared to DSL users.
7. Lack of technical support and online security services correlate with higher churn rates.

**Machine Learning Model Development**

**Feature Engineering Steps**

1. Merge All Data into One Dataset: Combine personal data, contract data, and internet data into a single dataset using customerID as the key.
2. Drop Unnecessary Columns: Remove columns that do not provide useful information for prediction, such as customerID, BeginDate, and EndDate.
3. One-Hot Encoding: Convert categorical variables into binary columns for machine learning algorithms.
4. Split the Data into Features and Target: Separate the dataset into predictor variables and the target variable (churn).
5. Split the Data into Train and Test Sets: Divide the data into training and testing sets to evaluate model performance.

**Models Tested**

1. Logistic Regression
2. Random Forest Classifier
3. Decision Tree Classifier
4. XGBoost Classifier
5. LightGBM Classifier
6. CatBoost Classifier
7. Gradient Boosting Classifier

**Results**

Model Performance

The Gradient Boosting Classifier achieved the highest ROC AUC score, indicating good discrimination between churn and non-churn customers. However, the F1 score suggests a need for a better balance between precision and recall.

Gradient Boosting Classifier:
ROC AUC: 85.88%
F1 Score: 57.04%

**Difficulties Encountered**

1. Imbalanced Data: The data distribution of churn customers is imbalanced, making it difficult to achieve the target ROC AUC score of 0.88.
2. Hyperparameter Tuning: Finding the right hyperparameters and machine learning model required extensive trial and error.
3. One-Hot Encoding: Some issues during one-hot encoding led to re-running the machine learning models.

**Summary**

The project successfully developed a machine learning model to predict customer churn for Interconnect, achieving an AUC-ROC score of 85.88% with the Gradient Boosting Classifier. Although this did not meet the goal of 0.88, it still represents a strong performance. The analysis revealed that churned customers typically have higher monthly charges and that factors such as contract type, payment method, and lack of technical support or online security services contribute to churn. These insights can help Interconnect in strategizing retention efforts and improving customer satisfaction.

**Recommendations to Treat Potential Churn Customers**

1. Targeted Promotions and Discounts:

Offer incentives for customers with month-to-month contracts to switch to longer-term contracts.
Provide personalized discounts to customers with high monthly charges.
Create attractive service bundles at competitive prices.
Implement loyalty programs to reward long-term customers with discounts and exclusive offers.

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
