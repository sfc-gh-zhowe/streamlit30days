from datetime import time, datetime
import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

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
     appointment = st.slider("Schedule your appointment:", value=(time(11, 30), time(12, 45)))
     st.write("You're scheduled for:", appointment)
     # Example 4
     st.subheader('Datetime slider')
     start_time = st.slider("When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm")
     st.write("Start time:", start_time)

# map the inputs to the function blocks
days = {
     "Day 2" : day_two,
     "Day 3" : day_three,
     "Day 5" : day_five,
     "Day 8" : day_eight,
}

main()