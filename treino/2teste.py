import pyautogui as pag
from suporte import press as ps
while True:
    if ps() == True:
        print("True")
    elif ps() == "pou":
        print("pou")
    else:
        print("Null")