import streamlit as st


# Design the front end of the app
st.header("Weather forecast for next 5 days")
place = st.text_input("Enter a city name : ",
            help="Enter a city name without spelling mistakes to get accurate data")
days = st.slider("Forecast days : ",min_value=1,max_value=5,
          help="Select for howmany days the forecast is needed ")
option = st.selectbox("Select data to view ",("Temperature Graph","Sky view"),
                      help="Select the type of view ")
st.subheader(f"{option} for next {days} days in {place.title()}")

