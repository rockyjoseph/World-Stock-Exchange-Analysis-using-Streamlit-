import pandas as pd
import numpy as np
import seaborn as sns

import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

plt.style.use('seaborn')

# Plot the value Counts of Each Stock.
def stock_counts(df):
    plt.figure(figsize=(15,8))
    sns.countplot(x=df['Index'],)
    plt.title('World Stock Exchanges', fontsize=30)
    plt.ylabel('Exchange Count')
    plt.xlabel('Exchange Code')


# Plot the close Price of the Exchanges
def plotting_close_price(stocks_df):
    
    # plot the close price of all the exhanges in one graph
    plot = px.line(stocks_df,x='Date', y=['NYA','N225','IXIC','GSPTSE','HSI','GDAXI','SSMI','KS11','TWII','SS','SZ','N100','NSEI','JO'],
                    title='Stock Exchanges Prices')
    plot.update_layout(height=600, width=900, xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=False, title='Price'))

    return st.plotly_chart(plot)


# Plot the Co-relation between Exchanges
def plotting_corr(stocks_df):
    fig = px.imshow(stocks_df.corr(), text_auto=True, aspect="auto")
    fig.update_layout(height=600, width=900)

    return st.plotly_chart(fig)


# Plotting all the Exchanges Individually
def new_york_exchange(df):
    df.drop(columns=['High','Open','Low','Adj Close', 'Volume'], inplace=True)

    NYA = df[df['Index'] == 'NYA']
    NYA.drop(columns=['Index'], inplace=True)

    fig = go.Figure()
    fig.add_trace(go.Line(x=NYA.Date ,y=NYA.Close,
                         mode='lines'))
    fig.update_layout(title='NYA Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def tokyo_exchange(df):
    N225 = df[df['Index'] == 'N225']
    N225.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=N225.Date ,y=N225.Close,
                         mode='lines'))
    fig.update_layout(title='N225 Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def nasdaq_exchange(df):
    IXIC = df[df['Index'] == 'IXIC']
    IXIC.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=IXIC.Date ,y=IXIC.Close,
                         mode='lines'))
    fig.update_layout(title='IXIC Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))

    return st.plotly_chart(fig)

def cananda_exchange(df):
    GSPTSE = df[df['Index'] == 'GSPTSE']
    GSPTSE.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=GSPTSE.Date ,y=GSPTSE.Close,
                         mode='lines'))
    fig.update_layout(title='GSPTSE Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def hong_kong_exchange(df):
    HSI = df[df['Index'] == 'HSI']
    HSI.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=HSI.Date ,y=HSI.Close,
                         mode='lines'))
    fig.update_layout(title='HSI Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def germany_exchange(df):
    GDAXI = df[df['Index'] == 'GDAXI']
    GDAXI.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=GDAXI.Date ,y=GDAXI.Close,
                         mode='lines'))
    fig.update_layout(title='GDAXI Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def swizz_exchange(df):
    SSMI = df[df['Index'] == 'SSMI']
    SSMI.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=SSMI.Date ,y=SSMI.Close,
                         mode='lines'))
    fig.update_layout(title='SSMI Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def korea_exchange(df):
    KS11 = df[df['Index'] == 'KS11']
    KS11.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=KS11.Date ,y=KS11.Close,
                         mode='lines'))
    fig.update_layout(title='Ks11 Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def taiwan_exchange(df):
    TWII = df[df['Index'] == 'TWII']
    TWII.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=TWII.Date ,y=TWII.Close,
                         mode='lines'))
    fig.update_layout(title='TWII Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def china_exchange(df):
    SS = df[df['Index'] == '000001.SS']
    SS.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=SS.Date ,y=SS.Close,
                         mode='lines'))
    fig.update_layout(title='SS Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def shangai_exchange(df):
    SZ = df[df['Index'] == '399001.SZ']
    SZ.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=SZ.Date ,y=SZ.Close,
                         mode='lines'))
    fig.update_layout(title='SZ Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def europe_exchange(df):
    N100 = df[df['Index'] == 'N100']
    N100.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=N100.Date ,y=N100.Close,
                         mode='lines'))
    fig.update_layout(title='N100 Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def india_exchange(df):
    NSEI = df[df['Index'] == 'NSEI']
    NSEI.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=NSEI.Date ,y=NSEI.Close,
                         mode='lines'))
    fig.update_layout(title='NSEI Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                  yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

def south_africa_exchange(df):
    JO = df[df['Index'] == 'J203.JO']
    JO.drop(columns=['Index'], inplace=True)
    
    fig = go.Figure()
    fig.add_trace(go.Line(x=JO.Date ,y=JO.Close,
                         mode='lines'))
    fig.update_layout(title='JO Stock Exchange' ,height=500, width=900, xaxis=dict(showgrid=False, title='Date'),
                                yaxis=dict(showgrid=False, title='Price'))
    
    return st.plotly_chart(fig)

