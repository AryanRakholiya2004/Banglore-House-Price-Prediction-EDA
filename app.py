import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('house_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load label encoders
with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

# App title
st.title("🏠 House Price Prediction App (Bengaluru)")

# Input form
with st.form("input_form"):
    st.subheader("Enter House Details")

    area_type = st.selectbox("Area Type", label_encoders['area_type'].classes_)
    location = st.selectbox("Location", label_encoders['location'].classes_)
    total_sqft = st.number_input("Total Sqft", min_value=100.0, max_value=10000.0, value=1000.0)
    bedrooms = st.slider("Bedrooms (BHK)", min_value=1, max_value=10, value=2)
    is_hall_kitchen = st.checkbox("Includes Hall + Kitchen", value=True)

    submitted = st.form_submit_button("Predict Price")

# Prediction logic
if submitted:
    try:
        input_data = {
            'area_type': area_type,
            'location': location,
            'total_sqft': total_sqft,
            'Bedrooms': bedrooms,
            'is_hallKitchen': is_hall_kitchen
        }

        df_input = pd.DataFrame([input_data])

        # Encode categorical columns
        for col in df_input.select_dtypes(include='object').columns:
            le = label_encoders.get(col)
            if le:
                if df_input[col].values[0] in le.classes_:
                    df_input[col] = le.transform(df_input[col])
                else:
                    st.error(f"❌ '{df_input[col].values[0]}' is an unknown value for '{col}'")
                    st.stop()

        # Predict
        prediction = model.predict(df_input)
        st.success(f"💰 Estimated Price: ₹{prediction[0]:,.2f}")

    except Exception as e:
        st.error(f"An error occurred: {e}")
