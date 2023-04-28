# Imports tkinter, json modules
import json
import tkinter as tk


# Initializes tkinter window and defines its dimensions and title. Also gets data.json file
main = tk.Tk()
main.geometry("320x600")
main.title("AOT Test")
main.resizable(False, False)
with open("Aot-Character-Match\AOT-Character-Match\Data.json") as f:
    data = f.read()
d = json.loads(data)

# Main variables
val_a = tk.IntVar()
val_b = tk.IntVar()
q = list(d["Questions"].values())
a = list(d["Answers"].values())
length = len(q)
current_question_index = 0
user_data = {"Q1": 0, "Q2": 0, "Q3": 0, "Q4": 0, "Q5": 0,
             "Q6": 0, "Q7": 0, "Q8": 0, "Q9": 0, "Q10": 0,
             "Q11": 0, "Q12": 0, "Q13": 0, "Q14": 0, "Q15": 0,
             "Q16": 0, "Q17": 0, "Q18": 0, "Q19": 0, "Q20": 0, "Q21": 0}


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
    global val_a, val_b, current_question_index, user_data
    if val_a.get() == 1:
        val_b.set(0)
        user_data[f"Q{current_question_index+1}"] = 1
    elif val_b.get() == 1:
        val_a.set(0)
        user_data[f"Q{current_question_index+1}"] = 2


def next_question():
    # Goes to next question
    global current_question_index
    current_question_index += 1
    if current_question_index > length:
        return result()
    question_text = q[current_question_index]
    answer_options = a[current_question_index]
    val_a.set(0)
    val_b.set(0)
    answers_label_a.config(
        text=answer_options['a'], state='normal', variable=val_a, command=selection)
    answers_label_b.config(
        text=answer_options['b'], state='normal', variable=val_b, command=selection)
    questions_main_label.config(text=f"-{question_text}-")


def prev_question():
    # Goes to previous question
    global current_question_index
    current_question_index -= 1
    if current_question_index > length:
        return result()
    question_text = q[current_question_index]
    answer_options = a[current_question_index]
    val_a.set(0)
    val_b.set(0)
    answers_label_a.config(
        text=answer_options['a'], state='normal', variable=val_a, command=selection)
    answers_label_b.config(
        text=answer_options['b'], state='normal', variable=val_b, command=selection)
    questions_main_label.config(text=f"-{question_text}-")


def result():
    global user_data
    results_data_label.config(text=f"{user_data}")


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


reset_button = tk.Button(main, text="reset", font=(
    "Goth Titan", 14), width=6, command=reset)
reset_button.place(x=7, y=560)

start_button = tk.Button(main, text="start", font=(
    "Goth Titan", 14), width=6)
start_button.place(x=60, y=560)

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

main_label = tk.Label(main, image=characters.logo_img)
main_label.place(x=160, y=50, anchor="center")

char_match_label = tk.Label(
    main, text="personality test", font=("Goth Titan", 30))
char_match_label.place(x=160, y=120, anchor="center")

results_label = tk.Label(
    main, text="results", font=("Goth Titan", 30))
results_label.place(x=160, y=320, anchor="center")

results_data_label = tk.Label(
    main, text=f"", font=("Goth Titan", 5))
results_data_label.place(x=160, y=360, anchor="center")

main.mainloop()
