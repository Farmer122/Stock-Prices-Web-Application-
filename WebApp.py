#!/usr/bin/env python
# coding: utf-8

# In[4]:


#pip install yfinance


# In[2]:


import yfinance as yf
import pandas as pd
import streamlit as st


# In[3]:


st.write('''
# Jamal Web Application for Apple Stock

Below we have the stock **closing prices** and **volume** for **Apple** Stock

''')


tickerSymbol = 'AAPL' #Also known as the stock symbol, this is the abbreviation for Apple 

tickerData = yf.Ticker(tickerSymbol)#retieves Data for our ticker, here it is Apple Stock

tickerDf = tickerData.history(period= '1d', start= '2011-4-06', end='2021-4-06') 
#Historical prices for Apple stock from 2011 - 2021

st.write(''' ## Closing price for Apple Stock''')

st.line_chart(tickerDf.Close)

st.write(''' ## Volume of Apple Stock''')

st.line_chart(tickerDf.Volume)


# In[ ]:




