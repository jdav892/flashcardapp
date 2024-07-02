BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

current_card = {}
learning = {}
try:
    data = pandas.read_csv("/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("/data/french_words.csv")
    learning = original_data.to_dict(orient="records")
else:
    learning = data.to_dict(orient="records")





def swap_card():
    global current_card, timer
    window.after_cancel(timer)
    current_card = random.choice(learning)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_image)
    timer = window.after(3000, func=flip_card)
    
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_image)    
    

def known():
    learning.remove(current_card)
    data = pandas.DataFrame(learning)
    data.to_csv("/data/words_to_learn.csv", index=False)
    swap_card()



window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=flip_card)


x_image = PhotoImage(file="/flashCards/images/wrong.png")
x_button = Button(image=x_image, highlightthickness=0, command=swap_card)
x_button.grid(column=0, row=1)

check_image = PhotoImage(file="/flashCards/images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=known)
check_button.grid(column=1, row=1)

canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="/images/card_front.png")
back_image = PhotoImage(file="/images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 40, "bold"))

swap_card()

window.mainloop()