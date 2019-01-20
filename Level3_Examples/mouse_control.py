import pyautogui

print(pyautogui.size())         # screen size
print(pyautogui.position())     # mouse position

# move to!
pyautogui.moveTo(100, 200)      

# x: 80px y: 80px
pyautogui.click(80, 80)         
pyautogui.doubleClick(80, 80)
pyautogui.rightClick(80, 80)

Mouse Control in Python
