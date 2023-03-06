import pyautogui
import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

def ScreenShots():
    myss = pyautogui.screenshot()
    myss.save("ss.png")
    print("Saved in this directory")

button = tk.Button(text='Take SS', command=ScreenShots, bg='green', fg='white', font=10)

canvas1.create_window(150, 150, window=button)

root.mainloop()
