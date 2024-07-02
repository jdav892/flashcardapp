BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="lightblue")


x_image = PhotoImage(file="C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/flashCards/images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/flashCards/images/right.png")
check_button = Button(image=check_image, highlightthickness=0)
check_button.grid(column=1, row=1)

canvas = Canvas(width=900, height=600)
front_image = PhotoImage(file="C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/flashCards/images/card_front.png")
canvas.create_image(400, 526, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

window.mainloop()