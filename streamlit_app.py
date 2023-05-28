import streamlit
streamlit.title('My parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach &Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
##my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_to_show = my_fruit_list.loc[fruits_selected]
stremlit.dataframe(fruits_to_show)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

import snowflake.connector
