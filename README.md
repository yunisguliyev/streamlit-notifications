# Streamlit Push Notification Component

This repository contains a simple Python script that integrates with [Streamlit](https://streamlit.io) to send push notifications directly from your Streamlit app. The notifications can include a title, body, icon, and sound.

[DEMO APP](https://notifications.streamlit.app)

## Features

- **Customizable Notifications**: Specify the notification title, body, icon, and sound.
- **Browser-Based Notifications**: Utilizes the browser's native notification API.
- **Audio Alerts**: Plays a sound alongside the notification.

## Installation

   ```bash
   git clone https://github.com/yunisguliyev/streamlit-push-notifications.git
   ```

## Usage

Import the `send_push` function from the script and call it within your Streamlit app.

### Parameters

- `title`: The title of the notification (default is `"Pass TITLE as an argument 🔥"`).
- `body`: The body text of the notification (default is `"Pass BODY as an argument 👨🏻‍💻"`).
- `icon_path`: The path to an icon image (default is an empty string, meaning no icon).
- `sound_path`: The path to an audio file to be played with the notification (default is a sound from Pixabay).
- `tag`: A tag to group notifications (default is an empty string).

### Example

```python
import streamlit as st
from streamlit-push-notifications import send_push

st.title("Streamlit Push Notification Example")

if st.button("Send Notification"):
    send_push(title="Hello, World!",
              body="This is a test notification.",
              icon_path="path_to_your_icon.png",
              sound_path="https://example.com/your_sound.mp3",
              tag="test")
```

## How It Works

- **Notification API**: The script uses the JavaScript Notification API to create notifications.
- **Media Handling**: Streamlit’s media file manager handles the uploading and serving of icon and audio files.

### Error Handling

If the icon or sound file cannot be uploaded to the server, the script falls back to using a default or the provided file path directly.

## Contributing

Feel free to contribute by submitting issues or pull requests. Any enhancements or bug fixes are welcome!
Also you can contanct me via [LinkedIn](https://www.linkedin.com/in/yunisguliyev/)

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---
