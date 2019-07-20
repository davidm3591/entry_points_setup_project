from extraction_pptx import *
from tkinter import *

########################################################################
# Extraction Tool GUI
# Edgenuity, Inc.
########################################################################
# GUI code (main) to start Extraction Tool program - calls get_file()
# on start button click.
# - 07/04/2019 drm
########################################################################




def extract_open():
    """Create GUI to launch extraction_tool."""
    root = Tk()
    root.geometry("425x160")
    root.title("Edgenuity Extraction Tool")
    root.iconbitmap("edge_img.ico")

    def update_import(update_text):
        print("Import Started")
        ppt_file_display.config(text=update_text)

    powerpoint_desc = Label(root, text="Current PowerPoint source file")
    powerpoint_file = Label(root, text="PPT: ", font=(None, 11))
    ppt_file_display = Label(root, text="file.pptx")
    action_desc = Label(root, text="Action (current)")
    # action_current = Label(root, text = "")
    slide_desc = Label(root, text="Slide:")
    slide_number = Label(root, text="")

    start_button = Button(
        root, text="Start",
        font=(None, 10),
        command=get_file
    )

    powerpoint_desc.grid(row=0, column=0, padx=10)
    powerpoint_file.grid(row=1, column=0, padx=10, sticky=W)
    ppt_file_display.grid(row=1, column=0)
    action_desc.grid(row=2, column=0, pady=15)
    # action_current.grid(row = 2, column = 0, padx = 5, pady = 15)
    slide_desc.grid(row=2, column=1, pady=15)
    slide_number.grid(row=2, column=2, pady=15, sticky=W)
    start_button.grid(row=3, column=2, padx=80, pady=25, ipadx=35)

    root.mainloop()
