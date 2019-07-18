import pandas as pd
import numpy as np
from tkinter import *

# Importing Chen Values
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

def computation(event=True):
    value_entered = element.get()
    if value_entered.isdigit():
        z = int(value_entered)
    else:
        popuperror("Enter a valid atomic number.")
        return
    mode = str(radio_switch.get())

    if mode == "m" or mode == "cm":
        if z >= 57 and z <= 59:
            toggle_mcg = mcg_57_to_59.copy()
        elif z >= 60 and z <= 69:
            toggle_mcg = mcg_60_to_69.copy()
        elif z >= 70 and z <= 73:
            toggle_mcg = mcg_70_to_73.copy()
        elif z >= 74 and z <= 76:
            toggle_mcg = mcg_74_to_76.copy()
        elif z >= 77 and z <= 90:
            toggle_mcg = mcg_77_to_90.copy()
        else:
            popuperror("Atomic number not in supported range for McGuire Values.\nEnter a number between 57 and 90")
            return
        for i in range(-2, 3):
            toggle_mcg["a" + str(i)] = toggle_mcg["a" + str(i)] * (z ** i)
        mcg_values = "McGuire Values\n" + np.exp(toggle_mcg.sum(axis=1)).round(5).to_string()

    if mode == "c" or mode == "cm":
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
            popuperror("Atomic number not in supported range for Chen Values.\nEnter a number between 67 and 90")
            return
        for i in range(-2, 3):
            toggle_chen["a" + str(i)] = toggle_chen["a" + str(i)] * (z ** i)
        chen_values = "Chen Values\n" + np.exp(toggle_chen.sum(axis=1)).round(5).to_string()

    if mode == "cm":
        mcg_results["text"] = mcg_values
        mcg_results.pack(padx=30, side=LEFT)
        chen_results["text"] = chen_values
        chen_results.pack(padx=30, side=LEFT)
    elif mode == "c":
        chen_results["text"] = chen_values
        chen_results.pack(padx=30,side=TOP)
        mcg_results.pack_forget()
    elif mode == "m":
        mcg_results["text"] = mcg_values
        mcg_results.pack(padx=30, side=TOP)
        chen_results.pack_forget()

def popuperror(msg):
    popup = Tk()
    popup.geometry("430x100")
    popup["bg"] = "white"
    popup.wm_title("Error")
    label = Label(popup, text=msg, font="Roboto", bg="white")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command=popup.destroy, bg="#dcdcdc", borderwidth=0)
    B1.pack()
    popup.mainloop()

# GUI
root = Tk()
root.title("Values")
root.geometry("350x500")

radio_switch = StringVar(None, "cm")
root["bg"] = "white"
Label(root, text="Enter Atomic Number:", font=("Roboto", 15), bg="white").pack(pady=7, anchor=W, padx=30)
element = Entry(root, justify=CENTER, bg="#dcdcdc", borderwidth=0, font=("Roboto", 13))
element.pack(fill=X, padx=30, anchor=W)
Radiobutton(root, text="Chen Values", padx=30, variable=radio_switch, value="c", bg="white").pack(anchor=W)
Radiobutton(root, text="McGuire Values", padx=30, variable=radio_switch, value="m", bg="white").pack(anchor=W)
Radiobutton(root, text="Both Chen and McGuire Values", padx=30, variable=radio_switch, value="cm", bg="white").pack(anchor=W)
mcg_results = Label(root, text="", font=("Roboto", 13), bg="white")
chen_results = Label(root, text="", font=("Roboto", 13), bg="white")
element.bind("<Return>", computation)
Button(root, text="Generate", command=computation, bg="#dcdcdc", borderwidth=0).pack(anchor=W, padx=30, pady=5)
root.mainloop()