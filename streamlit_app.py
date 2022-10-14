import streamlit
#import pandas
#import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My Parents new healthy Diner")

streamlit.header("Breakfast Favorites")
streamlit.text(" 🥣 Omega 3 and Blueberry Omlet")
streamlit.text(" 🥗 Kale Spinach & Rocket Smoothie")
streamlit.text(" 🐔 Hard-boiled free-range egg !")
streamlit.text(" 🥑🍞Avacado Tost !")

streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")
streamlit.text("🍌 Oaty banana smoothie")
streamlit.text("🍌🥭Trail mix smoothie")
streamlit.text("🍇 Endless summer smoothie")
streamlit.text("🥝 Orange creamsicle protein shake")


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Apple', 'Avocado'])
fruits_selected = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_selected)

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?','Apple')
  if not fruit_choice:
     streamlit.error("Please select a fruit to get Information")
  else:
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    streamlit.dataframe(fruityvice_normalized)
  except URLError as e:
    streamlit.error()
  
 


streamlit.stop()

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)
add_my_fruit = streamlit.text_input('What fruit would you like Add?')
my_cur.execute("Insert into fruit_load_list values ('"+ add_my_fruit +"')")



