import streamlit as st
from streamlit_push_notifications import send_push


st.title("Streamlit Push Notifications 📢")
st.divider()

title = st.text_input("Title:")
body = st.text_input("Body:")
sound = st.checkbox("Sound:", help= "You can add your audio as well", value= True)



if sound:
    sound_path = "delfin.mp3"
else:
    sound_path = "delfin.mp3"


if st.button("Push"):
    if title != '' or body != '':
        send_push(title= title,
                body= body, icon_path= "streamlit-mark-light.png", sound_path= sound_path)
    else:
        send_push(icon_path= "streamlit-mark-light.png", sound_path= sound_path)

