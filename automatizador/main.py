import pyautogui
from time import sleep

cont = 0
while True:
    pyautogui.moveTo(530, 10)
    sleep(2)
    pyautogui.click()
    sleep(2)
    pyautogui.moveTo(60, 110)
    pyautogui.click()
    sleep(2)
    pyautogui.moveTo(400, 120)
    pyautogui.click()
    sleep(2)
    pyautogui.write('twitter.com')
    pyautogui.press('enter')
    sleep(2)
    pyautogui.moveTo(800, 300)
    pyautogui.click()
    pyautogui.write(f'Este tweet foi escrito em um teste automatizado de python. Tweet numero {cont}')
    sleep(2)
    pyautogui.moveTo(1150, 430)
    pyautogui.click()
    # cont += 1twitter.com
