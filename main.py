from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ------------------------------ FLIP CARD --------------------------------- #


# ---------------------------- GET VOCAB WORD ------------------------------- #
vocab_list = pandas.read_csv("data/arabic_words.csv")
to_learn = vocab_list.to_dict(orient="records")


def vocab_word():
    current_card = random.choice(to_learn)
    card.itemconfig(card_title, text="Arabic")
    card.itemconfig(card_word, text=current_card["Arabic"])


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash Cards")

card = Canvas(width=800, height=526)
front = PhotoImage(file="card_images/card_front.png")
card.create_image(400, 263, image=front)
card_title = card.create_text((400, 150), text="", font=("Arial", 40, "italic"))

card_word = card.create_text((400, 263), text="", font=("Arial", 60, "bold"))

card.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card.grid(column=0, row=0, columnspan=2)

right = PhotoImage(file="card_images/right1.png")
right_button = Button(image=right, highlightthickness=0, command=vocab_word)
right_button.grid(column=1, row=1)

wrong = PhotoImage(file="card_images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=vocab_word)
wrong_button.grid(column=0, row=1)

vocab_word()
window.mainloop()
