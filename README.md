# Streamlit Push Notification Component

This repository contains a simple Python script that integrates with [Streamlit](https://streamlit.io) to send push notifications directly from your Streamlit app. The notifications can include a title, body, icon, and sound.

[DEMO APP](https://notifications.streamlit.app)

## Features

- **Customizable Notifications**: Specify the notification title, body, icon, and sound.
- **Browser-Based Notifications**: Utilizes the browser's native notification API.
- **Audio Alerts**: Plays a sound alongside the notification.

## Installation

   ```bash
pip install git+https://github.com/wambugu71/streamlit-push-notifications.git
   ```
or  
```bash
pip install streamlit-push-notifications
```
## Usage
```Python
import  streamlit  as  st
from streamlit_push_notifications import send_alert, send_push

st.write("Sending  notification alert!")
if  st.button("send notification"):
    send_alert(message="Hello from  streamlit_push_notifications ")
    
if  st.button("notification"):
    send_push(title= "Pass TITLE as an argument 🔥", body = "Pass BODY as an argument 👨🏻‍💻")

```

### Parameters

- `title`: The title of the notification (default is `"Pass TITLE as an argument 🔥"`).
- `body`: The body text of the notification (default is `"Pass BODY as an argument 👨🏻‍💻"`).
- `icon_path`: The path to an icon image (default is an empty string, meaning no icon).
- `sound_path`: The path to an audio file to be played with the notification (default is a sound from Pixabay).
- `tag`: A tag to group notifications (default is an empty string).

## How It Works

- **Notification API**: The script uses the JavaScript Notification API to create notifications.
- **Media Handling**: Streamlit’s media file manager handles uploading, and serving icon, and audio files.

### Error Handling

If the icon or sound file cannot be uploaded to the server, the script returns to using a default or the provided path directly.

## Contributing

Feel free to contribute by submitting issues or pull requests. Any enhancements or bug fixes are welcome!
Also you can contanct me via Main   developer [LinkedIn](https://www.linkedin.com/in/yunisguliyev/) 
or 
contact [Wambugu Kinyua](https://www.linkedin.com/in/kennedy-wambugu-1b362b26b/)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
