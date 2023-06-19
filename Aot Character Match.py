# Imports tkinter, json modules
import json
import tkinter as tk
from PIL import ImageTk, Image

# Initializes tkinter window and defines its dimensions and title. Also gets data.json file
main = tk.Tk()
main.geometry("320x600")
main.title("AOT Test")
main.resizable(False, False)
with open("Aot-Character-Match\AOT-Character-Match\Data.json", encoding="utf-8") as f:
    data = f.read()
d = json.loads(data)

# Main variables
val_a = tk.IntVar()
val_b = tk.IntVar()
q = list(d["Questions"].values())
a = list(d["Answers"].values())
image_paths = list(d["images"].values())
images = []
for i in image_paths:
    images.append(ImageTk.PhotoImage(Image.open(i)))
length = len(q)
current_question_index = 0


def question_num():
    # Keeps track of question number
    global question_number
    question_number += 1
    if question_number < length:
        questions_main_label.config(text=q[question_number])
        answers_label_a.config(text=a[question_number]['a'])
        answers_label_b.config(text=a[question_number]['b'])
        val_a.set(0)
        val_b.set(0)


def selection():
    # Tracks users answers and adds them to user data
    global val_a, val_b, current_question_index, d
    if val_a.get() == 1:
        val_b.set(0)
        d["UserData"][f"Q{current_question_index+1}"] = 1
    elif val_b.get() == 1:
        val_a.set(0)
        d["UserData"][f"Q{current_question_index+1}"] = 2


def char_match():
    global d
    personality_type = []
    for i in range(1, 71):
        if i in [1, 8, 15, 22, 29, 36, 43, 50, 57, 64]:
            if d["UserData"][f"Q{i}"] == 1:
                d["UserPT"]["E"] += 1
            elif d["UserData"][f"Q{i}"] == 2:
                d["UserPT"]["I"] += 1
        elif i in [2, 9, 14, 16, 23, 27, 30, 37, 41, 44, 51, 58, 62, 65]:
            if d["UserData"][f"Q{i}"] == 1:
                d["UserPT"]["S"] += 1
            elif d["UserData"][f"Q{i}"] == 2:
                d["UserPT"]["N"] += 1
        elif i in [3, 5, 6, 7, 10, 13, 17, 24, 28, 31, 33, 34, 38, 40, 42, 45, 47, 48, 52, 55, 56, 59, 61, 63, 66, 68, 69, 70]:
            if d["UserData"][f"Q{i}"] == 1:
                d["UserPT"]["T"] += 1
            elif d["UserData"][f"Q{i}"] == 2:
                d["UserPT"]["F"] += 1
        elif i in [4, 11, 12, 18, 19, 20, 25, 26, 32, 35, 39, 46, 49, 53, 54, 60, 67]:
            if d["UserData"][f"Q{i}"] == 1:
                d["UserPT"]["J"] += 1
            elif d["UserData"][f"Q{i}"] == 2:
                d["UserPT"]["P"] += 1

    if d["UserPT"]["I"] > d["UserPT"]["E"]:
        personality_type.append("I")
    else:
        personality_type.append("E")

    if d["UserPT"]["S"] > d["UserPT"]["N"]:
        personality_type.append("S")
    else:
        personality_type.append("N")

    if d["UserPT"]["T"] > d["UserPT"]["F"]:
        personality_type.append("T")
    else:
        personality_type.append("F")

    if d["UserPT"]["J"] > d["UserPT"]["P"]:
        personality_type.append("J")
    else:
        personality_type.append("P")

    personality_type = "".join(personality_type)

    return personality_type


