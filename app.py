import streamlit as st
import pickle
import pandas as pd

# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="Electricity Consumption Prediction",
    page_icon="⚡",
    layout="wide"
)

# --------------------------------
# Load Model
# --------------------------------

with open("electricity_model_6features.pkl", "rb") as file:
    model = pickle.load(file)

# --------------------------------
# Load Model Metrics
# --------------------------------

with open("model_metrics.pkl", "rb") as file:
    metrics = pickle.load(file)

# --------------------------------
# Load Dataset for Chart
# --------------------------------

energy_data = pd.read_csv("energydata_complete.csv")

energy_data["date"] = pd.to_datetime(energy_data["date"])

energy_data["hour"] = energy_data["date"].dt.hour

# --------------------------------
# Title
# --------------------------------

st.title("⚡ Electricity Consumption Prediction")

st.write(
    "Predict electricity consumption using Machine Learning "
    "with Linear Regression."
)

st.divider()

# --------------------------------
# Sidebar
# --------------------------------

st.sidebar.title("📌 About Project")

st.sidebar.write(
    """
    This project predicts electricity consumption using
    Linear Regression.

    **Machine Learning Model**
    - Linear Regression

    **Input Features**
    - Outdoor Temperature
    - Outdoor Humidity
    - Indoor Temperature
    - Wind Speed
    - Hour
    - Month

    **Technology**
    - Python
    - Pandas
    - Scikit-learn
    - Streamlit
    - Matplotlib / Seaborn
    """
)

# --------------------------------
# User Inputs
# --------------------------------

    # --------------------------------
# User Inputs
# --------------------------------

st.subheader("🔢 Enter Input Values")

col1, col2, col3 = st.columns(3)

with col1:
    T_out = st.number_input(
        "Outdoor Temperature (°C)",
        min_value=-20.0,
        max_value=50.0,
        value=20.0,
        step=0.1,
        format="%.1f"
    )

    RH_out = st.number_input(
        "Outdoor Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=60.0,
        step=0.1,
        format="%.1f"
    )

with col2:
    T1 = st.number_input(
        "Indoor Temperature (°C)",
        min_value=10.0,
        max_value=40.0,
        value=20.0,
        step=0.1,
        format="%.1f"
    )

    Windspeed = st.number_input(
        "Wind Speed",
        min_value=0.0,
        max_value=20.0,
        value=4.0,
        step=0.1,
        format="%.1f"
    )

with col3:
    hour = st.number_input(
        "Hour",
        min_value=0,
        max_value=23,
        value=12,
        step=1
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=6,
        step=1
    )

# --------------------------------
# --------------------------------
# Prediction Button
# --------------------------------

if st.button("🔮 Predict Electricity Consumption"):

    # Create input DataFrame
    input_data = pd.DataFrame({
        "T_out": [T_out],
        "RH_out": [RH_out],
        "T1": [T1],
        "Windspeed": [Windspeed],
        "hour": [hour],
        "month": [month]
    })

    # Prediction
    prediction_wh = model.predict(input_data)[0]

    # --------------------------------
    # Consumption Calculation
    # --------------------------------

    interval_kwh = prediction_wh / 1000

    daily_units = interval_kwh * 24
    monthly_units = daily_units * 30

    rate_per_unit = 8
    monthly_bill = monthly_units * rate_per_unit

    # --------------------------------
    # Prediction Result
    # --------------------------------

    st.divider()

    st.subheader("⚡ Prediction Result")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Predicted Consumption",
            f"{prediction_wh:.2f} Wh"
        )

    with col2:
        st.metric(
            "Estimated Monthly Consumption",
            f"{monthly_units:.2f} Units"
        )

    with col3:
        st.metric(
            "Estimated Monthly Bill",
            f"₹{monthly_bill:.0f}"
        )

    st.info(
        f"💰 Electricity rate used: ₹{rate_per_unit} per unit"
    )

    # --------------------------------
    # Input Summary
    # --------------------------------

    st.subheader("📋 Input Summary")

    summary = pd.DataFrame({
        "Feature": [
            "Outdoor Temperature",
            "Outdoor Humidity",
            "Indoor Temperature",
            "Wind Speed",
            "Hour",
            "Month"
        ],
        "Value": [
            f"{T_out} °C",
            f"{RH_out} %",
            f"{T1} °C",
            Windspeed,
            hour,
            month
        ]
    })

    st.dataframe(
        summary,
        use_container_width=True,
        hide_index=True
    )    # --------------------------------
    # Bill Information
    # --------------------------------

    st.info(
        f"💰 Electricity rate used: ₹{rate_per_unit} per unit"
    )

    # --------------------------------
    

# --------------------------------
# Historical Consumption Chart
# --------------------------------

st.divider()

st.subheader("📈 Electricity Consumption by Hour")

hourly_consumption = (
    energy_data
    .groupby("hour")["Appliances"]
    .mean()
    * 6
    / 1000
)

hourly_chart = pd.DataFrame({
    "Hour": hourly_consumption.index,
    "Units": hourly_consumption.values
})

st.line_chart(
    hourly_chart,
    x="Hour",
    y="Units"
)

st.caption(
    "Average historical electricity consumption by hour "
    "based on the original energy dataset."
)

# --------------------------------
# Model Performance
# --------------------------------

st.divider()

st.subheader("📊 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "MAE",
        f"{metrics['MAE']:.2f}"
    )

with col2:
    st.metric(
        "RMSE",
        f"{metrics['RMSE']:.2f}"
    )

with col3:
    st.metric(
        "R² Score",
        f"{metrics['R2']:.2f}"
    )

st.caption(
    "Model performance is calculated using the test dataset."
)

# --------------------------------
# Footer
# --------------------------------

st.divider()

st.write(
    "⚡ Electricity Consumption Prediction | "
    "Linear Regression Machine Learning Project"
)