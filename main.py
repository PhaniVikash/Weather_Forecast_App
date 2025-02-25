import streamlit as st
import plotly.express as px

from backend import get_data

# Design the front end of the app
st.header("Weather forecast for next 5 days with Time interval of 3 hrs")
place = st.text_input("Enter a city name : ",
            help="Enter a city name without spelling mistakes to get accurate data")
days = st.slider("Forecast days : ",min_value=1,max_value=5,
          help="Select for howmany days the forecast is needed ")
option = st.selectbox("Select data to view ",("Temperature Graph","Sky view"),
                      help="Select the type of view ")
st.subheader(f"{option} for next {days} days in {place.title()}")

# Create plot or graph accordingly
if place:
    try:
        filter_data=get_data(place,days)
        if option=="Temperature Graph":
            temp = [dict["main"]["temp"]/10 for dict in filter_data]
            date = [dict["dt_txt"] for dict in filter_data]
            figure=px.line(x=date,y=temp,labels={"x":"Dates","y":"Temperatures (C)"})
            st.plotly_chart(figure)
        if option == "Sky view":
            image={"Clear":"image/clear.png","Clouds":"image/cloud.png","Rain":"image/rain.png","Snow":"image/snow.png"}
            sky_condition = [dict["weather"][0]["main"] for dict in filter_data]
            image_path=[image[condition] for condition in sky_condition]

            st.image(image_path,width=115)
    except KeyError:
        st.write("Place doesn't exists")