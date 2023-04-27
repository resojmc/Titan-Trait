# Imports tkinter, json modules
import tkinter as tk
import json

# Initializes tkinter window and defines its dimensions and title. Also gets data from .json file
root = tk.Tk()
root.geometry("800x600")
root.title("AOT Match")
with open("Aot-Character-Match\Data.json") as f:
    data = f.read()
d = json.loads(data)

# Imports attack on titan logo
logo_img = tk.PhotoImage(file="C:\Users\J\Documents\GitHub\Aot-Character-Match\logo.png")

main_label = tk.Label(root, text="Character Personality Match", image=logo_img)
main_label.place(x=200, y=200)

# Character personality types
eren_yeager = d["Main Type"]["I"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["P"]
mikasa_ackerman = d["Main Type"]["I"], d["Main Type"]["S"], d["Main Type"]["T"], d["Main Type"]["J"]
armin_arlert = d["Main Type"]["I"], d["Main Type"]["N"], d["Main Type"]["F"], d["Main Type"]["J"]
levi_ackerman = d["Main Type"]["I"], d["Main Type"]["S"], d["Main Type"]["T"], d["Main Type"]["P"]
erwin_smith = d["Main Type"]["E"], d["Main Type"]["N"], d["Main Type"]["T"], d["Main Type"]["J"]
annie_leonhart = d["Main Type"]["I"], d["Main Type"]["S"], d["Main Type"]["T"], d["Main Type"]["P"]
hange_zoe = d["Main Type"]["E"], d["Main Type"]["N"], d["Main Type"]["T"], d["Main Type"]["P"]
historia_reiss = d["Main Type"]["E"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["J"]
founder_ymir = d["Main Type"]["I"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["J"]
zeke_yeager = d["Main Type"]["I"], d["Main Type"]["N"], d["Main Type"]["T"], d["Main Type"]["P"]
reiner_braun = d["Main Type"]["E"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["J"]
bertholdt_hoover = d["Main Type"]["I"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["J"]
connie_springer = d["Main Type"]["E"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["P"]
grisha_yeager = d["Main Type"]["I"], d["Main Type"]["N"], d["Main Type"]["F"], d["Main Type"]["J"]
carla_yeager = d["Main Type"]["E"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["J"]
sasha_braus = d["Main Type"]["E"], d["Main Type"]["S"], d["Main Type"]["F"], d["Main Type"]["P"]
jean_kirstein = d["Main Type"]["E"], d["Main Type"]["S"], d["Main Type"]["T"], d["Main Type"]["J"]

root.mainloop()
