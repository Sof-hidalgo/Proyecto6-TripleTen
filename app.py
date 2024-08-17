import streamlit as st
import plotly.express as px
from analysis import load_data, clean_data, get_manufacturers, filter_data_by_manufacturer


# Loading and cleaning data
csv_path = 'vehicles_us.csv'
car_data = load_data(csv_path)
car_data = clean_data(car_data)


# App title
st.title('Vehicles Analysis')

# price distribution histogram
st.header('Price Distribution')
st.write('This histogram shows the price distribution of vehicles in USD. It allows visualizing the frequency of vehicles in different price ranges, identifying the most common price ranges and the general dispersion of prices in the dataset.')


hist_botton = st.button('Build histogram')

if hist_botton:
    fig = px.histogram(car_data,
        x='price', 
        color_discrete_sequence=['#FF6B6B'],
        labels={'price': 'USD'})
    st.plotly_chart(fig)




# Model Year Distribution histogram
st.header('Model Year Distribution')
st.write('This histogram represents the distribution of vehicle model years. It helps to understand the age of vehicles in the dataset, showing which model years are most prevalent and how vehicles are distributed over time.')
fig = px.histogram(car_data, 
                   x='model_year', 
                   color_discrete_sequence=['#4ECDC4'],
                   labels={'model_year": "Model Year'})
st.plotly_chart(fig)




# 'Mileage Distribution (odometer) histogram
st.header('Mileage Distribution')
st.write('This histogram shows the distribution of vehicle mileage (odometer) in miles. It allows you to see how vehicle usage is distributed, identifying common mileage ranges and possible outliers.')
fig = px.histogram(car_data, 
             x='odometer', 
             #title= 'Mileage Distribution',
             labels={'odometer': 'Mileage (Miles)'}
             )
st.plotly_chart(fig)




# Relation between Mileage and Vehicles Price
st.header('Relation between Mileage and Vehicles Price')
st.write('This scatter plot relates mileage to vehicle price. It helps to visualize whether there is a correlation between these two variables, showing how price tends to vary with respect to mileage.')

scatter_button = st.button('Build Scatter Plot')
if scatter_button:
   
    fig = px.scatter(car_data, 
                    x='odometer', 
                    y='price',
                    color_discrete_sequence=['#FFA07A'],
                    labels= {'odometer': 'Mileage (Miles)', 'price': 'USD'}
                    ) 
    st.plotly_chart(fig)




# Vehicle types by manufacturer
st.header('Vehicle types by manufacturer')
st.write('This stacked bar chart shows the types of vehicles produced by each manufacturer. It allows to compare the diversity and proportion of vehicle types between different manufacturers.')
fig = px.bar(car_data, 
             x='manufacturer', 
             color='type', 
             #title='Vehicle types by manufacturer ',
             labels={'type': 'Vehicle type', 'manufacturer': 'Manufacturer'},
             barmode='stack'
             )
st.plotly_chart(fig)




# Relation between ´condition´ and ´model_year´ histogram
st.header('Relation between ´condition´ and ´model_year´')
st.write('This histogram shows the relationship between model year and vehicle condition. It helps to visualize how the condition of vehicles is distributed over model years, allowing to identify trends in vehicle aging and maintenance.')
fig = px.histogram(car_data, 
             x='model_year', 
             color='condition',
             #title= 'Relation between ´condition´ and ´model_year´',
             labels={'model_year': 'Model Year', 'condition' : 'Car Condition'}
             )
st.plotly_chart(fig)


# Compare Price Distribution between Manufacturers
st.header("Compare Price Distribution between Manufacturers")

manufacturers = get_manufacturers(car_data)

# Creating a sidebar for manufacturer selection
manufacturer_1 = st.sidebar.selectbox("Select manufacturer 1", manufacturers)
manufacturer_2 = st.sidebar.selectbox("Select manufacturer 2", manufacturers)

# Checkbox to normalize the histogram
normalize = st.sidebar.checkbox("Normalize histogram", value=True)

# filtering the data according to user selection
filtered_data = filter_data_by_manufacturer(car_data, manufacturer_1, manufacturer_2)

# histogram with custom colors
fig = px.histogram(filtered_data, 
                    x='price', 
                    color='manufacturer', 
                    barmode='overlay', 
                    histnorm='percent' if normalize else None,
                    title=f'Price Distribution: {manufacturer_1} vs {manufacturer_2}',
                    labels={'price': 'Price', 'manufacturer': 'Manufacturer'},
                    color_discrete_sequence=['#f9b697', '#82c20a', '#12c0fd'])
st.plotly_chart(fig)