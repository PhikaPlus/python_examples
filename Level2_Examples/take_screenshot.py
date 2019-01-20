import pyautogui
import tkinter as tk

window = tk.Tk()


def callback():
    image = pyautogui.screenshot('screenshot.png')


shot_btn = tk.Button(window,
                     text = 'Take ScreenShot Now',
                     command = callback)
shot_btn.place(x = 50, y = 50)

window.mainloop()
