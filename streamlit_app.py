import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('My parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale,Spinach &Rocket Smoothie')
streamlit.text('🐔Hard Boiled Free range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

##my_fruit_list = my_fruit_list.set_index('Fruit')
#fruits_to_show = my_fruit_list.loc[fruits_selected]
#stremlit.dataframe(fruits_to_show)
#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response)

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
my_cur.execute("select*from fruit_load_list")
my_data_rows= my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
my_cur.execute("insert into fruit_load_list values('from streamlit')")
 streamlit.title('ou will be Cordially Invited to the Exchanges
...as soon as you submit your Account Locator
...using the Streamlit form LINKED HERE!')
