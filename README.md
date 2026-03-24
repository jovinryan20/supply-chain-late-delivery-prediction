# 🚛 Global Supply Chain Late Delivery Risk Prediction

**End-to-End Machine Learning Project**  
**Best Model:** Decision Tree (ROC-AUC = **0.857**)

Predict whether an order will be delivered late using the DataCo Supply Chain dataset.

![Project Banner](https://via.placeholder.com/1200x300/1e3a8a/ffffff?text=Supply+Chain+Late+Delivery+Prediction)

---

## 📊 Project Overview

This project aims to **predict late delivery risk** in the supply chain using historical order and shipping data.  

After extensive EDA, feature engineering, and model evaluation, the **Decision Tree** emerged as the best performing model with an impressive **ROC-AUC of 0.857**, outperforming XGBoost, Random Forest, and Logistic Regression.

### Key Achievements
- Handled class imbalance (~54.8% late deliveries)
- Built an interactive **Streamlit web app** with live predictions
- Created a comprehensive **Power BI dashboard** for business insights
- Focused on model interpretability and low overfitting

---

## 📈 Exploratory Data Analysis

### Key Insights from the Data

| Plot | Description |
|------|-------------|
| **Shipping Mode Impact** | Does shipping mode significantly affect late delivery risk? |
| **Late Risk by Region** | Regional analysis of delay patterns |
| **Risk of Delay by Week** | Weekly trends in late deliveries |
| **Model Performance** | ROC curves comparing all models |

<div align="center">

**Does Shipping Mode Affect Late Delivery?**  
<img src="plots/does_shipping_affect.png" width="48%" alt="Shipping Mode Impact">

**Late Risk by Region**  
<img src="plots/late_risk_byregion.png" width="48%" alt="Late Risk by Region">

**Risk of Delay by Week**  
<img src="plots/riskof_delay_byweek.png" width="48%" alt="Risk of Delay by Week">

**Model Comparison - ROC Curves**  
<img src="plots/ROC_curve_models.png" width="48%" alt="ROC Curve Models">

</div>

---

## 🤖 Modelling Results

**Winner Model: Decision Tree** with **ROC-AUC = 0.857**

### Model Comparison

| Model                | ROC-AUC   | Status      |
|----------------------|-----------|-------------|
| Decision Tree        | **0.857** | 🏆 **Winner** |
| XGBoost              | 0.850     | Strong      |
| Random Forest        | 0.836     | Good        |
| Logistic Regression  | 0.745     | Baseline    |

The Decision Tree was selected for its excellent performance, simplicity, and low overfitting.

---

## 📈 Power BI Dashboard

Interactive business dashboard built in Power BI for deep visual analysis.

**Download the full interactive dashboard:**

[![Download Power BI Dashboard](https://img.shields.io/badge/Download-.pbix-FF0000?style=for-the-badge&logo=powerbi&logoColor=white)](dashboards/supplychain.pbix)

**Key Dashboard Features:**
- Late delivery risk overview
- Shipping mode and store delay analysis
- Regional and weekly performance insights
- Interactive slicers and drill-downs

*(Open with free Power BI Desktop for full interactivity)*

---

## 🌐 Live Demo

Try the **Live Prediction App** built with Streamlit:

[![Streamlit App](https://img.shields.io/badge/Launch_Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://your-app-name.streamlit.app)

**Features:**
- Real-time late delivery predictions using the Decision Tree model
- Interactive input form
- Instant probability scores

---

## 🛠️ Tech Stack

- **Python** | **Pandas** | **Scikit-learn** | **Joblib**
- **Streamlit** (Interactive Web App)
- **Plotly** & **Matplotlib** (Visualizations)
- **XGBoost**, **Random Forest**, **Decision Tree**, **Logistic Regression** (Modelling) 
- **Power BI** (Business Dashboard)
- **GitHub** (Version Control & Showcase)

---

## 📁 Project Structure

supply-chain-late-delivery-prediction/

├── data/                  # Raw and processed datasets

├── models/                # Trained models (.pkl)

├── plots/                 # EDA and model plots

├── dashboards/            # Power BI .pbix file

├── deployment/            # Streamlit app.py

├── notebooks/             # Jupyter notebooks

├── src/                   # Reusable Python scripts

├── README.md

├── requirements.txt

└── app.py


## 🚀 How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/yourusername/supply-chain-late-delivery-prediction.git
```

2. Install dependencies:Bashpip 
 ```bash
install -r requirements.txt
```
3. Run the Streamlit app:
 ```bash
streamlit run app.py
```

---

<div align="center">

⭐ **If you found this useful, consider giving it a star!** ⭐

---

*Made with 💖 by **Jovin Ryan Samuel***

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/jovinryan20/)

</div>