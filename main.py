import streamlit as st
import requests


title = st.header("Share Ticker - API FRONT")

new_ticker = st.text_input("Enter a ticker: ").upper()

st.write(new_ticker)

body = [
  {
    "current_ticker": new_ticker
  }
]

if new_ticker:
    r = requests.put(f"https://test-api-evpk.onrender.com/api/v1/ticker/{new_ticker}", json={"new_ticker": new_ticker}).json()
    st.write(r)

