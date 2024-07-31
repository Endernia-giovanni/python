import keyboard as kb
def press():
    while True:
        if kb.is_pressed("p"):
            return True
        elif kb.is_pressed('o'):
            return "pou"
        else:
            return "Null"