from msilib.schema import Font
from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('Welcome!')


f = ("Times New Roman", 14)

def Exit():
    ws.destroy()

Label(
    ws,
    text='''YOU HAVE SUCCESSFULLY LOGGED IN''',
    padx=20,
    pady=20,
    bg='#80558C',
    font=f,
    fg="white"
).pack(expand=True, fill=BOTH)


Button(
    ws, 
    text="Press to Exit",
    font=f,
    command=Exit,
    cursor="hand2"

    ).pack(fill=X, expand=TRUE, side=LEFT)



ws.eval('tk::PlaceWindow . center')
ws.mainloop()