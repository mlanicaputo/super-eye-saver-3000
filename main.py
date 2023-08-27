import time
from tkinter import Button, Label, Tk, ttk


def window():
    # configure window
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="LOOK AT SOMETHING 20 FEET AWAY FOR 20 SECONDS!!!").grid(column=0, row=0)
    ttk.Button(frm, text="Ok, did it!", command=root.destroy).grid(column=1, row=0)
    ttk.Button(frm, text="Quit", command=exit).grid(column=1, row=1)
    root.mainloop()
    

def run():
    # sleep for 20 minutes
    # time.sleep(1200)
    time.sleep(1200)

    # create window
    window()


def main():
    run()


if __name__ == "__main__":
    main()