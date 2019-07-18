import pandas as pd
import numpy as np
from tkinter import *

toggle_chen = None
toggle_mcg = None
chen_67_to_69 = pd.read_csv('chcof1.id', index_col=0)
chen_70_to_74 = pd.read_csv('chcof2.id', index_col=0)
chen_75_to_80 = pd.read_csv('chcof3.id', index_col=0)
chen_81_to_85 = pd.read_csv('chcof4.id', index_col=0)
chen_86_to_90 = pd.read_csv('chcof5.id', index_col=0)
# Importing McGuire Values
mcg_57_to_59 = pd.read_csv('mgcof1.id', index_col=0)
mcg_60_to_69 = pd.read_csv('mgcof2.id', index_col=0)
mcg_70_to_73 = pd.read_csv('mgcof3.id', index_col=0)
mcg_74_to_76 = pd.read_csv('mgcof4.id', index_col=0)
mcg_77_to_90 = pd.read_csv('mgcof5.id', index_col=0)

def popuperror(msg):
    popup = Tk()
    popup.geometry("300x100")
    popup["bg"] = "white"
    popup.wm_title("Error")
    label = Label(popup, text=msg, font="Roboto", bg="white")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy, bg="#dcdcdc", borderwidth=0)
    B1.pack()
    popup.mainloop()

def computation(event):
    value_entered = element.get()
    if value_entered.isdigit():
        z = int(value_entered)
    else:
        popuperror("Enter numbers only.")

    mode = str(radio_switch.get())

    if mode == "m" or mode =="cm":
        if z>=57 and z <= 59:
            toggle_mcg = mcg_57_to_59.copy()
        elif z>=60 and z <= 69:
            toggle_mcg = mcg_60_to_69.copy()
        elif z>=70 and z <= 73:
            toggle_mcg = mcg_70_to_73.copy()
        elif z>=74 and z <= 76:
            toggle_mcg = mcg_74_to_76.copy()
        elif z>=77 and z <= 90:
            toggle_mcg = mcg_77_to_90.copy()
        else:
            popuperror("Atomic number not in supported range.")
        for i in range(-2, 3):
            toggle_mcg["a" + str(i)] = toggle_mcg["a" + str(i)] * (z ** i)

    if mode == "c" or mode =="cm" :
        if z >= 67 and z <= 69:
            toggle_chen = chen_67_to_69.copy()
        elif z >= 70 and z <= 74:
            toggle_chen = chen_70_to_74.copy()
        elif z >= 75 and z <= 80:
            toggle_chen = chen_75_to_80.copy()
        elif z >= 81 and z <= 85:
            toggle_chen = chen_81_to_85.copy()
        elif z >= 86 and z <= 90:
            toggle_chen = chen_86_to_90.copy()
        else:
            popuperror("Atomic number not in supported range.")
        for i in range(-2, 3):
            toggle_chen["a" + str(i)] = toggle_chen["a" + str(i)] * (z ** i)
    if mode == "cm":
        mcg_label["text"] = "McGuire Results"
        mcg_label.pack(padx=1)
        mcg_results["text"] = (np.exp(toggle_mcg.sum(axis=1)).round(5))
        mcg_results.pack(padx=1)
        chen_label["text"] = "Chen Results"
        chen_label.pack(padx=1)
        chen_results["text"] = (np.exp(toggle_chen.sum(axis=1)).round(5))
        chen_results.pack(padx=1)
    elif mode=="c":
        chen_label["text"] = "Chen Results"
        chen_label.pack(padx=1)
        chen_results["text"] = (np.exp(toggle_chen.sum(axis=1)).round(5))
        chen_results.pack(padx=1)
        mcg_results.pack_forget()
        mcg_label.pack_forget()
    elif mode =="m":
        mcg_label["text"] = "McGuire Results"
        mcg_label.pack(padx=1)
        mcg_results["text"] = (np.exp(toggle_mcg.sum(axis=1)).round(5))
        mcg_results.pack(padx=1)
        chen_results.pack_forget()
        chen_label.pack_forget()


root = Tk()
root.title("Values")
root.geometry("600x800")
radio_switch = StringVar(None, "cm")
root["bg"] = "white"
Label(root, text="Enter Atomic Number:", font="Roboto", bg="white").pack(pady=7)
element = Entry(root, justify=CENTER, bg="#dcdcdc", width=80, borderwidth=0)
element.pack()
Radiobutton(root,
              text="Chen Values",
              padx = 20,
              variable=radio_switch,
              value="c", bg="white").pack()
Radiobutton(root,
              text="McGuire Values",
              padx = 20,
              variable=radio_switch,
              value="m", bg="white").pack()
Radiobutton(root,
              text="Both Chen and McGuire Values",
              padx = 20,
              variable=radio_switch,
              value="cm", bg="white").pack()
mcg_label = Label(root, text="", font=("Roboto", 13), bg="white")
mcg_results = Label(root, text="", font=("Roboto", 13), bg="white")
chen_label = Label(root, text="", font=("Roboto", 13), bg="white")
chen_results = Label(root, text="", font=("Roboto", 13), bg="white")
element.bind("<Return>", computation)
root.mainloop()