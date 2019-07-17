import pandas as pd
import numpy as np
from tkinter import *

def computation(event):
    toggle_chen = None
    toggle_mcg = None
    chen_67_to_69 = pd.read_csv('chcof1.csv',index_col=0)
    chen_70_to_74 = pd.read_csv('chcof2.csv',index_col=0)
    chen_75_to_80 = pd.read_csv('chcof3.csv',index_col=0)
    chen_81_to_85 = pd.read_csv('chcof4.csv',index_col=0)
    chen_86_to_90 = pd.read_csv('chcof5.csv',index_col=0)
    # Importing McGuire Values
    mcg_57_to_59 = pd.read_csv('mgcof1.csv',index_col=0)
    mcg_60_to_69 = pd.read_csv('mgcof2.csv',index_col=0)
    mcg_70_to_73 = pd.read_csv('mgcof3.csv',index_col=0)
    mcg_74_to_76 = pd.read_csv('mgcof4.csv',index_col=0)
    mcg_77_to_90 = pd.read_csv('mgcof5.csv',index_col=0)
    z = int(element.get())
    mode = str(radio_switch.get())

    if mode == "m" or mode =="cm":
        if z>=57 and z <= 59:
            toggle_mcg = mcg_57_to_59
        elif z>=60 and z <= 69:
            toggle_mcg = mcg_60_to_69
        elif z>=70 and z <= 73:
            toggle_mcg = mcg_70_to_73
        elif z>=74 and z <= 76:
            toggle_mcg = mcg_74_to_76
        elif z>=77 and z <= 90:
            toggle_mcg = mcg_77_to_90
        else:
            raise Exception("Atomic number not in supported range.")
        print("****McG Values****")
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
            raise Exception("Atomic number not in supported range.")
        print("****Chen Values****")
        for i in range(-2, 3):
            toggle_chen["a" + str(i)] = toggle_chen["a" + str(i)] * (z ** i)
    if mode == "cm":
        mcg_results["text"] = (np.exp(toggle_mcg.sum(axis=1)).round(5))
        chen_results["text"] = (np.exp(toggle_chen.sum(axis=1)).round(5))
    elif mode=="c":
        chen_results["text"] = (np.exp(toggle_chen.sum(axis=1)).round(5))
        mcg_results["text"] = ""
    elif mode =="m":
        mcg_results["text"] = (np.exp(toggle_mcg.sum(axis=1)).round(5))
        chen_results["text"] = ""

root = Tk()
root.title("Values")
root.geometry("600x800")
radio_switch = StringVar()
root["bg"] = "white"
Label(root, text="Element:", font="Roboto", bg="white").pack(pady=7)
element = Entry(root, justify=CENTER, bg="#dcdcdc", width=80, borderwidth=0)
element.pack()
Radiobutton(root,
              text="Chen Values",
              padx = 20,
              variable=radio_switch,
              value="c").pack()
Radiobutton(root,
              text="McGuire Values",
              padx = 20,
              variable=radio_switch,
              value="m").pack()
Radiobutton(root,
              text="Both Chen and McGuire Values",
              padx = 20,
              variable=radio_switch,
              value="cm").pack()
mcg_results = Label(root, text="", font=("Roboto", 13), bg="white")
mcg_results.pack(padx=1)
chen_results = Label(root, text="", font=("Roboto", 13), bg="white")
chen_results.pack(padx=1)

element.bind("<Return>", computation)
root.mainloop()