import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image


df = pd.read_csv('vehicles_us.csv')
df = df.head(500)

st.title('Choose the car you like')
st.subheader('You will definitely find your car')

img = Image.open("car.png")

st.image(img)

# add a histogram
fig_type = px.histogram(df,
                        x='type', 
                        nbins=13, 
                        color='type',
                        color_discrete_sequence=px.colors.qualitative.Set1, 
                        title='Types of vehicles')
fig_type.update_xaxes(categoryorder='total descending')

st.plotly_chart(fig_type, use_container_width=True)

# add a scatter plot
fig_price = px.scatter(df, 
                y='model_year', 
                x='price', 
                  color="condition",
                 color_discrete_sequence=px.colors.qualitative.Set1, 
                  title='Correlation between price and model year')
 
st.plotly_chart(fig_price, use_container_width=True)

# add a checkbox
st.caption('Choose your parameters here')

use_model_year = st.checkbox('Use Model Year as Y-axis', value=False)

if use_model_year:
    x_param = 'model_year'
else:
    x_param = 'type'

fig_price = px.scatter(df, 
                       x=x_param, 
                       y='price', 
                       color="condition",
                       color_discrete_sequence=px.colors.qualitative.Set1, 
                       title=f'Correlation between price and {x_param}')

st.plotly_chart(fig_price, use_container_width=True)
