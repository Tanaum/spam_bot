import time, pyautogui

name = input('Enter file name: ')
try:
    repeat = int(input('How many times should it repeat? '))
except ValueError:
    quit('Do you not know what numbers are?')

time.sleep(10)
n=0

while n <repeat:
    with open(name,'r') as file:
        for line in file:
            pyautogui.typewrite(line)
            pyautogui.press('enter')
    n+=1
    time.sleep(5)