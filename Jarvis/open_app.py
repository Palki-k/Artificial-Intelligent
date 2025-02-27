import pyautogui
import subprocess
import time



def open_app(command):

   try:
       subprocess.run(command)
   except Exception as e:
       print(e)
       pyautogui.press("win")
       time.sleep(0.2)
       pyautogui.write(command)
       time.sleep(0.2)
       pyautogui.press('enter')

while True:
    x=input()
    open_app(x)
