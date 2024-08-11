import streamlit as st
from streamlit_push_notifications import send_push


st.title("Streamlit Push Notifications 📢")
st.divider()

title = st.text_input("Title:")
body = st.text_input("Body:")

if st.button("Push"):
    if title != '' or body != '':
        send_push(title= title,
                body= body)
    else:
        send_push()

#streamlit run test_ui.py