import streamlit as st
import plotly.express as px

# Design the front end of the app
st.header("Weather forecast for next 5 days")
place = st.text_input("Enter a city name : ",
            help="Enter a city name without spelling mistakes to get accurate data")
days = st.slider("Forecast days : ",min_value=1,max_value=5,
          help="Select for howmany days the forecast is needed ")
option = st.selectbox("Select data to view ",("Temperature Graph","Sky view"),
                      help="Select the type of view ")
st.subheader(f"{option} for next {days} days in {place.title()}")

def get_days(days):
    dates=["25-02-2025","26-02-2025","27-02-2025"]
    temperatures=[34,36,31]
    return dates,temperatures

d,t=get_days(days)

figure=px.line(x=d,y=t,labels={"x":"Dates","y":"Temperatures (C)"})
st.plotly_chart(figure)
