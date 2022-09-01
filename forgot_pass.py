from tkinter import*
from PIL import Image,ImageTk
import mysql.connector


cnx = mysql.connector.connect(user='root',password='Pass@123', database='login')
cursor = cnx.cursor()


r=Tk()
r.geometry('875x470')
r['bg']='white'
sql=("select password from page where email ="''" %s"''"")


def back(new2):
    r.destroy()
    import project_login
    new2.destroy()


def reset():
    email=(email_entry.get())
    data=(email,)
    cursor.execute(sql,data)
    ab=cursor.fetchone()
    print("hello")

    if (email==""):
        new=Toplevel(r)
        new.title("Error !!")
        new['bg']='white'
        new.geometry('400x300')
        lql=Label(new,text="ERROR",font=('Sans Serif',13))
        lql.place(x=0,y=0)

    elif(email==sql):
        new1=Toplevel(r)
        new1.title("Error !!")
        new1['bg']='white'
        new1.geometry('400x300')
        lql1=Label(new1,text=ab[0],font=('Sans Serif',13))
        lql1.place(x=0,y=0)

    else:
        new2=Toplevel(r)
        new2.title("Important !!")
        new2.geometry('670x300')
        new2['bg']='white'
        lqll2=Label(new2,text="This is your password plss dont share with anyone !!",font=('Sans Serif',20),fg='Light blue',bg='white')
        lql2=Label(new2,text=ab[0],font=('Times New Roman',23),fg="violet",bg="Light Blue")
        bbt=Button(new2,text="Go Back",command=lambda:back(new2),font=('Times New Roman',23),fg="violet",bg="Light Blue")
        lql2.place(x=20,y=60)
        lqll2.place(x=20,y=20)
        bbt.place(x=250,y=100)


header=Label(r,text='FORGOT ',font=('Lucida Fax',30),bg='white',fg="#4120A9")
header2=Label(r,text='YOUR PASSWORD ? ',font=('Lucida Fax',30),bg='white',fg="#4120A9")
text1=Label(r,text="you can reset your password here",font=('Lucida Sans',14),bg='white',fg="#4120A9")
email=Label(r,text="Email Address",font=('Lucida Sans',16),bg='white',fg="#4120A9")
email_entry=Entry(r,bd=5,font=('Lucida Sans',14), width=31,bg='white',fg="#9571D5")
button=Button(r,text="Reset Password",command=reset,font=('Lucida Fax',14),width=31,bg="#4120A9",activebackground="#9571D5",fg='white',cursor='hand2')
image=Image.open("C:/Users/ilmuser/Downloads/ffs.webp")
re_image=image.resize((420,470),Image.ANTIALIAS)
image=ImageTk.PhotoImage(re_image)
Label(r,image= image,bg='white',fg="#4120A9").place(x=0,y=0)
header.place(x=450,y=40)
header2.place(x=450,y=100)
text1.place(x=450,y=190)
email.place(x=450,y=260)
email_entry.place(x=450,y=295)  
button.place(x=450,y=355)

r.mainloop()