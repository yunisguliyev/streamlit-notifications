import streamlit as st
from streamlit_push_notifications import send_push


st.title("Streamlit Push Notifications 📢")
st.divider()

title = st.text_input("Title:")
body = st.text_input("Body:")
icon = st.checkbox("Icon:", help= "You can add your icons as well")
sound = st.checkbox("Sound:", help= "You can add your audio as well")



if sound:
    sound_path = "https://cdn.pixabay.com/audio/2024/02/19/audio_e4043ea6be.mp3"
else:
    sound_path = ""


if st.button("Push"):
    if title != '' or body != '':
        send_push(title= title,
                body= body, icon_path= "streamlit-mark-light.png", sound_path= sound_path)
    else:
        send_push(icon_path= "streamlit-mark-light.png", sound_path= sound_path)

