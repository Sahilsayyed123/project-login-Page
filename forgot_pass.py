from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import smtplib
import string
import random


cnx = mysql.connector.connect(
    user='root', password='msd10911', database='login')
cursor = cnx.cursor()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()


r = Tk()
r.geometry('875x470')
r['bg'] = 'white'
sql = ("select password from page where email ="''" %s"''"")


def back(new2):
    r.destroy()
    import project_login
    new2.destroy()


def reset():
    email = (email_entry.get())
    data = (email,)
    cursor.execute(sql, data)
    ab = cursor.fetchone()

    S = 6
    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k=S))
    otp = str(ran)
    data1 = (otp, email)
    sql1 = ("update page set OTP ="''"%s"''" where email ="''"%s"''"")
    cursor.execute(sql1, data1,)
    cnx.commit()

    server.login("sahilsayyed0409@gmail.com", "qldfxklffpealjuq")

    if (email == ""):
        messagebox.showerror("ERROR", "Something is missing")

    else:
        messagebox.showinfo("Hello", "Please Check your email")
        msg = "\r\n".join(["Please do not share! your OTP is", str(ran),])
        server.sendmail("sahilsayyed0409@gmail.com", email, msg)


header = Label(r, text='FORGOT ', font=(
    'Lucida Fax', 30), bg='white', fg="#4120A9")
header2 = Label(r, text='YOUR PASSWORD ? ', font=(
    'Lucida Fax', 30), bg='white', fg="#4120A9")
text1 = Label(r, text="you can reset your password here",
              font=('Lucida Sans', 14), bg='white', fg="#4120A9")
email = Label(r, text="Email Address", font=(
    'Lucida Sans', 16), bg='white', fg="#4120A9")
email_entry = Entry(r, bd=5, font=('Lucida Sans', 14),
                    width=31, bg='white', fg="#9571D5")
button = Button(r, text="Send Password", command=reset, font=('Lucida Fax', 14),
                width=31, bg="#4120A9", activebackground="#9571D5", fg='white', cursor='hand2')
image = Image.open(
    "C:\PERSONAL PROJECTS\project-login-Page\images\loggedin.webp")
re_image = image.resize((420, 470), Image.ANTIALIAS)
image = ImageTk.PhotoImage(re_image)
Label(r, image=image, bg='white', fg="#4120A9").place(x=0, y=0)
header.place(x=450, y=40)
header2.place(x=450, y=100)
text1.place(x=450, y=190)
email.place(x=450, y=260)
email_entry.place(x=450, y=295)
button.place(x=450, y=355)

r.mainloop()
