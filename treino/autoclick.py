import pyautogui as py
import keyboard as kb
i = 1
ligado =False
while True:
    if kb.is_pressed('o'):
        ligado = True
    while ligado == True:
        py.write('p')
        if kb.is_pressed('o'):
            ligado = False
