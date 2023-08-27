import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

plt.style.use('seaborn')


# Plot the first and the last price of each exchanges
def plotting_first_and_last_price(stocks_df):
    # stocks_df.set_index('Date', inplace=True)

    earnings = []
    for i in stocks_df.columns:
        prices = { i + ' First Price':stocks_df[i][0], i + ' Last Price':stocks_df[i][-1]}
        earnings.append(prices)
    st.write(earnings)


# Plot the Risk / Reward 
def risk_reward_ratio(stocks_df):

    # Calculating the risk and returns from the exchanges
    stocks_df.set_index('Date', inplace=True)
    simple_returns = stocks_df.pct_change()

    # Calculating the Simple Returns Annually
    summary = simple_returns.describe().T.loc[:,['mean','std']]
    summary['mean'] = summary['mean'] * 252
    summary['std'] = summary['std'] * 252

    # Plot the Returns 
    fig = px.scatter(summary, x='std', y='mean', text=stocks_df.columns, log_x=True, size_max=60)
    fig.update_traces(textposition='top center')

    fig.update_layout(
        height=600, width=800, xaxis=dict(showgrid=False, title='Annual Risk'),
        yaxis=dict(showgrid=False, title='Annual Return'),
        title_text='Risk/Reward'
    )
    st.plotly_chart(fig)


# Simple Moving Average (SMA)
def simple_moving_average(stocks_df, user_input):

    # Creating the dataframe for SMA
    # stocks_df.set_index('Date', inplace=True)
    stocks_df['SMA_50'] = stocks_df[user_input].rolling(window=50).mean()
    stocks_df['SMA_100'] = stocks_df[user_input].rolling(window=100).mean()

    stocks_df.dropna(inplace=True)

    # Plot the SMA
    fig = px.line(stocks_df, y=[user_input, 'SMA_50', 'SMA_100'], title='Simple Moving Average (SMA)')

    fig.update_layout(height=600, width=800,xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=False, title='Price'))

    return st.plotly_chart(fig)

def bollinger_bands(stocks_df, user_input):

    # stocks_df.set_index('Date', inplace=True)
    stocks_df['SMA_20'] = stocks_df[user_input].rolling(window=20).mean()
    stocks_df['STD_20'] = stocks_df[user_input].rolling(window=20).std()

    stocks_df.dropna(inplace=True)

    stocks_df['Upper_band'] = stocks_df['SMA_20'] + (stocks_df['STD_20'] * 2)
    stocks_df['Lower_band'] = stocks_df['SMA_20'] - (stocks_df['STD_20'] * 2)  

    # Plot the SMA
    fig = px.line(stocks_df, y=[user_input, 'Upper_band', 'Lower_band'], title='Bollinger Bands (BB)')

    fig.update_layout(height=600, width=800,xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=False, title='Price'))

    return st.plotly_chart(fig)


