import pandas as pd
import numpy as np
import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from functools import partial

filepath = ''


def open_file():
    """Open a file for reading"""
    filepath = askopenfilename(
        filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    print(filepath)
    lbl_csv_file['text'] = "Filename: " + str(os.path.basename(filepath))
    filepath = filepath


def run(filepath):
    print(filepath)
    delimiter = ent_delimiter['text']
    if delimiter not in [';', ',', '|']:
        delimiter = ';'
    print(delimiter)
    df = pd.read_csv(filepath, delimiter=delimiter)
    print(df)
    groups = df.groupby(np.arange(len(df.index)) / 10000)
    for (frameno, frame) in groups:
        filename = groups.get_group(frameno).values[0][0].replace(':', '')
        frame.to_csv(f'{filename}.csv', sep=delimiter,
                     header=True, index=False, encoding="ISO-8859-1")


window = tk.Tk()
window.title("Simple CSV Splitter")
#window.rowconfigure(3, minsize=50, weight=1)
#window.columnconfigure(1, minsize=50, weight=1)
frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()
lbl_csv_file = tk.Label(master=frm_form, text="Select CSV file...")
btn_csv_file = tk.Button(
    master=frm_form, text="Open", command=open_file)
lbl_csv_file.grid(row=0, column=0, sticky="e")
btn_csv_file.grid(row=0, column=2, sticky="e")
lbl_delimiter = tk.Label(master=frm_form, text="Specify delimiter:")
ent_delimiter = tk.Entry(master=frm_form, width=3)
lbl_delimiter.grid(row=1, column=0, sticky="e")
ent_delimiter.grid(row=1, column=1)
ent_delimiter.insert(tk.END, ';')

btn_run = tk.Button(
    master=frm_form, text="Run", command=partial(run, filepath))
btn_run.grid(row=2, column=2, sticky="e")

#delimiter = ';'
#org_file = 'test.csv'
#df = pd.read_csv(org_file, delimiter=delimiter)

#groups = df.groupby(np.arange(len(df.index))/10000)
# for (frameno, frame) in groups:
#filename = groups.get_group(frameno).values[0][0].replace(':', '')
#frame.to_csv("%s.csv" % filename, sep=delimiter, header=True, index=False, encoding="ISO-8859-1")
# frame.to_csv(f'{filename}.csv', sep=delimiter, header=True,
#            index=False, encoding="ISO-8859-1")

window.mainloop()
