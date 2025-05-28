# 🧠 Income Prediction Using Census Data

Welcome to the **Income Prediction ML Project Assignment**!  
This is a web application that predicts whether a person earns more or less than $50K annually based on features like age, education, capital gain/loss, and marital status. The application uses a trained machine learning model and offers both a Flask-based web interface and a Streamlit interface for interaction.

---

🧠 Model Description: Model: A classification model (likely Logistic Regression, Random Forest, etc.) stored as classification_model.pkl

Scaler: StandardScaler or similar object saved as scaler.pkl

Target: Predict income

---

## 🎯 Objective


- Deploy the model using both:
  - A **Flask web application**
  - A **Streamlit app**
---

## 📦 Dataset Information

- **Dataset Name:** Adult Census Income
- **Source:** [OpenML](https://www.openml.org/d/1590)
- **Load using:**  
  ```python
  from sklearn.datasets import fetch_openml
  data = fetch_openml("adult", version=2, as_frame=True)
  ````

* **Target column:** `income`
* **Task type:** Binary Classification (`>50K` or `<=50K`)

---

🛠 Features:

Categorical to numerical feature mapping

Log-transform on age

Standardization on selected numeric columns

Manual mapping for education and sex

---

Two user interfaces:

Flask Web Interface

Streamlit UI

---

![image](https://github.com/user-attachments/assets/c367b1b1-d928-471e-b4d3-11e8de57886b)

---

![image](https://github.com/user-attachments/assets/94f8a728-2c7d-457e-9e1f-204eeef12c2a)



