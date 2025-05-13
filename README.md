# 🧠 Income Prediction Using Census Data

Welcome to the **Income Prediction ML Project Assignment**!  
In this project, you will build a machine learning model to predict whether a person earns more than $50K per year using demographic and work-related attributes.

---

## 🎯 Objective

Your task is to:

- Perform **Exploratory Data Analysis (EDA)** on the "Adult Census Income" dataset.
- **Preprocess the data** to make it suitable for machine learning.
- Build and evaluate a **classification model** to predict income (`>50K` or `<=50K`).
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

## 📝 Assignment Instructions

1. **Fork this repository** to your GitHub account.
2. Perform **EDA** and **data preprocessing** in a Jupyter Notebook.
3. Build a **classification model**, evaluate its performance (accuracy, precision, recall, etc.).
4. **Save the trained model** using `pickle` or `joblib`.
5. Create a **Flask web app** that takes user input and displays the predicted income category.
6. Create a **Streamlit app** with the same functionality but using Streamlit widgets.
7. Update the `README.md` with:

   * Your project overview
   * Methodology
   * Live app links (Streamlit if possible)
   * Screenshots, etc.
9. Push all your files to your forked GitHub repo and **submit the GitHub repo link**.

---

## 📂 Folder Structure

```
income-predictor/
├── flask_app.py                # Flask app entry point
├── streamlit_app.py            # Streamlit app entry point
├── model/
│   └── model.pkl               # Trained and serialized model files
├── templates/
│   └── index.html              # HTML template for Flask form
├── static/                     # (Optional) Static files for Flask
├── notebook/
│   └── eda\_model.ipynb        # notebooks
├── requirements.txt            # List of Python dependencies
└── README.md                   # Updated with your project details
```
