# Predictive Modeling for Price Forecasting and Market Analysis_DA_Batch1

# Intro
This project as apart of training Data Analysis using python in Approach club.

# Objectives
Predict the adjusted closing price (Adj Close) using time-series forecasting or regression models.

# Dataset
The dataset contains historical price and trading volume data for Toyota stock. The file, Toyota_Data.csv, includes the following columns:
	1.	Date: Date of the record.
	2.	Adj Close: Adjusted closing price.
	3.	Close: Unadjusted closing price.
	4.	High: Highest price of the day.
	5.	Low: Lowest price of the day.
	6.	Open: Opening price of the day.
	7.	Volume: Total trading volume for the day.

# Steps
There are some steps we should follow:
	1.	Data Preprocessing such as: Convert Date column to datetime format and set it as the index, Handle missing values ,and scale features.
	2.	Generate additional features such as: Moving averages (e.g., 7-day, 30-day), Daily percentage price changes, and Rolling volatility (standard deviation over a specified window).
	3.	Split data into training and testing sets based on chronological order to prevent data leakage.
	4.	Make regression models: Random Forest, Decision Trees, or Linear Regression for price prediction using engineered features.
	5.	Evaluate models using metrics such as: Root Mean Squared Error (RMSE).
	6.	Compare model performance and select the best-performing model.


# Conclusion

This project successfully implemented predictive models for forecasting future prices and analyzing market trends using historical Toyota stock data. By regression-based models, we were able to identify patterns, trends, and key factors influencing stock price movements.

