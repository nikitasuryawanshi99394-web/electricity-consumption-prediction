# ⚡ Electricity Consumption Prediction

## 📌 Project Overview

This project predicts electricity consumption using Machine Learning.

A Linear Regression model is trained on the Appliances Energy Prediction dataset and deployed as an interactive Streamlit web application.

The application allows users to enter environmental and time-related information and get an estimated electricity consumption and monthly electricity bill.

## 🎯 Objective

The main objective of this project is to predict electricity consumption based on:

- Outdoor Temperature
- Outdoor Humidity
- Indoor Temperature
- Wind Speed
- Hour
- Month

## 🤖 Machine Learning Model

- Algorithm: Linear Regression
- Type: Supervised Machine Learning
- Target Variable: Appliances
- Train-Test Split: 80% Training / 20% Testing

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit
- Pickle

## 📊 Dataset

The project uses the Appliances Energy Prediction dataset.

The dataset contains household environmental conditions and appliance energy consumption recorded at approximately 10-minute intervals.

## 🌐 Streamlit Web Application

The web application provides:

- Electricity consumption prediction
- Daily electricity unit estimation
- Monthly electricity unit estimation
- Estimated monthly electricity bill
- Model performance metrics
- Historical electricity consumption chart
- User input summary

## 💰 Electricity Bill Calculation

For this project, the electricity rate is assumed to be:

**₹8 per unit**

The predicted consumption is converted from Wh to estimated daily and monthly electricity usage.

> Note: The electricity bill shown by the application is an estimated project calculation and may differ from an actual electricity bill.

## 📈 Model Performance

The model performance is evaluated using:

- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- R² Score

The performance metrics are stored in `model_metrics.pkl`.

## 📁 Project Structure

```text
Electricity-Consumption-Prediction/
│
├── app.py
├── electricity_model_6features.pkl
├── model_metrics.pkl
├── energydata_complete.csv
├── requirement.txt
└── README.md
