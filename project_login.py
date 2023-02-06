from atexit import register
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector

cnx = mysql.connector.connect(
    user='root', password='msd10911', database='login')
cursor = cnx.cursor()

r = Tk()
r.title('Login page')
r['bg'] = "white"


def register():
    ask = messagebox.askquestion("Hello", "Do you want to Register first ?")
    if (ask == 'yes'):
        r.destroy()
        import project_input


def submit():
    user = (t1.get())
    pass1 = (t2.get())
    data = (user,)

    sql = ("select password from page where username ="''" %s"''"")

    cursor.execute(sql, data)
    ab = cursor.fetchone()

    if (pass1 == "" and user != ""):
        l3.config(text="Something is missing !", bg='white', fg="red")

    if (user == "" and pass1 != ""):
        l3.config(text="Invalid Username or Password !", bg='white', fg="red")
    if (pass1 != ab[0]):
        l3.config(text="Incorrect Password !", bg='white', fg="red")

    if (pass1 == ab[0]):
        cnx.close()
        r.destroy()
        import logged_in


def forgot():
    r.destroy()
    import forgot_pass


r.geometry('840x470')
mainl = Label(r, text="Welcome", font=(
    'Bahnschrift Light', 18), bg='white', fg='#0B1F65')
mainl2 = Label(r, text="Log into your account", font=(
    'Bahnschrift SemiBold', 18), bg='white', fg='#0B1F65')
l1 = Label(r, text='username', font='TimesNewRoman', bg='white', fg='#0B1F65')
l2 = Label(r, text='password', font='TimesNewRoman', bg='white', fg='#0B1F65')
l3 = Label(r, text=None, bg='white')
t1 = Entry(r, bd=5, font=('TimesNewRoman', 13),
           bg='white', width=35, fg='#16488F')
t2 = Entry(r, bd=5,  show=None, font=(
    'TimesNewRoman', 13), bg='white', fg='#16488F')
t2 = Entry(r, bd=5, show='*', font=('TimesNewRoman', 13),
           bg='white', width=35, fg='#16488F')
d = Button(r, text='Login', command=submit, width=29, bg="#0B1F65",
           activebackground="#16488F", fg="white", cursor="hand2", font='TimesNewRoman')
e = Button(r, text='Forgot Password ?', command=forgot,
           width=16, bg='white', fg='blue', cursor='hand2')
s1 = Button(r, text="Register", command=register, width=29, bg="#0B1F65",
            activebackground="#16488F", fg="white", cursor="hand2", font='TimesNewRoman')
image = Image.open("C:/PERSONAL PROJECTS/project-login-Page/images/login.webp")
re_image = image.resize((420, 470), Image.ANTIALIAS)
image = ImageTk.PhotoImage(re_image)
Label(r, image=image, bg='white', fg="#4120A9").place(x=0, y=0)


mainl.place(x=225+323, y=8+63)
mainl2.place(x=164+323, y=43+63)

l1.place(x=120+323, y=115+63)
t1.place(x=120+323, y=145+63)
l2.place(x=120+323, y=180+63)
t2.place(x=120+323, y=210+63)


s1.place(x=120+323, y=280+110)
d.place(x=120+323, y=280+63)
e.place(x=322+323, y=180+63)
l3.place(x=218+323, y=250+63)


r.eval('tk::PlaceWindow . right')
r.mainloop()
