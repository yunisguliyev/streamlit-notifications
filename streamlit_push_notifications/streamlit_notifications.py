from streamlit import runtime
from streamlit.components.v1 import html

def send_push(title: str = "Pass TITLE as an argument 🔥",
            body: str = "Pass BODY as an argument 👨🏻‍💻",
            icon_path: str = "",
            sound_path: str = "https://cdn.pixabay.com/audio/2024/02/19/audio_e4043ea6be.mp3",
            only_when_on_other_tab: bool = False,
            tag: str = "") -> None:
    """
  Sends a push notification to the user's browser.

  Parameters:
  - title (str): The title of the notification.
  - body (str): The body text of the notification.
  - icon_path (str): The file path to the icon image for the notification.
  - sound_path (str, url): The file path or URL to the sound to play when the notification is sent.
  - only_when_on_other_tab (bool): If True, the notification is sent only when the user is on another tab.
  - tag (str): A tag to associate with the notification.
  """

    try:
        icon_path_on_server = runtime.get_instance().media_file_mgr.add(icon_path, "image/png", "")
    except:
        icon_path_on_server = ""

    try:
        sound_path_on_server = runtime.get_instance().media_file_mgr.add(sound_path, mimetype= "audio/mpeg", coordinates= "1.(3.-14).5")
    except:
        sound_path_on_server = sound_path


    variables = f"""
    var title = "{title}";
    var body = "{body}";
    var icon = "{icon_path_on_server}";
    var audio = "{sound_path_on_server}";
    var tag = "{tag}";
    var notificationSent = false; // Flag to track notification state
    """

    script = """
    Notification.requestPermission().then(perm => {
        if (perm === 'granted') {
            notification = new Notification(title, {
                body: body,
                icon: icon,
                tag: tag
            });

            new Audio(audio).play();
            notificationSent = true; // Set the flag to true after sending notification
        } else if (perm === 'denied') {
            console.log('The user refuses to have notifications displayed.');
        } else if (perm === 'default') {
            console.log('The user choice is unknown, so the browser will act as if the value were denied.');
        } else {
            console.log('Unknown permission issue.');
        }
    }).catch(error => {
        console.error('An error occurred while requesting notification permission:', error);
    });
    """

    if icon_path == "":
        script += 'console.log("Pass your ICON PATH as an argument");'

    if only_when_on_other_tab:
        script = """
        let notification;
        document.addEventListener("visibilitychange", () => {{
            if (document.visibilityState === "hidden" && !notificationSent) {{""" + script + """}} else if (document.visibilityState === "visible") {{
                if (notification) {{
                    notification.close();
                }}
                notificationSent = false; // Reset the flag when the tab becomes visible
            }}
        }});
        """
    else:
        pass

    combined = '<script>' + variables + script + '</script>'
    html(combined, width=0, height=0)


def send_alert(message):
    """
  Displays a simple alert dialog in the user's browser.

  Parameters:
  - message (str): The message to display in the alert dialog.
  """
    script = '<script>' + f'window.alert("{message}")' + '</script>'
    html(script,width= 0, height= 0)
