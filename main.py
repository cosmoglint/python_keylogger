import pynput

from pynput.keyboard import Key, Listener

def pressed(key):
    print(key, "pressed")

def released(key):
    if key==Key.esc:
        return False

with Listener(on_press=pressed, on_release=released) as the_listener:
    the_listener.join()
