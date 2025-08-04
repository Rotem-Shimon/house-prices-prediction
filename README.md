# 🏠 House Prices Prediction  
> **Academic Project** – Developed as part of the *Machine Learning* course at **Afeka Academic College of Engineering**.  
> Goal: Predict residential house prices using machine learning techniques.  

## 📌 Project Overview  
This project aims to predict house sale prices based on multiple property features (size, quality, neighborhood, etc.).  
It demonstrates the full pipeline of a machine learning project:  
- **Data preprocessing**: Cleaning, handling missing values, encoding categorical variables.  
- **Exploratory Data Analysis (EDA)**: Understanding the most important factors affecting house prices.  
- **Baseline modeling**: Initial prediction using **Linear Regression**.  
- **Evaluation**: Assessing model performance with regression metrics (R², RMSE).  

## 📊 Dataset  
- **Source**: [Kaggle – House Prices: Advanced Regression Techniques](https://www.kaggle.com/c/house-prices-advanced-regression-techniques)  
- **Files used**:  
  - data/train.csv – Training dataset with features + target (SalePrice)  
  - data/test.csv – Test dataset for evaluation and predictions  
- **Features**: Property size, type, year built, quality, and many categorical variables.  

## 🚀 Current Features  
- **Baseline Model**: Linear Regression  
- **Data Preprocessing**:  
  - Filling missing values (median for numeric data)  
  - One-hot encoding for categorical variables  
- **Basic Evaluation**: R² score and RMSE  

## 📷 Visual Examples  
### Distribution of Sale Price  
![](images/distribution_sale_price.png)  

### Feature Correlation Heatmap  
![](images/heatmap_correlation.png)  

### Model RMSE Comparison (Train vs Validation)  
![](images/model_rmse_comparison.png)  

### Model Metrics Comparison (MSE, RMSE, R²)  
![](images/model_metrics_comparison.png)  

## 🔮 Planned Improvements  
- Add advanced models: Random Forest, XGBoost, Gradient Boosting  
- Model comparison with cross-validation  
- Hyperparameter tuning  
- Feature importance analysis (SHAP, permutation)  
- Residual analysis and prediction vs actual plots  
- Deployment via a simple web app  

## 📚 References  
- Kaggle – House Prices: Advanced Regression Techniques  
- Hands-On Machine Learning with Scikit-Learn, Keras & TensorFlow – Aurélien Géron  
- Scikit-learn Documentation  
- XGBoost Documentation  

## 🛠️ Project Structure  
house-prices-prediction/  
├─ data/                   Training & test datasets  
│   ├─ train.csv  
│   └─ test.csv  
├─ images/                 Saved visualizations  
│   ├─ distribution_sale_price.png  
│   ├─ heatmap_correlation.png  
│   ├─ model_rmse_comparison.png  
│   └─ model_metrics_comparison.png  
├─ House_Prices.ipynb      Main Jupyter Notebook  
├─ functions.py            Helper functions  
├─ requirements.txt        Python dependencies  
└─ README.md               Project documentation  

## ⚡ How to Run  
1. Clone repository:  
   git clone https://github.com/Rotem-Shimon/house-prices-prediction.git  
2. Install dependencies:  
   pip install -r requirements.txt  
3. Open Notebook:  
   jupyter notebook House_Prices.ipynb  
4. Run all cells to reproduce analysis and results.  

## 👨‍🎓 Author  
**Rotem Shimon**  
2nd-year Computer Science student at Afeka Academic College of Engineering.  
