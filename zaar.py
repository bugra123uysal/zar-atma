import tkinter as tk
import random

""" random  """
def rnddd():
    fff=random.randint(1,6)
    goor.config(text=fff)



yyer=tk.Tk()
yyer.geometry("400x600")
""" atılan zatın sonucunu göstericek """
goor=tk.Label(yyer,text="0")
goor.place(x=190, y=130)

""" bastığında zarı atar """
dugme=tk.Button(yyer,text="zar at", command=rnddd)
dugme.place(x=180, y=240)



yyer.mainloop()