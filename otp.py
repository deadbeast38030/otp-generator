import streamlit as st #helps to create web apps using python
import random          #build in module to generate random numbers 
from plyer import notification #to get the notification feature from plyer

st.title("OTP Generator by Manish ") #big heading of the web page 
if st.button("Generate OTP"):        #to create the button on the web page
    otp=random.randint(1000,9999)    #to generate the random number
    st.success(f"Your OTP is : {otp}")  #showing the automated green success message on the screen
    st.code(otp,language = "text")    #display the otp in code style box

    notification.notify(              #the notification part
        title = "Your OTP",           #notification heading
        message = f"Your OTP is {otp}, \n Please donot share your OTP with anyone", #the notification body text
        app_name="OTP Generator",   #name of the app
    )

