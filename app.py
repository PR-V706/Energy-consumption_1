import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(
    page_title="HVAC Energy Optimisation",
    page_icon="❄️",
    layout="wide"
)

# -----------------------------
# TITLE
# -----------------------------

st.title("❄️ AI-Based HVAC Energy Optimisation")
st.write("Smart Air Conditioning Energy Monitoring Dashboard")

# -----------------------------
# SIDEBAR - SENSOR INPUT
# -----------------------------

st.sidebar.header("Sensor Inputs")

temperature = st.slider(
    "Room Temperature (°C)",
    16, 40, 29
)

humidity = st.slider(
    "Humidity (%)",
    20, 90, 65
)

power = st.slider(
    "AC Power (kW)",
    0.1, 5.0, 1.5
)

setpoint = st.slider(
    "AC Setpoint (°C)",
    16, 30, 24
)

# Sample calculation
energy = power * 0.25

# -----------------------------
# LIVE MONITORING
# -----------------------------

st.subheader("📊 Live Monitoring")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Temperature",
    f"{temperature} °C"
)

col2.metric(
    "Humidity",
    f"{humidity} %"
)

col3.metric(
    "AC Power",
    f"{power:.2f} kW"
)

col4.metric(
    "Energy / 15 min",
    f"{energy:.3f} kWh"
)

st.divider()

# -----------------------------
# SAMPLE ENERGY DATA
# -----------------------------

st.subheader("📈 Energy Consumption")

times = [
    datetime.now() - timedelta(minutes=15 * i)
    for i in range(11, -1, -1)
]

energy_values = [
    0.28, 0.31, 0.35, 0.30,
    0.38, 0.42, 0.40, 0.36,
    0.33, 0.35, 0.37, energy
]

df = pd.DataFrame({
    "Time": times,
    "Energy (kWh)": energy_values
})

fig = px.line(
    df,
    x="Time",
    y="Energy (kWh)",
    markers=True,
    title="Energy Consumption Over Time"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# ROOM CONDITIONS
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("🌡️ Room Conditions")

    conditions = pd.DataFrame({
        "Parameter": [
            "Temperature",
            "Humidity",
            "AC Setpoint"
        ],

        "Value": [
            f"{temperature} °C",
            f"{humidity} %",
            f"{setpoint} °C"
        ]
    })

    st.dataframe(
        conditions,
        hide_index=True,
        use_container_width=True
    )

# -----------------------------
# RECOMMENDATION
# -----------------------------

with col2:

    st.subheader("💡 Energy Recommendation")

    if temperature > setpoint + 3:

        st.warning(
            "Room temperature is considerably "
            "above the AC setpoint. "
            "Check cooling performance."
        )

    elif humidity > 70:

        st.info(
            "Humidity is relatively high. "
            "Monitor indoor comfort."
        )

    else:

        st.success(
            "Current room conditions are "
            "within the monitoring range."
        )

# -----------------------------
# PROJECT STATUS
# -----------------------------

st.divider()

st.subheader("🚀 Project Development Status")

st.write("✅ Dashboard prototype")
st.write("🔄 Sensor data integration - Upcoming")
st.write("🔄 AI energy prediction - Upcoming")
st.write("🔄 Energy optimisation model - Upcoming")
st.write("🔄 ESP32 hardware integration - Upcoming")

st.caption(
    "Prototype dashboard using sample data. "
    "AI prediction and live sensor integration "
    "will be added in the next development stage."
)