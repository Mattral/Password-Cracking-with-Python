import os
import pyautogui
import time

try:
   pass_file = open("10-million-password-list-top-1000000.txt", "r")
except:
   print("Password file not opened")
   quit()

time.sleep(5)

for password in pass_file:
    password = password.replace("\n","")

    pyautogui.write(password, interval=0.1)
    pyautogui.press('enter')
    time.sleep(0.5)
    print(password)
