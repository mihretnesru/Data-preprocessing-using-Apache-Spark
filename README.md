# 🔍 Predicting Readmission Within 30 Days for Diabetic Patients

This project addresses the critical issue of predicting hospital readmission risk among diabetic patients within 30 days post-discharge. By leveraging machine learning techniques, the goal is to improve **patient outcomes** and **optimize healthcare resource allocation**. The study identifies high-risk patients using the **Diabetes 130-Hospitals Dataset**, applying advanced classification models to predict readmission likelihood.

---

## 📜 Overview

Diabetes is a chronic condition affecting millions worldwide, contributing to frequent hospitalizations and significant healthcare costs. Hospital readmissions within 30 days of discharge pose financial and operational burdens on healthcare systems. Identifying patients at risk of readmission allows for targeted interventions, improving patient care and reducing costs.

This project uses a comprehensive **machine learning pipeline** to analyze clinical data and predict 30-day readmissions. By evaluating multiple classification models, the **Random Forest** algorithm emerged as the best-performing model, providing accurate predictions while identifying key features influencing readmission risk.

---

## ✨ Key Features

1. **Comprehensive Machine Learning Pipeline**:
   - Preprocessing data to address missing values and class imbalances.
   - Balancing classes with **SMOTE (Synthetic Minority Oversampling Technique)**.

2. **Model Evaluation**:
   - Compared **Logistic Regression**, **Decision Trees**, **Random Forest**, **XGBoost**, and **CatBoost**.
   - Prioritized **Recall** and **AUC Score** to minimize false negatives and optimize healthcare resource allocation.

3. **Feature Importance Analysis**:
   - Highlighted top predictors for readmission:
     - **Number of lab procedures**
     - **Number of medications**
     - **Time spent in the hospital**

---

## 📂 Dataset

### Diabetes 130-Hospitals Dataset
- **Source**: Fairlearn Datasets
- **Description**: 10 years of clinical care data from 130 U.S. hospitals.
- **Features**: 25 variables, including patient demographics, lab results, and treatment details.
- **Target Variable**: Readmission within 30 days (`Yes` or `No`).
- **Class Imbalance**:
  - 11.16% of patients readmitted within 30 days.
  - 88.84% of patients not readmitted.

### Preprocessing Steps
1. Removed features with >80% missing data (e.g., `max_glu_serum`, `A1C_result`).
2. Dropped invalid or underrepresented entries in categorical variables (e.g., `gender`, `race`).
3. Applied **one-hot encoding** for categorical variables.
4. Balanced the dataset using **SMOTE** to mitigate class imbalance.

---

## 🔧 Methods

The project implemented a robust pipeline with the following stages:

1. **Data Splitting**:
   - Training: 60%
   - Validation: 20%
   - Testing: 20%
   - Used **stratified splitting** to preserve class proportions.

2. **Models Evaluated**:
   - **Logistic Regression**: Best suited for binary classification.
   - **Decision Trees**: Handles non-linear relationships but prone to overfitting.
   - **Random Forest**: Ensemble of decision trees offering high accuracy and robustness.
   - **XGBoost**: Gradient boosting algorithm for improved precision.
   - **CatBoost**: Handles categorical data efficiently with symmetric trees.

3. **Hyperparameter Tuning**:
   - Grid search with 5-fold cross-validation for optimal parameter selection.
   - Examples:
     - Random Forest: `n_estimators=200`, `max_depth=10`, `min_samples_split=2`.
     - XGBoost: `learning_rate=0.1`, `max_depth=7`, `n_estimators=200`.

---

## 📊 Results

### Model Performance
| Model               | Precision | Recall  | F1-Score | AUC Score |
|---------------------|-----------|---------|----------|-----------|
| Logistic Regression | 1.000     | 0.853   | 0.921    | 0.927     |
| Decision Tree       | 0.907     | 0.873   | 0.890    | 0.892     |
| Random Forest       | 0.991     | 0.877   | 0.930    | **0.936** |
| XGBoost             | 0.995     | 0.860   | 0.922    | 0.927     |
| CatBoost            | 0.999     | 0.855   | 0.921    | 0.927     |

### Selected Model: Random Forest
- **Recall**: 0.877
- **AUC Score**: 0.936
- **Why Random Forest?**
  - Balanced precision and recall.
  - Lowest false negatives, reducing missed readmission risks.

### Feature Importance
Key features identified:
1. **Number of lab procedures**.
2. **Number of medications**.
3. **Time spent in the hospital**.

![Feature Importance](path/to/feature_importance_plot.png)

---

## 🚀 How to Run the Project

### Prerequisites
- Python 3.x
- Libraries:
  - `pandas`, `numpy`, `scikit-learn`, `imbalanced-learn`, `xgboost`, `catboost`, `matplotlib`
