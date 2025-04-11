# Banglore-House-Price-Prediction-EDA

# 🏠 Bengaluru House Price Prediction App

This is an end-to-end **Machine Learning project** built by a **Data Science student** to predict housing prices in **Bengaluru, India** based on various property features. The project is deployed using **Streamlit**, allowing users to interact with the model and estimate property prices in real-time.

> 🎯 This project is part of my Data Science portfolio and showcases the complete lifecycle of a machine learning problem — from data preprocessing to model deployment.

---

## Previews

#### Streamlit App Preview
![image](https://github.com/user-attachments/assets/00a95990-8403-4bf4-a114-db7d0e9cac7b)

- You can try this with below link
🔗 <a href="">Banglore House Price Prediction</a>

---

## 📌 Project Objective

The objective of this project is to:
- Predict the price of residential properties in Bengaluru.
- Build a machine learning model using real-world housing data.
- Handle categorical data and anomalies in the dataset.
- Deploy a user-friendly interface using Streamlit for real-time predictions.

---

## 📊 Dataset Overview

The dataset contains real estate listings in Bengaluru with the following key features:
- `area_type`
- `location`
- `size` (BHK information)
- `total_sqft`
- `bath` (bathrooms)
- `price` (target variable in lakhs)

---

## 📈 Key Performance Indicators (KPIs)

| KPI | Description |
|-----|-------------|
| 🔍 Data Cleaning | Converted `size` column to extract number of bedrooms |
| 📐 Feature Engineering | Created `is_hallKitchen` binary feature |
| 🧹 Missing Data Handling | Dropped or handled null values appropriately |
| 🏷️ Label Encoding | Encoded `area_type` and `location` using `LabelEncoder` |
| 📊 Feature Selection | Removed irrelevant or low-variance features |
| 🧠 Model Training | Trained `RandomForestRegressor` with hyperparameter tuning using `GridSearchCV` |
| 📤 Model Export | Saved trained model and encoders using `pickle` |
| 🌐 Streamlit UI | Developed interactive frontend to collect input and display predictions |

---

## 🧩 Problems Faced & Solutions

| Problem | Solution |
|--------|----------|
| 🚫 Non-numeric input (like "2 BHK") in `size` column | Extracted numeric part to form `Bedrooms` column |
| 🌀 Categorical values not seen during prediction | Used `LabelEncoder` and handled unseen labels gracefully in Streamlit |
| 🧮 Inconsistent sqft entries (e.g., ranges like "1200-1400") | Handled and cleaned to use average or removed |
| 🔁 Model failed during GridSearch | Root cause: non-numeric columns not properly encoded. Fixed with label encoding. |
| ❌ ValueError: could not convert string to float | Fixed by identifying columns that needed encoding before training |

---

## 📦 Libraries & Tools Used

- `pandas` — Data manipulation
- `numpy` — Numerical operations
- `matplotlib` & `seaborn` — Visualization
- `scikit-learn` — Machine learning and preprocessing
- `pickle` — Model serialization
- `Streamlit` — Web app deployment

---

## 📊 DataSet
- <a href="https://github.com/AryanRakholiya2004/Banglore-House-Price-Prediction-EDA/blob/main/Bengaluru_House_Data.csv">Bengaluru_House_Data.csv</a>

---

## 🧠 Skills Developed

- End-to-end ML pipeline design
- Data cleaning & preprocessing techniques
- Feature engineering & selection
- Model training, evaluation & tuning
- Serialization with `pickle`
- Web app development using Streamlit
- Debugging and error-handling for real-world datasets
- Working with categorical data & encoders
- Building user-interactive data science projects

---

## 🖥️ How to Run This App Locally

```bash
git clone https://github.com/yourusername/bangalore-house-price-predictor.git
cd bangalore-house-price-predictor
pip install -r requirements.txt
streamlit run app.py
```
