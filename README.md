# 🧠 Income Prediction Using Census Data

Welcome to the **Income Prediction ML Project Assignment**!  
This repository is provided as a base for your assignment where you will build a machine learning model to predict whether a person earns more than $50K per year using demographic and work-related attributes.

---

## 📌 Objective

The goal of this assignment is to:
- Perform **Exploratory Data Analysis (EDA)** on the "Adult Census Income" dataset.
- **Preprocess the data** to make it ready for machine learning.
- Train and evaluate a **classification model** to predict income class (`>50K` or `<=50K`).
- **Deploy** the model using a simple **Flask web application** where users can input values and see the prediction.

---
## 📦 Dataset Information

- Dataset Name: **Adult Census Income**
- Source: [OpenML](https://www.openml.org/d/1590)
- Load using:  
  ```python
  from sklearn.datasets import fetch_openml
  data = fetch_openml("adult", version=2, as_frame=True)
  ````

* Target: `income`
* Task: **Binary Classification**

---


## 📝 Assignment Instructions

1. **Fork this repository** into your GitHub account.
2. Complete the assignment by:
   - Performing EDA in a Jupyter notebook.
   - Preprocessing the dataset.
   - Building and evaluating a classification model.
   - Saving the model using `pickle` or `joblib`.
   - Creating a simple Flask app for deployment.
3. Add your files into the appropriate folders as per the structure below.
4. Replace this `README.md` with your own version, including:
   - Project Title and Objective
   - Dataset and Technologies used
   - Methodology
   -Screenshots/Demo

---

## 📂 Expected Folder Structure

```

income-predictor/
├── app.py                       # Flask app for web deployment
├── model/
│   └── pkl files         # Trained and serialized model
├── templates/
│   └── index.html               # HTML page for the web form
├── static/                      # For CSS/images (optional)
├── notebook/
│   └── eda\_model\_training.ipynb # notebooks
├── requirements.txt             # List of Python dependencies
└── README.md                    # Your updated readme with project details

````
