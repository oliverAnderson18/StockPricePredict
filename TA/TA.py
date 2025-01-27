import numpy as np
import pandas as pd
import pandas_ta as ta

# Adding the columns of the next day's Open and Close values (targets of our prediction)

df = pd.read_excel("../Data/asset.xlsx")

df["Date"] = pd.to_datetime(df["Date"])
df["Volume"] = df['Volume'].str.replace(',', '').astype(float)

df = df.sort_values("Date")

df["High_next"] = df["High"].shift(-1)
df["Low_next"] = df["Low"].shift(-1)
df["Open_next"] = df["Open"].shift(-1)
df["Close_next"] = df["Close"].shift(-1)

# Creating columns with the values of TA indicators

df["Short_SMA"] = ta.sma(df["Close"], length=15)
df["Mid_SMA"] = ta.sma(df["Close"], length=45)
df["Long_SMA"] = ta.sma(df["Close"], length=140)

df["EMA"] = ta.ema(df["Close"], length=60)

bbands = ta.bbands(df["Close"], length=10, std=2)
df = pd.concat([df, bbands], axis=1)

df["RSI"] = ta.rsi(df["Close"], length=14)

stoch = ta.stoch(df["High"], df["Low"], df["Close"], length=14, smoothK=3, smoothD=3)
df = pd.concat([df, stoch], axis=1)

df["CMF"] = ta.cmf(df["High"], df["Low"], df["Close"], df["Volume"], length=14)

df.dropna()
