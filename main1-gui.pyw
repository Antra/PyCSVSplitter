import tkinter
from tkinter import ttk, StringVar
from tkinter.filedialog import askopenfilename
import pandas as pd
import numpy as np


class GUI:
    def __init__(self, window):
        # 'StringVar()' is used to get the instance of input field
        self.input_text = StringVar()
        self.input_text1 = StringVar()
        self.path = ''
        self.delimiter = ''

        window.title("Simple CSV Splitter")
        window.resizable(0, 0)  # this prevents from resizing the window
        window.geometry("700x300")

        ttk.Button(window, text="CSV File",
                   command=lambda: self.set_csv_path()
                   ).grid(row=0, ipadx=5, ipady=5)
        ttk.Entry(window,
                  textvariable=self.input_text,
                  width=70).grid(row=0, column=1, ipadx=1, ipady=1)

        ttk.Label(window, text="Specify delimiter:").grid(
            row=1, ipadx=5, ipady=15)
        self.txt_delimiter = ttk.Entry(
            window, textvariable=self.input_text1, width=3)
        self.txt_delimiter.grid(row=1, column=1, ipadx=1, ipady=1, sticky="w")
        self.txt_delimiter.insert(0, ';')

        ttk.Button(window, text="Run", command=self.run).grid(
            row=2, column=1, ipadx=5, ipady=5, sticky="e")

        ttk.Button(window, text="Quit", command=self.quit).grid(
            row=2, column=2, ipadx=5, ipady=5, sticky="e")

    def set_csv_path(self):
        self.path = askopenfilename()
        self.input_text.set(self.path)

    def run(self):
        delimiter = self.txt_delimiter.get()
        if delimiter not in [';', ',', '|']:
            delimiter = ';'
        path = self.get_csv_path()
        if not path:
            return
        df = pd.read_csv(path, delimiter=delimiter)
        groups = df.groupby(np.arange(len(df.index)) / 10000)
        for (frameno, frame) in groups:
            filename = groups.get_group(frameno).values[0][0].replace(':', '')
            frame.to_csv(f'{filename}.csv', sep=delimiter,
                         header=True, index=False, encoding="ISO-8859-1")

    def get_csv_path(self):
        """Function provides the CSV full file path."""
        return self.path

    def get_delimiter(self):
        """Function provides the delimiter."""
        return self.delimiter

    def quit(self):
        """Function to end the execution."""
        window.destroy()


if __name__ == '__main__':
    window = tkinter.Tk()
    gui = GUI(window)
    window.mainloop()
