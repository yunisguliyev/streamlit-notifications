
only_when_on_other_tab = True




code = '''
let notification
document.addEventListener("visibilitychange", () => {
    if(document.visibilityState === "hidden"){

    

    }
    else{
        notification.close()
    }
})
'''


script = """
Notification.requestPermission().then(perm => {
if (perm === 'granted') {
    new Notification(title, {
        body: "body",
        icon: "icon",
        tag: "tag"
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

if only_when_on_other_tab:
    script = """
    let notification
    document.addEventListener("visibilitychange", () => {
        if(document.visibilityState === "hidden"){
    """ + script + """
        }
    else{
        notification.close()
        }
    })
    """
else:
    pass    


print(script)