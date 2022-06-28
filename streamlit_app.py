import streamlit as st

st.server.add_route("do", do_callback)

if st.server.request.do == 