from tkinter import *
from extraction_pptx import read_file
# Build Tkinter App for Testing Setup/Entry Scritps


def extract_open():
    root = Tk()

    edge_label = Label(root, text=" Edgenuity Extraction Tool \n")
    edge_inc = Label(root, text=" Edgenuity, Inc.")
    start_app_button = Button(root, text="Start", padx=10,
                              pady=2, command=read_file)

    edge_inc.pack()
    edge_label.pack()
    start_app_button.pack(side=RIGHT)

    root.mainloop()
