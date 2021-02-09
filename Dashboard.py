import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


stocks_df = pd.read_csv('stock.csv')
stocks_df = stocks_df.sort_values(by = 'Date')
desc = stocks_df.describe()
stocks_df['Date'] = pd.to_datetime(stocks_df['Date'], format = '%Y-%m-%d')

def show_plot(df,title):
    fig, ax = plt.subplots(figsize=(18,6))
    for i in df.columns[1:]:
        ax.plot(df['Date'], df[i], label = i)
    ax.title.set_text(title)
    ax.legend()
    st.pyplot(fig)
def normalized(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i]/x[i][0]
    return x

def interactive_plot(df,title):
    fig = px.line(title = title)
    
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y = df[i], name = i)
        
    st.plotly_chart(fig)
def multi_dailyreturn(df):
    new_df = df[df.columns[1:].to_list()]
    dailyreturn = new_df.copy()

    for j in range(1,len(new_df)):
        dailyreturn.loc[j] = ((new_df.loc[j]-new_df.loc[j-1])/new_df.loc[j-1])*100
    dailyreturn.loc[0] = 0
    
    df[df.columns[1:].to_list()] = dailyreturn
    return df


st.title('Welcome To Stock Price Analysis App')
if st.button('Dataset'):
    st.write(stocks_df)
    st.button('Close')

if st.button('Data Description'):
    st.write(desc)
    st.button('Close')

if st.button('Charts'):
    st.button('Close')
    st.subheader('Price')
    interactive_plot(stocks_df,' ')
    st.subheader('Normalized Price')
    interactive_plot(normalized(stocks_df),' ')
    st.subheader('Daily Return')
    interactive_plot(multi_dailyreturn(stocks_df),' ')
   

