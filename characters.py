# character imgs
import os
import tkinter as tk


def load_images(root):
    images = {}
    images["logo"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "logo.png"))
    images["eren"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "eren.png"))
    images["annie"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "annie.png"))
    images["armin"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "armin.png"))
    images["mikasa"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "mikasa.png"))
    images["bertholdt"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "bertholdt.png"))
    images["carla"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "carla.png"))
    images["connie"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "connie.png"))
    images["erwin"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "erwin.png"))
    images["ymir"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "founder.png"))
    images["grisha"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "grisha.png"))
    images["hange"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "hange.png"))
    images["historia"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "historia.png"))
    images["jean"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "jean.png"))
    images["levi"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "levi.png"))
    images["reiner"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "reiner.png"))
    images["sasha"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "sasha.png"))
    images["zeke"] = tk.PhotoImage(file=os.path.join(
        os.path.dirname(__file__), "character-imgs", "zeke.png"))

    root.images = images  # store the images as an attribute of the root window