def next_question():
    # Goes to next question
    global current_question_index
    current_question_index += 1
    if current_question_index >= length:
        results = char_match()
        results_data_label.config(
            text=f"{results}".lower(), font=("Goth Titan", 25))
        for char in d["Character PT"].values():
            if results == char:
                vals = list(d["Character PT"].values())
                fullname = list(d["Full Name"].values())
                position = vals.index(char)
                char_match_label.config(
                    image=images[position], height=150, width=150)
                char_name.config(
                    text=f"{fullname[position]}".lower(), font=("Goth Titan", 25))
    else:
        question_text = q[current_question_index]
        answer_options = a[current_question_index]
        val_a.set(0)
        val_b.set(0)
        answers_label_a.config(
            text=answer_options['a'], state='normal', variable=val_a, command=selection)
        answers_label_b.config(
            text=answer_options['b'], state='normal', variable=val_b, command=selection)
        questions_main_label.config(text=f"-{question_text}-")
        question_counter.config(text=f"{current_question_index}/70")


def prev_question():
    # Goes to previous question
    global current_question_index
    current_question_index -= 1
    if current_question_index >= length:
        results = char_match()
        results_data_label.config(
            text=f"{results}".lower(), font=("Goth Titan", 25))
        for char in d["Character PT"].values():
            if results == char:
                vals = list(d["Character PT"].values())
                fullname = list(d["Full Name"].values())
                position = vals.index(char)
                char_match_label.config(
                    image=images[position], height=150, width=150)
                char_name.config(
                    text=f"{fullname[position]}".lower(), font=("Goth Titan", 25))
    else:
        question_text = q[current_question_index]
        answer_options = a[current_question_index]
        val_a.set(0)
        val_b.set(0)
        answers_label_a.config(
            text=answer_options['a'], state='normal', variable=val_a, command=selection)
        answers_label_b.config(
            text=answer_options['b'], state='normal', variable=val_b, command=selection)
        questions_main_label.config(text=f"-{question_text}-")
        question_counter.config(text=f"{current_question_index}/70")


def reset():
    # Resets quiz
    global current_question_index
    current_question_index = 0
    question_text = q[current_question_index]
    answer_options = a[current_question_index]
    val_a.set(0)
    val_b.set(0)
    answers_label_a.config(
        text=answer_options['a'], state='normal', variable=val_a, command=selection)
    answers_label_b.config(
        text=answer_options['b'], state='normal', variable=val_b, command=selection)
    questions_main_label.config(text=f"-{question_text}-")
    results_data_label.config(text=f"")
    question_counter.config(text=f"{current_question_index}/70")


question_counter = tk.Label(
    main, text=f"{current_question_index}/70", font=("Goth Titan", 16))
question_counter.place(x=156, y=577, anchor="center")

reset_button = tk.Button(main, text="reset", font=(
    "Goth Titan", 14), width=14, command=reset)
reset_button.place(x=7, y=560)

next_button = tk.Button(main, text="next", font=(
    "Goth Titan", 14), width=6, command=next_question)
next_button.place(x=266, y=560)

prev_button = tk.Button(main, text="prev", font=(
    "Goth Titan", 14), width=6, command=prev_question)
prev_button.place(x=212, y=560)

questions_main_label = tk.Label(
    main, text=f"-{q[0]}-")
questions_main_label.place(x=160, y=170, anchor="center")

answers_label_a = tk.Checkbutton(
    main, variable=val_a, text=a[0]['a'], command=selection)
answers_label_a.place(x=160, y=220, anchor="center")

answers_label_b = tk.Checkbutton(
    main, variable=val_b, text=a[0]['b'], command=selection)
answers_label_b.place(x=160, y=260, anchor="center")

main_label = tk.Label(main, image=images[0])
main_label.place(x=160, y=50, anchor="center")

personality_label = tk.Label(
    main, text="personality test", font=("Goth Titan", 30))
personality_label.place(x=160, y=120, anchor="center")

char_match_label = tk.Label(main, )
char_match_label.place(x=100, y=430, anchor="center")

char_name = tk.Label(main, text="")
char_name.place(x=100, y=530, anchor="center")

results_label = tk.Label(
    main, text="results", font=("Goth Titan", 30))
results_label.place(x=160, y=320, anchor="center")

type_label = tk.Label(
    main, text="your type:", font=("Goth Titan", 25))
type_label.place(x=250, y=360, anchor="center")

results_data_label = tk.Label(
    main, text=f"".lower(), font=("Goth Titan", 25))
results_data_label.place(x=250, y=400, anchor="center")

main.mainloop()
