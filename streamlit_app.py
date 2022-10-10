import streamlit
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

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)





