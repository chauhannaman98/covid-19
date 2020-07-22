import streamlit as st
import pandas as pd
from covid import Covid
import csv

st.title('Covid 19, a worldwide analysis')
st.text('Source: Johns Hopkins University')
st.text('Clear cache from menu in upper-right corner for updating data')

covid = Covid()

countries = covid.list_countries()

@st.cache
def generate_csv_data():
  country_list = []
  for country in countries:
    country_list.append(covid.get_status_by_country_name(country['name']))

  keys = country_list[0].keys()
  with open('covid.csv', 'w') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(country_list)

generate_csv_data()

data = pd.read_csv('covid.csv')
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

data_head = data.head(10)
# st.write(data_head)
