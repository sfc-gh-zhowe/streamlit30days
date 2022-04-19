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

def day_fifteen():
     st.header('st.latex')

     st.latex(r'''
          a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
          \sum_{k=0}^{n-1} ar^k =
          a \left(\frac{1-r^{n}}{1-r}\right)
          ''')

def day_sixteen():
     st.title('Customizing the theme of Streamlit apps')

     st.write('Contents of the `.streamlit/config.toml` file of this app')

     st.code("""
     [theme]
     primaryColor="#F39C12"
     backgroundColor="#2E86C1"
     secondaryBackgroundColor="#AED6F1"
     textColor="#FFFFFF"
     font="monospace"
     """)

     number = st.sidebar.slider('Select a number:', 0, 10, 5)
     st.write('Selected number from slider widget is:', number)

def day_seventeen():
     st.title('st.secrets')

     st.write(st.secrets['message'])
     st.write("DB username:", st.secrets["db_username"])
     st.write("DB password:", st.secrets["db_password"])
     st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

     # And the root-level secrets are also accessible as environment variables:
     import os
     st.write(
          "Has environment variables been set:",
          os.environ["db_username"] == st.secrets["db_username"])
          
def day_eighteen():
     st.title('st.file_uploader')

     st.subheader('Input CSV')
     uploaded_file = st.file_uploader("Choose a file")

     if uploaded_file is not None:
          df = pd.read_csv(uploaded_file)
          st.subheader('DataFrame')
          st.write(df)
          st.subheader('Descriptive Statistics')
          st.write(df.describe())
     else:
          st.info('☝️ Upload a CSV file')

def day_nineteen():
     st.set_page_config(layout="wide")

     st.title('How to layout your Streamlit app')

     with st.expander('About this app'):
          st.write('This app shows the various ways on how you can layout your Streamlit app.')
          st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)

     st.sidebar.header('Input')
     user_name = st.sidebar.text_input('What is your name?')
     user_emoji = st.sidebar.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
     user_food = st.sidebar.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

     st.header('Output')

     col1, col2, col3 = st.columns(3)

     with col1:
          if user_name != '':
               st.write(f'👋 Hello {user_name}!')
          else:
               st.write('👈  Please enter your **name**!')

     with col2:
          if user_emoji != '':
               st.write(f'{user_emoji} is your favorite **emoji**!')
          else:
               st.write('👈 Please choose an **emoji**!')

     with col3:
          if user_food != '':
               st.write(f'🍴 **{user_food}** is your favorite **food**!')
          else:
               st.write('👈 Please choose your favorite **food**!')


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
     "Day 15" : day_fifteen,
     "Day 16" : day_sixteen,
     "Day 17" : day_seventeen,
     "Day 18" : day_eighteen,
     "Day 19" : day_nineteen,
}

main()