import numpy as np
import pandas as pd
import streamlit as st

import seaborn as sns
import matplotlib.pyplot as plt

import src.data_validation
import src.data_transformation

import plotly.express as px
import plotly.graph_objects as go
plt.style.use('seaborn')

st.set_option('deprecation.showPyplotGlobalUse', False)

# Datasets
df = pd.read_csv('data\indexData.csv')
index_data = pd.read_csv('data\indexInfo.csv')
stocks_df = pd.read_csv("data\stock_exchanges.csv")

# Title
st.sidebar.title('Stock Exchanges Dataset')
user_menu = st.sidebar.radio('Select an Option',
                             ('Overview', 'Data', 'Analysis', 'Indicators', 'Returns'))

# Overview
if user_menu == 'Overview':
    st.header('World-Stock-Exchange-Analysis')
    st.title('Overview')
    st.write('''This is a project of Data Analysis of different Stock Exchanges Data. So the goal is to create a Dashboard using streamlit
                for Analysing which Indices has less risk and high returns or vice-versa by using Python Libraries. Before going further
                I want to tell this project is for Education and Inforamtion purposes don't see the Analysis and start investing in Stocks.''')

    st.header('Data')
    st.write('''There are three dataframe of the stock exchanges where the indexInfo data provides the information of the stock exchanges, indexData
                provides the high, low, open, close of the Index and last stock_exchanges which contains only the Close price of the stocks.''')

    st.header("Analysis")
    st.write('Analysing the Stock Performance using previous data by plotting diagrams and dataframe for visulaisation of the Indices')

    st.header('Indicators')
    st.write('''Indicators are great tools for giving us signals by where will the stock go in the Future. We will use Simple Moving Average(SMA)
                and Bollinger Bands which are mostly used by the traders in the market.''')

    st.header('Returns')
    st.write('''Analysing the past returns and risk/reward ratio to look which exchange or indices which has performed well and what is the risk
                of holding the stock, also providing the first day price and the last price of the stocks to see the changes in the price.''')


# Data
if user_menu == 'Data':
    # Index Info
    st.title('Stocks Exchange Code & Information')
    st.table(index_data)

    # Index Data
    st.header('Stocks Exchange Data')
    st.dataframe(df)

    # Stocks Close Data
    st.header('Stocks Exchange Close Price')
    st.dataframe(stocks_df)


# EDA
if user_menu == 'Analysis':

    # Making toggle
    st.title('Analysis of the Stock Exchanges')
    home_stocks, ivd_stocks = st.tabs(["Exchanges", "Individual Stock Exchanges"])

    with home_stocks:

        # plotting countplot
        st.header('Stock Exhanges data count')
        stock_count = src.data_validation.stock_counts(df)
        st.pyplot(stock_count)

        # Plotting Close price
        st.header('Stock Exchanges Price')
        src.data_validation.plotting_close_price(stocks_df)

        # Plotting Co-relation
        st.header('Co-realtion between Exchanges')
        src.data_validation.plotting_corr(stocks_df)

    with ivd_stocks:

        # Plotting Individually
        src.data_validation.new_york_exchange(df)
        src.data_validation.tokyo_exchange(df)
        src.data_validation.nasdaq_exchange(df)
        src.data_validation.cananda_exchange(df)
        src.data_validation.hong_kong_exchange(df)
        src.data_validation.germany_exchange(df)
        src.data_validation.swizz_exchange(df)
        src.data_validation.korea_exchange(df)
        src.data_validation.taiwan_exchange(df)
        src.data_validation.china_exchange(df)
        src.data_validation.shangai_exchange(df)
        src.data_validation.europe_exchange(df)
        src.data_validation.india_exchange(df)
        src.data_validation.south_africa_exchange(df)

# Indicators
if user_menu == 'Indicators':

    stocks_df.set_index('Date', drop=True, inplace=True)
    st.title('Indicators for Each Stock')

    # Getting the user input
    user_input = st.selectbox('Select the Stock Exchanges',
                                stocks_df.columns)

    # Plot the Simple Moving Average
    src.data_transformation.simple_moving_average(stocks_df, user_input)

    # Plot the Bollinger Bands
    src.data_transformation.bollinger_bands(stocks_df, user_input)


# Returns
if user_menu == 'Returns':

    # Plot the Risk/Rewad Ratio
    st.header('Risk/Reward Ratio')
    src.data_transformation.risk_reward_ratio(stocks_df)

    # Plot the first and last Day price
    st.header('First and Last Day Close price')
    src.data_transformation.plotting_first_and_last_price(stocks_df)
