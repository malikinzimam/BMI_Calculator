import streamlit as st

st.title("📊 BMI Calculator")

weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
height_feet = st.number_input("Enter your height (feet):", min_value=1.0, format="%.2f")

height_meters = height_feet * 0.3048  

if st.button("🔢 Calculate"):
    if height_meters > 0:
        bmi = weight / (height_meters ** 2)
        st.write(f"### Your BMI: {bmi:.2f}")

        if bmi < 18.5:
            st.warning("📉 You are underweight. Consider a healthy diet.")
        elif 18.5 <= bmi < 24.9:
            st.success("✅ Your weight is normal! Keep maintaining it.")
        elif 25 <= bmi < 29.9:
            st.info("⚠️ You are overweight. Focus on exercise.")
        else:
            st.error("🚨 You are obese! Pay attention to diet and exercise.")
    else:
        st.error("❌ Please enter a valid height!")

st.sidebar.header("📌 BMI Categories")
st.sidebar.markdown("""
- **Below 18.5** → Underweight  
- **18.5 - 24.9** → Normal weight  
- **25 - 29.9** → Overweight  
- **30 or above** → Obese  
""")
