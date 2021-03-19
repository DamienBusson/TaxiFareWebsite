import streamlit as st
import datetime
import requests


# '''
# # TaxiFareModel front
# '''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# DAY
pickup_day = st.date_input(
    "On which day would you like to travel?",
    )
st.write('You will travel on:', pickup_day)


# TIME
pickup_time = st.time_input(
    'At what time?',
    )
st.write('You will travel at:', pickup_time)


# DEPARTURE ADDRESS
pickup_longitude = st.number_input('Insert your pick-up longitude')
pickup_latitude = st.number_input('Insert your pick-up latitude')


# ARRIVAL ADDRESS
dropoff_longitude = st.number_input('Insert your drop-off longitude')
dropoff_latitude = st.number_input('Insert your drop-off latitude')


# NUMBER OF PASSENGERS
passenger_count = st.slider('number of passengers:', 1, 4, 1)


#'''
### Once we have these, let's call our API in order to retrieve a prediction

#See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...
#
#🤔 How could we call our API ? Off course... The `requests` package 💡
#'''


pickup_datetime = str(pickup_day) + ' ' + str(pickup_time) + ' UTC'

X = dict(
        key=['na'],
        pickup_datetime=[pickup_datetime],
        pickup_longitude=[float(pickup_longitude)],
        pickup_latitude=[float(pickup_latitude)],
        dropoff_longitude=[float(dropoff_longitude)],
        dropoff_latitude=[float(dropoff_latitude)],
        passenger_count=[int(passenger_count)])

url = "https://cloudruntry-cb57u5rl5q-ew.a.run.app/predict_fare/"

response = requests.get(url, params=X).json()

prediction = response['prediction']

if st.button('Get your price prediction'):
    st.write(f"Your taxi fare will cost approx {prediction} USD.")


# if url == 'hhttps://cloudruntry-cb57u5rl5q-ew.a.run.app/predict_fare/':

#   st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')


#'''

#2. Let's build a dictionary containing the parameters for our API...

#3. Let's call our API using the `requests` package...

#4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
#'''
