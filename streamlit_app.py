import streamlit as st

st.server.add_route("do", do_callback)

temperatura = st.server.request.temperatura

print(temperatura)