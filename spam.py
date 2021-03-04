import pyautogui, time

time.sleep(5)
f = open("C:/Users/William/Desktop/scribe.txt", "r")

for sentence in f:
    for word in sentence.split(" "):
        pyautogui.typewrite(word)
        pyautogui.press("enter")