import pandas as pd
import numpy as np
from tkinter import *
from tkinter import filedialog

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
        if 57 <= z <= 59:
            toggle_mcg = mcg_57_to_59.copy()
        elif 60 <= z <= 69:
            toggle_mcg = mcg_60_to_69.copy()
        elif 70 <= z <= 73:
            toggle_mcg = mcg_70_to_73.copy()
        elif 74 <= z <= 76:
            toggle_mcg = mcg_74_to_76.copy()
        elif 77 <= z <= 90:
            toggle_mcg = mcg_77_to_90.copy()
        else:
            popuperror("Atomic number not in supported range for McGuire Values.\nEnter a number between 57 and 90")
            return
        for i in range(-2, 3):
            toggle_mcg["a" + str(i)] = toggle_mcg["a" + str(i)] * (z ** i)

        mcg_values = "McGuire Values\n" + np.exp(toggle_mcg.sum(axis=1)).round(5).to_string().replace("1.0000", "N/A      ")

    if mode == "c" or mode == "cm":
        if 67 <= z <= 69:
            toggle_chen = chen_67_to_69.copy()
        elif 70 <= z <= 74:
            toggle_chen = chen_70_to_74.copy()
        elif 75 <= z <= 80:
            toggle_chen = chen_75_to_80.copy()
        elif 81 <= z <= 85:
            toggle_chen = chen_81_to_85.copy()
        elif 86 <= z <= 90:
            toggle_chen = chen_86_to_90.copy()
        else:
            popuperror("Atomic number not in supported range for Chen Values.\nEnter a number between 67 and 90")
            return
        for i in range(-2, 3):
            toggle_chen["a" + str(i)] = toggle_chen["a" + str(i)] * (z ** i)
        chen_values = "Chen Values\n" + np.exp(toggle_chen.sum(axis=1)).round(5).to_string().replace("1.00000", "N/A      ")

    if mode == "cm":
        mcg_results["text"] = mcg_values
        mcg_results.grid(row=8, column=0,columnspan=2)
        chen_results["text"] = chen_values
        chen_results.grid(row=8, column=2,columnspan=2)
    elif mode == "c":
        chen_results["text"] = chen_values
        chen_results.grid(row=8,columnspan=5,column=0, sticky=W+E+N+S)
        mcg_results.grid_forget()
    elif mode == "m":
        mcg_results["text"] = mcg_values
        mcg_results.grid(row=8,columnspan=5,column=0, sticky=W+E+N+S)
        chen_results.grid_forget()


def popuperror(msg, kind="Error"):
    popup = Tk()
    popup.iconbitmap("logo.ico")
    popup.geometry("430x100")
    popup.resizable(False, False)
    popup["bg"] = "white"
    popup.wm_title(kind)
    label = Label(popup, text=msg, font=("Arial", 12), bg="white")
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Exit", command=popup.destroy, bg="#2c3e50", fg="white", padx=10, borderwidth=0)
    B1.pack()
    popup.mainloop()


def exportcsv(event=True):
    exp_df = pd.DataFrame()
    from_a = from_an.get()
    if from_a.isdigit():
        z1 = int(from_a)
    else:
        popuperror("Enter a valid atomic number.")
        return
    to_a = to_an.get()
    if to_a.isdigit():
        z2 = int(to_a)
    else:
        popuperror("Enter a valid atomic number.")
        return
    mode = str(radio_switch.get())
    for z in range(z1, z2+1):
        if mode == "m" or mode == "cm":
            if 57 <= z <= 59:
                toggle_mcg = mcg_57_to_59.copy()
            elif 60 <= z <= 69:
                toggle_mcg = mcg_60_to_69.copy()
            elif 70 <= z <= 73:
                toggle_mcg = mcg_70_to_73.copy()
            elif 74 <= z <= 76:
                toggle_mcg = mcg_74_to_76.copy()
            elif 77 <= z <= 90:
                toggle_mcg = mcg_77_to_90.copy()
            else:
                popuperror("Atomic number not in supported range for McGuire Values.\nEnter a number between 57 and 90")
                return
            for i in range(-2, 3):
                toggle_mcg["a" + str(i)] = toggle_mcg["a" + str(i)] * (z ** i)
            exp_df[str(z)] = (np.exp(toggle_mcg.sum(axis=1)).round(5)).replace(1.0, "N/A")
        if mode == "c" or mode == "cm":
            if 67 <= z <= 69:
                toggle_chen = chen_67_to_69.copy()
            elif 70 <= z <= 74:
                toggle_chen = chen_70_to_74.copy()
            elif 75 <= z <= 80:
                toggle_chen = chen_75_to_80.copy()
            elif 81 <= z <= 85:
                toggle_chen = chen_81_to_85.copy()
            elif 86 <= z <= 90:
                toggle_chen = chen_86_to_90.copy()
            else:
                popuperror("Atomic number not in supported range for Chen Values.\nEnter a number between 67 and 90")
                return
            for i in range(-2, 3):
                toggle_chen["a" + str(i)] = toggle_chen["a" + str(i)] * (z ** i)
            exp_df[str(z)] = np.exp(toggle_chen.sum(axis=1)).round(5).replace(1.0, "N/A")
    export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
    exp_df.to_csv(export_file_path, index=True, header=True)
    popuperror(msg="Values Exported", kind="Exported")


