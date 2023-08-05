import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruit_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)

# create repeatable code black (called a function)
def get_fruityvice_data(this_fruit_choice):
      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice )
      fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
      return fruityvice_normalized

streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
        streamlit.error("Please select the fruit to get information")
  else:
      back_from_function = get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)

except URLError as e:
    streatlit.error()


# write your own comment -what does the next line do? 

# write your own comment - what does this do?


# streamlit.stop()



def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from pc_rivery_db.public.fruit_load_list")
         return my_cur.fetchall()
      

#add a button to load fruit
if streamlit.button('get fruit load list'):
      my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
      my_data_rows = get_fruit_load_list()
      streamlit.dataframe(my_data_rows)

streamlit.text(my_data_rows)



streamlit.write('Thanks for adding', add_my_fruit)
my_cur.execute("insert into FRUIT_LOAD_LIST values('from streamlit')")
