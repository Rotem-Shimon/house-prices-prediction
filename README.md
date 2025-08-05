# 🏠 House Price Prediction

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Processing-yellow?logo=pandas) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikit-learn) ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-red?logo=jupyter)

**Goal:** Build a regression model to predict house prices in Ames, Iowa using property attributes.  
**Best model:** Ridge Regression (**RMSE ≈ 0.15**, **R² ≈ 0.88**).  

---

## 🔹 What I Did
- Preprocessed **80+ features** (handled missing values, one-hot encoding, PCA).
- Explored correlations — **neighborhood** and **overall quality** were the strongest predictors.
- Applied **log transformation** to stabilize target distribution.
- Built and compared multiple regression models: **Linear, Ridge, KNN, Decision Tree, SGD, Bagging**.

---

## 📊 Dataset
**Source:** [Kaggle – House Prices](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)  
**Size:** 1460 training samples, 1459 test samples, 80 features.

---

## 🖼️ Key Visualizations
**Feature Correlation Heatmap:**  
![](images/heatmap_correlation.png)

**Model Performance Comparison:**  
![](images/model_rmse_comparison.png)

---

## 🛠️ Tech Stack
**Python**, **Pandas**, **Scikit-learn**, **Plotly**, **Jupyter Notebook**

---

## ▶️ How to Run
```bash
git clone https://github.com/Rotem-Shimon/house-prices-prediction.git
pip install -r src/requirements.txt
jupyter notebook House_Prices.ipynb
```

---

## 👨‍💻 Author
**Rotem Shimon** – 2nd-year CS student @ Afeka College.  
Passionate about data science & practical ML solutions.
