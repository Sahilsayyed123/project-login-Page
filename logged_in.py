from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('Welcome!')
ws['bg']='#5d8a82'

f = ("Times bold", 14)

def back():
    ws.destroy()
    import project_login

    
Label(
    ws,
    text="YOU HAVE SUCCESSFULLY LOGGED IN",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=f
).pack(expand=True, fill=BOTH)


Button(
    ws, 
    text="Go to Login page", 
    font=f,
    command=back
    ).pack(fill=X, expand=TRUE, side=LEFT)



ws.eval('tk::PlaceWindow . center')
ws.mainloop()