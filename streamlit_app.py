import streamlit

streamlit.title('My Parents New Healthy Diner')


streamlit.header('Breakfast Favorites')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.text('Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.dataframe(my_fruit_list)