# GUI
root = Tk()
root.title("MFCKYLD")
root.geometry("700x700")
root.iconbitmap("logo.ico")
frame = Frame(root)
frame.pack()
radio_switch = StringVar(None, "cm")
radio_switch_ex = StringVar(None, "c")
root["bg"] = "white"
frame["bg"] = "white"

Label(frame, text="Export To CSV", font=("Arial", 16), bg="white", pady=5).grid(row=0,columnspan=5,column=0, sticky=W+E+N+S)
Radiobutton(frame, text="Chen Values", variable=radio_switch_ex, value="c", bg="white", padx=1, pady=5).grid(row=1,column=1, columnspan=1)
Radiobutton(frame, text="McGuire Values", variable=radio_switch_ex, value="m", bg="white",pady=5).grid(row=1, column=1, columnspan=3)
Label(frame, text="From Atomic Number ", font=("Arial", 12), bg="white", pady=5).grid(row=2,column=0, sticky=W+E+N+S)
from_an = Entry(frame, justify=CENTER, bg="#e4e8e8", borderwidth=0, font=("Arial", 13))
from_an.grid(row=2, column=1, sticky=W+E+N+S)
Label(frame, text="   To", font=("Arial", 12), bg="white", pady=5).grid(row=2,column=2, sticky=W+E+N+S)
to_an = Entry(frame, justify=CENTER, bg="#e4e8e8", borderwidth=0, font=("Arial", 13))
to_an.grid(row=2, column=3, sticky=W+E+N+S, padx=10)
Button(frame, text="Export", command=exportcsv, bg="#2c3e50", fg="white" , padx=10, borderwidth=0).grid(row=2,column=4)

Label(frame, text="________________________________________________\n\nQuick View", font=("Arial", 16), bg="white", pady=5).grid(row=3,columnspan=5,column=0, sticky=W+E+N+S)
Label(frame, text="Enter Atomic Number:", font=("Arial", 12), bg="white", pady=5).grid(row=4,columnspan=5,column=0, sticky=W+E+N+S)
element = Entry(frame, justify=CENTER, bg="#e4e8e8", borderwidth=0, font=("Arial", 13))
element.grid(row=5,columnspan=5,column=0, sticky=W+E+N+S)
Radiobutton(frame, text="Chen Values", variable=radio_switch, value="c", bg="white", padx=1, pady=5).grid(row=6,column=0, columnspan=2)
Radiobutton(frame, text="McGuire Values", variable=radio_switch, value="m", bg="white").grid(row=6, column=1, columnspan=2)
Radiobutton(frame, text="Both Chen and McGuire Values", variable=radio_switch, value="cm", bg="white").grid(row=6, column=2, columnspan=2)
mcg_results = Label(frame, text="", font=("Arial", 13), bg="white",pady=10)
chen_results = Label(frame, text="", font=("Arial", 13), bg="white",pady=10)
element.bind("<Return>", computation)
Button(frame, text="Generate", command=computation, bg="#2c3e50", fg="white" , padx=10, borderwidth=0).grid(row=7,columnspan=5,column=0)
root.mainloop()
