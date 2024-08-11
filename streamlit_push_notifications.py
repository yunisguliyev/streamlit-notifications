from streamlit import runtime
from streamlit.elements import image
from streamlit.components.v1 import html


def send_push(title: str = "Pass TITLE as an argument 🔥",
            body: str = "Pass BODY as an argument 👨🏻‍💻",
            icon_path: str = "",
            sound_path: str = "https://cdn.pixabay.com/audio/2024/02/19/audio_e4043ea6be.mp3",
            tag: str = "") -> None:


    try:
        icon_path_on_server = image.image_to_url(icon_path, 300, 300, "RGB", "auto", icon_path)
    except:
        icon_path_on_server = ""

    try:
        sound_path_on_server = runtime.get_instance().media_file_mgr.add(sound_path, mimetype= "audio/mpeg", coordinates= "1.(3.-14).5")
    except:
        sound_path_on_server = sound_path



    variables = f"""
    var title = "{title}"
    var body = "{body}"
    var icon = "{icon_path_on_server}"
    var audio = "{sound_path_on_server}"
    var tag = "{tag}"
    
    """

    script = """
    Notification.requestPermission().then(perm => {
    if (perm === 'granted') {
        new Notification(title, {
            body: body,
            icon: icon,
            tag: tag
        });

        new Audio(audio).play();
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
        script = script + 'console.log("Pass your ICON PATH as an argument")'

    combined = '<script>' + variables + script + '</script>'


    print(combined)
    html(combined, width= 0, height= 0)


