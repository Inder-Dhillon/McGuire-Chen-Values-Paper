import pandas as pd
import numpy as np
from tkinter import *

root = Tk()
root.title("Values")
root.geometry("600x800")


result_list = ['w1', 'w2', 'w3', 'w4', 'w5', 'f12', 'f13', 'f14', 'f15', 'f23', 'f24', 'f25', 'f34', 'f35', 'f45']
toggle_chen = None
toggle_mcg = None
mode = "cm"

#Importing Chen Values
chen_67_to_69 = pd.read_csv('chcof1.csv')
chen_70_to_74 = pd.read_csv('chcof2.csv')
chen_75_to_80 = pd.read_csv('chcof3.csv')
chen_81_to_85 = pd.read_csv('chcof4.csv')
chen_86_to_90 = pd.read_csv('chcof5.csv')
chen_67_to_69.index = result_list
chen_70_to_74.index = result_list
chen_75_to_80.index = result_list
chen_81_to_85.index = result_list
chen_86_to_90.index = result_list
#Importing McGuire Values
mcg_57_to_59 = pd.read_csv('mgcof1.csv')
mcg_60_to_69 = pd.read_csv('mgcof2.csv')
mcg_70_to_73 = pd.read_csv('mgcof3.csv')
mcg_74_to_76 = pd.read_csv('mgcof4.csv')
mcg_77_to_90 = pd.read_csv('mgcof5.csv')
mcg_57_to_59.index = result_list
mcg_60_to_69.index = result_list
mcg_70_to_73.index = result_list
mcg_74_to_76.index = result_list
mcg_77_to_90.index = result_list


def computation(event):
    z = int(element.get())
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
        mcg_results["text"]= (np.exp(toggle_mcg.sum(axis=1)).round(5))

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
        chen_results["text"]=(np.exp(toggle_chen.sum(axis=1)).round(5))


root["bg"] = "white"
Label(root, text="Element:", font="Roboto", bg="white").pack(pady=7)
element = Entry(root, justify=CENTER, bg="#dcdcdc", width=80, borderwidth=0)
element.pack()
mcg_results = Label(root, text="", font=("Roboto", 13), bg="white")
mcg_results.pack(padx=1)
chen_results = Label(root, text="", font=("Roboto", 13), bg="white")
chen_results.pack(padx=1)

element.bind("<Return>", computation)
root.mainloop()