import streamlit as st
import random


# Page config (optional but makes it look better)
st.set_page_config(page_title="OTP Generator", page_icon="🔐")

st.title("🔐 OTP Generator by Manish")

# Session_state to store OTP
if "otp" not in st.session_state:#Storing the data as streamlit reloads the page everytime we click a button 
    st.session_state.otp = None #if the otp doesnot exists it will be set to none 

# Generate OTP button
if st.button("Generate OTP"):#if the button is pressed
    st.session_state.otp = random.randint(1000, 9999)  # Generating a random 4-digit OTP
    st.success("OTP Generated Successfully!")
# Display OTP
if st.session_state.otp:#if the otp is not "none"
    st.code(st.session_state.otp, language="text")#Display the otp in code style box
    st.warning("⚠️ Please do not share your OTP with anyone.")#printing a warning message in yellow box

    # Optional: Add verify section
    user_input = st.text_input("Enter OTP to Verify")#printing a text to take input from the user the otp

    if st.button("Verify OTP"):#if he clicks the verify otp button
        if user_input == str(st.session_state.otp):#checking the user input with the random generated otp
            st.success("✅ OTP Verified Successfully!")
        else:
            st.error("❌ Incorrect OTP. Try again.")

