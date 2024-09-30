import tkinter as tk
import pandas as pd
import random
import time

from docutils.nodes import image

data = pd.read_csv("data/french_words.csv")
current_card = {}

def next_click():
    global current_card
    current_card = random.randint(0,101)
    french_word = data["French"][current_card]
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(word_title, text = f"{french_word}", fill = "black")
    canvas.itemconfig(front_canvas, image = front_image)




def english_translation():
    global current_card
    english_word = data["English"][current_card]
    back_image = tk.PhotoImage(file="images/card_back.png")
    canvas.itemconfig(front_canvas, image = back_image )
    canvas.itemconfig(card_title, text="English", fill = "white")
    canvas.itemconfig(word_title, text=f"{english_word}", fill = "white")








#-----------------------UI Creation------------------------
BACKGROUND_COLOR = "#B1DDC6"


window = tk.Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg=BACKGROUND_COLOR)

window.after(3000, func=english_translation)

canvas = tk.Canvas(width=800, height=526)

front_image = tk.PhotoImage(file="images/card_front.png")
front_canvas = canvas.create_image(400,263,image = front_image)
card_title = canvas.create_text(400, 150,text = "Title", font=("Ariel",40,"italic"))

word_title = canvas.create_text(400,263, text="word", font=("Ariel",60,"bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0, columnspan = 2)



right_image = tk.PhotoImage(file="images/right.png")
left_image = tk.PhotoImage(file="images/wrong.png")
right_button = tk.Button(image=right_image, highlightthickness=0, command= next_click)
left_button = tk.Button(image=left_image, highlightthickness=0, command=next_click)
right_button.grid(row = 1, column = 0)
left_button.grid(row = 1, column = 1)




#-------------------------------Load Data------------------------






window.mainloop()
