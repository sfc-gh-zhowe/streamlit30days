from datetime import time, datetime, timedelta
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st
import pandas_profiling 
from streamlit_pandas_profiling import st_profile_report

def main():
     with st.sidebar:
          day = st.selectbox("Select Day", (days.keys()))
     st.header(day)
     days[day]()

def day_two():
     st.write('Hello world!')

def day_three():
     st.header('st.button')
     if st.button('Say hello'):
          st.write('Why hello there')
     else:
          st.write('Goodbye')

def day_five():
     st.header('st.write')
     # Example 1
     st.write('Hello, *World!* :sunglasses:')
     # Example 2
     st.write(1234)
     # Example 3
     df = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40] })
     st.write(df)
     # Example 4
     st.write('Below is a DataFrame:', df, 'Above is a dataframe.')
     # Example 5
     df2 = pd.DataFrame(np.random.randn(200, 3), columns=['a', 'b', 'c'])
     c = alt.Chart(df2).mark_circle().encode(x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
     st.write(c)

def day_eight():
     def slider_change():
          dt1 = datetime.combine(datetime.today(), st.session_state.slider_value[0])
          dt2 = datetime.combine(datetime.today(), st.session_state.slider_value[1])
          delta = dt2 - dt1
          if (delta < timedelta(hours=2)):
               hr = dt1 + timedelta(hours=2)
               st.session_state.slider_value = (st.session_state.slider_value[0], time(hr.hour, hr.minute))

     st.header('st.slider')
     # Example 1
     st.subheader('Slider')
     age = st.slider('How old are you?', 0, 130, 25)
     st.info(f"I'm {age} years old")
     #st.write("I'm ", age, 'years old')
     # Example 2
     st.subheader('Range slider')
     values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
     st.write('Values:', values)
     # Example 3
     st.subheader('Range time slider')
     appointment = st.slider("Schedule your appointment:", value=st.session_state.slider_value, on_change=slider_change, key='slider_value')
     st.write("You're scheduled for:", appointment)
     # Example 4
     st.subheader('Datetime slider')
     start_time = st.slider("When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm")
     st.write("Start time:", start_time)

def day_nine():
     st.header('Line chart')

     chart_data = pd.DataFrame(
          np.random.randn(20, 3),
          columns=['a', 'b', 'c'])

     st.line_chart(chart_data)

def day_ten():
     st.header('st.selectbox')

     option = st.selectbox(
          'What is your favorite color?',
          ('Blue', 'Red', 'Green'))

     st.write('Your favorite color is ', option)

def day_eleven():
     st.header('st.multiselect')

     options = st.multiselect(
          'What are your favorite colors',
          ['Green', 'Yellow', 'Red', 'Blue'],
          ['Yellow', 'Red'])

     st.write('You selected:', options)

def day_twelve():
     st.header('st.checkbox')

     st.write ('What would you like to order?')

     icecream = st.checkbox('Ice cream')
     coffee = st.checkbox('Coffee')
     cola = st.checkbox('Cola')

     if icecream:
          st.write("Great! Here's some more 🍦")

     if coffee: 
          st.write("Okay, here's some coffee ☕")

     if cola:
          st.write("Here you go 🥤")

def day_fourteen():
     st.header('`streamlit_pandas_profiling`')

     df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')

     pr = df.profile_report()
     st_profile_report(pr)







if 'slider_value' not in st.session_state:
    st.session_state.slider_value = (time(11, 30), time(12, 45))

# map the inputs to the function blocks
days = {
     "Day 2"  : day_two,
     "Day 3"  : day_three,
     "Day 5"  : day_five,
     "Day 8"  : day_eight,
     "Day 9"  : day_nine,
     "Day 10" : day_ten,
     "Day 11" : day_eleven,
     "Day 12" : day_twelve,
     "Day 14" : day_fourteen,
}

main()