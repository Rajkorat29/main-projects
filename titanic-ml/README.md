# Titanic Survival Prediction (Machine Learning)

This project predicts the survival of passengers on the Titanic using Machine Learning models. It includes data preprocessing, feature engineering, model training (Logistic Regression and Decision Tree), and performance evaluation.

---

## 🚀 Objective

Predict whether a passenger survived or not, using features such as:

- Passenger Class
- Sex
- Age
- Fare
- Embarked Location
- Family members aboard

---

## 📁 Dataset

- Source: [Kaggle Titanic Dataset](https://www.kaggle.com/competitions/titanic/data)
- Files used: `train.csv`, `test.csv`

---

## 📊 Features Used

- `Pclass` (Passenger Class)
- `Sex` (Encoded as 0 = female, 1 = male)
- `Age` (Filled missing with median)
- `Fare` (Kept as is)
- `Embarked` (Encoded as numeric values)
- `SibSp` + `Parch` → `FamilySize`

---

## 🧪 ML Models

### 1. Logistic Regression

- Scikit-learn's `LogisticRegression`
- Accuracy, Confusion Matrix, Classification Report

### 2. Decision Tree Classifier

- Scikit-learn's `DecisionTreeClassifier`
- Feature importance plotted using Seaborn
- Accuracy, Confusion Matrix

---

## 📈 Visualizations

- Heatmap of correlations
- Countplot of survivors by gender
- Barplot of feature importances (Decision Tree)

---

## 🧹 Preprocessing Steps

- Label Encoding for `Sex` and `Embarked`
- Missing value handling for `Age` and `Embarked`
- Feature creation: `FamilySize = SibSp + Parch`

---

## 🛠️ Libraries Used

- `pandas`, `numpy` – for data handling
- `seaborn`, `matplotlib` – for visualization
- `sklearn` – for ML modeling

---

## 📌 Results

| Model                | Accuracy |
|---------------------|----------|
| Logistic Regression | ~80%     |
| Decision Tree       | ~82%     |

---

## 📂 Project Structure

titanic-ml/
│
├── train.csv
├── test.csv
├── titanic_prediction.ipynb
├── README.md
└── requirements.txt



---

## 🧠 Learning Outcome

- Handling real-world data with missing values
- Encoding categorical data
- Training and evaluating classification models
- Visualizing model performance and importance

---

## 🔗 GitHub

[👉 View Code on GitHub](https://github.com/yourusername/titanic-ml)

---

## 📌 Status

✅ In Progress – Aim: Accuracy above 80%, better tuning and cross-validation planned.

