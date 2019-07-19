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
        mcg_results.grid(row=4, column=0,columnspan=2)
        chen_results["text"] = chen_values
        chen_results.grid(row=4, column=2,columnspan=2)
    elif mode == "c":
        chen_results["text"] = chen_values
        chen_results.grid(row=4,columnspan=3,column=0, sticky=W+E+N+S)
        mcg_results.grid_forget()
    elif mode == "m":
        mcg_results["text"] = mcg_values
        mcg_results.grid(row=4,columnspan=3,column=0, sticky=W+E+N+S)
        chen_results.grid_forget()

def popuperror(msg):
    popup = Tk()
    popup.iconbitmap("logo.ico")
    popup.geometry("430x100")
    popup.resizable(False, False)
    popup["bg"] = "white"
    popup.wm_title("Error")
    label = Label(popup, text=msg, font="Roboto", bg="white")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Exit", command=popup.destroy, bg="#2c3e50", fg="white", padx=10, borderwidth=0)
    B1.pack()
    popup.mainloop()

# GUI
root = Tk()
root.title("Values")
root.geometry("500x500")
root.iconbitmap("logo.ico")
frame = Frame(root)
frame.pack()
radio_switch = StringVar(None, "cm")
root["bg"] = "white"
frame["bg"] = "white"
Label(frame, text="Enter Atomic Number:", font=("Roboto", 15), bg="white", pady=5).grid(row=0,columnspan=3,column=0, sticky=W+E+N+S)
element = Entry(frame, justify=CENTER, bg="#e4e8e8", borderwidth=0, font=("Roboto", 13))
element.grid(row=1,columnspan=3,column=0, sticky=W+E+N+S)
Radiobutton(frame, text="Chen Values", variable=radio_switch, value="c", bg="white", padx=1, pady=5).grid(row=2,column=0)
Radiobutton(frame, text="McGuire Values", variable=radio_switch, value="m", bg="white").grid(row=2, column=1)
Radiobutton(frame, text="Both Chen and McGuire Values", variable=radio_switch, value="cm", bg="white").grid(row=2, column=2)
mcg_results = Label(frame, text="", font=("Roboto", 13), bg="white",pady=10)
chen_results = Label(frame, text="", font=("Roboto", 13), bg="white",pady=10)
element.bind("<Return>", computation)
Button(frame, text="Generate", command=computation, bg="#2c3e50", fg="white" , padx=10, borderwidth=0).grid(row=3,columnspan=3,column=0)
root.mainloop()