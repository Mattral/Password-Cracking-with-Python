import pyautogui

secret = "turtle"
password = ""

while password != secret:
    password = pyautogui.password('Enter password (text will be hidden)')

print("Cracked, password is " + secret)
