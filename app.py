import streamlit as st
import pandas as pd
import joblib

# ========================== PAGE CONFIG ==========================
st.set_page_config(page_title="Global Supply Chain Late Delivery Predictor", layout="wide")

st.title("🚛 Global Supply Chain Late Delivery Risk Prediction")
st.markdown("**End-to-End Python Project** - **Machine Learning**")

st.markdown("---")

# Load model and encoders
@st.cache_resource
def load_artifacts():
    model = joblib.load("models/best_model_decision_tree.pkl")
    encoders = joblib.load("models/label_encoders.pkl")
    return model, encoders

model, encoders = load_artifacts()

# ========================== PROJECT OVERVIEW ==========================
st.header("Project Overview")

st.write("""
This end-to-end **Supply Chain Late Delivery Risk Prediction** project aims to predict whether an order will be delivered **late** (1) or **on time** (0) using historical shipping data from the DataCo Supply Chain dataset.
""")

st.markdown("""
### Key Highlights:
- **Best Performing Model**: Decision Tree (max_depth=8) with **ROC-AUC = 0.857**
- Outperformed XGBoost (0.850), Random Forest (0.836), and Logistic Regression (0.745)
- Successfully handled class imbalance (~54.8% Late deliveries)
- Built with a strong focus on interpretability and low overfitting
""")

st.markdown("""
### What Was Done:
- Comprehensive Exploratory Data Analysis (EDA)  
- Feature Engineering (Label Encoding + careful preprocessing)  
- Multiple model training and evaluation  
- Model selection based on ROC-AUC and generalization  
- Live prediction interface  
- Interactive Power BI dashboard for business insights  

### Business Value:
Accurate prediction of late deliveries enables proactive decision-making — such as choosing better shipping modes, flagging high-risk orders, and improving overall customer satisfaction and operational efficiency.
""")

# ========================== DATASET OVERVIEW ==========================
st.header("📊 Dataset Overview")
df = pd.read_csv("data/processed/Model_df.csv")

c1, c2, c3 = st.columns(3)
c1.metric("Total Orders", f"{len(df):,}")
c2.metric("Late Delivery Rate", f"{df['Late_delivery_risk'].mean():.1%}")
c3.metric("Features", len(df.columns)-1)

st.dataframe(df.head(8), use_container_width=True)
st.markdown("---")

# ========================== EDA ==========================
st.header("📈 Exploratory Data Analysis")

col1, col2 = st.columns(2)
with col1:
    import plotly.express as px
    fig1 = px.histogram(df, x="Shipping_mode", color="Late_delivery_risk", barmode="group",
                        title="Late Deliveries by Shipping Mode")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    fig2 = px.box(df, x="Late_delivery_risk", y="store_delay_rate",
                  title="Store Delay Rate vs Late Risk")
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")

# ========================== FEATURE ENGINEERING ==========================
st.header("🔧 Feature Engineering")
st.markdown("""
- Dropped `Order_id`  
- Label encoded: `Shipping_mode`, `Order_status`, `Order_state`, `Order_city`, `Payment_method`  
- Stratified 80/20 train-test split
""")
st.markdown("---")

# ========================== MODELLING RESULTS ==========================
st.header("🤖 Modelling Results")
st.write("**Winner: Decision Tree** — ROC-AUC = **0.857**")

st.image("plots/ROC_curve_models.png", caption="ROC Curves - All Models")

st.subheader("Model Comparison")

comparison = pd.DataFrame({
    "Model": ["Logistic Regression", "Decision Tree", "Random Forest", "XGBoost"],
    "ROC-AUC": [0.745, 0.857, 0.836, 0.850]
})

# Sort so best model comes first
comparison = comparison.sort_values(by="ROC-AUC", ascending=False).reset_index(drop=True)

st.dataframe(
    comparison.style
        .apply(lambda s: ['background-color: #FFD700; color: black; font-weight: bold' 
                         if s.name == 0 else '' for _ in s], axis=1)   # highlight first row
        .format({"ROC-AUC": "{:.4f}"})
        .bar(subset=['ROC-AUC'], color='#FFD700', width=80),
    use_container_width=True,
    hide_index=True
)

st.success("✅ Decision Tree selected as the Winner Model (Highest ROC-AUC = 0.857)")

st.markdown("---")

# ========================== LIVE PREDICTION (FIXED) ==========================
st.header("🔮 Live Late Delivery Prediction")
st.write("Enter order details below to get instant prediction from the **Decision Tree model**.")

col1, col2 = st.columns(2)

with col1:
    shipping_mode = st.selectbox("Shipping Mode", ["Standard Class", "First Class", "Second Class", "Same Day"])
    days_for_shipment = st.slider("Days for Shipment", 0, 4, value=2)
    payment_method = st.selectbox("Payment Method", ["DEBIT", "TRANSFER", "CASH", "PAYMENT"])

with col2:
    order_status = st.selectbox("Order Status", ["COMPLETE", "PENDING", "PROCESSING", "CLOSED", "CANCELED", "ON_HOLD"])
    store_delay_rate = st.slider("Store Delay Rate", 0.0, 1.0, value=0.5, step=0.01)
    order_state = st.text_input("Order State", "Maharashtra")
    order_city = st.text_input("Order City", "Pune")

if st.button("🚀 Predict Late Delivery Risk", type="primary"):
    # Create DataFrame with EXACT same columns and order as training
    input_data = pd.DataFrame({
        "Shipping_mode": [shipping_mode],
        "Days_for_shipment": [days_for_shipment],
        "Order_status": [order_status],
        "Order_state": [order_state],
        "Order_city": [order_city],
        "Payment_method": [payment_method],
        "store_delay_rate": [store_delay_rate]
    })

    # Apply label encoding safely
    for col, le in encoders.items():
        if col in input_data.columns:
            try:
                input_data[col] = le.transform(input_data[col])
            except ValueError:
                input_data[col] = le.transform([le.classes_[0]])[0]   # fallback

    # CRITICAL FIX: Reorder columns exactly as the model expects
    # This prevents the "feature names must be in the same order" error
    training_columns = ['Shipping_mode', 'Days_for_shipment', 'Order_status', 
                        'Order_state', 'Order_city', 'Payment_method', 'store_delay_rate']
    
    input_data = input_data[training_columns]

    # Make prediction
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ **HIGH RISK** of Late Delivery  \nProbability: **{probability:.1%}**")
    else:
        st.success(f"✅ **LOW RISK** — Likely On Time  \nProbability of Late: **{probability:.1%}**")

    st.caption(f"Raw probability: {probability:.4f}")

st.markdown("---")

# ========================== POWER BI SECTION ==========================
st.header("📈 Power BI Dashboard")
st.write("Download the full interactive Power BI report (.pbix)")

col1, col2 = st.columns([3,1])
with col1:
    st.image("dashboards/screenshots/overview.png", caption="Power BI Overview")
    st.image("dashboards/screenshots/product_analysis.png", caption="Product Analysis")
    st.image("dashboards/screenshots/shipping_analysis.png", caption="Shipping Analysis")
with col2:
    with open("dashboards/supplychain.pbix", "rb") as f:
        st.download_button(
            label="⬇️ Download supplychain.pbix",
            data=f,
            file_name="supplychain.pbix",
            mime="application/octet-stream"
        )

# Footer
st.caption("Built with ❤️ using Streamlit | End-to-End Data Science Project")