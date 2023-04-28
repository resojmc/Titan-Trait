# Imports tkinter, json modules
import tkinter as tk
import json

# Initializes tkinter window and defines its dimensions and title. Also gets data.json file
main = tk.Tk()
main.geometry("320x600")
main.title("AOT Test")
main.resizable(False, False)
with open("Aot-Character-Match\AOT-Character-Match\Data.json") as f:
    data = f.read()
d = json.loads(data)
logo_img = tk.PhotoImage(
    file="Aot-Character-Match\AOT-Character-Match\logo.png")


def questions():
    pass


reset_button = tk.Button(main, text="reset", font=("Goth Titan", 14), width=6)
reset_button.place(x=7, y=560)

start_button = tk.Button(main, text="start", font=(
    "Goth Titan", 14), width=6)
start_button.place(x=60, y=560)

next_button = tk.Button(main, text="next", font=("Goth Titan", 14), width=6)
next_button.place(x=266, y=560)

prev_button = tk.Button(main, text="prev", font=("Goth Titan", 14), width=6)
prev_button.place(x=212, y=560)

questions_main_label = tk.Label(
    main, text=f"""-{d['Questions']['1']}-
    
    
    """, font=("Goth Titan", 30))
questions_main_label.place(x=40, y=160)

answers_label_a = tk.Radiobutton(main, text=f"{d['Answers']['1']['a']}")
answers_label_a.place(x=40, y=220)

answers_label_b = tk.Radiobutton(main, text=f"{d['Answers']['1']['b']}")
answers_label_b.place(x=40, y=250)


main_label = tk.Label(main, image=logo_img)
main_label.place(x=0, y=0)

char_match_label = tk.Label(
    main, text="personality test", font=("Goth Titan", 30))
char_match_label.place(x=67, y=100)

main.mainloop()
