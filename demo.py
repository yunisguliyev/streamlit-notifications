import streamlit as st
from streamlit_push_notifications import send_push, send_alert


st.title("Streamlit Push Notifications 📢")
st.divider()

title = st.text_input("Title:")
body = st.text_input("Body:")
icon = st.checkbox("Icon:", help= "You can add your icons as well")
sound = st.checkbox("Sound:", help= "You can add your audio as well")
only_off_tab = st.checkbox("On other tab:", help= "Sends the push notification only when user is on the other tab")

if icon:
    icon_path = "streamlit-mark-light.png"
    st.info("Due to an unknown issue related to Streamlit Cloud, the icon is not displayed in the demo. However, this functionality has been tested and confirmed to work correctly on both local and remote servers.")
else:
    icon_path = ""

if sound:
    sound_path = "https://cdn.pixabay.com/audio/2024/02/19/audio_e4043ea6be.mp3"
else:
    sound_path = ""    


if st.button("Push"):
    if title != '' or body != '':
        send_push(title= title,
                body= body, icon_path= icon_path, sound_path= sound_path,only_when_on_other_tab= only_off_tab)
    else:
        send_push(icon_path= icon_path, sound_path= sound_path, only_when_on_other_tab= only_off_tab)

if st.button("Alert"):
    send_alert(body)

