import requests

API_KEY="f1c398336b1c685da0f0d3f8cc2d7095"
def get_data(place,days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response=requests.get(url)
    data=response.json()
    filter_data = data["list"]
    nr_values=8*days
    filter_data=filter_data[:nr_values]
    return filter_data



