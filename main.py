BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas




window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


x_image = PhotoImage(file="C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/flashCards/images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/flashCards/images/right.png")
check_button = Button(image=check_image, highlightthickness=0)
check_button.grid(column=1, row=1)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="C:/Users/jay-5/Documents/code/pythonProj/100daysOfPy/flashCards/images/card_front.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 40, "bold"))

window.mainloop()