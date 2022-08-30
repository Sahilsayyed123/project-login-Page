from tkinter import*
import mysql.connector

cnx = mysql.connector.connect(user='root',password='Pass@123', database='login')
cursor = cnx.cursor()

r=Tk() 
r.title('Login page') 

def Yes():
    r.destroy
    import project_input

def No():
    r.destroy()



def submit(): 

    user=(t1.get()) 
    pass1=(t2.get()) 
    data=(user,)





    if (user or pass1 == ""):
        l3.config(text="Something is missing !", fg='red')
        top= Toplevel(r)
        top.geometry("750x250")
        top.title("!!!!!!")
        lbl=Label(top, text= "Hello Are you new herte!", font=('Mistral 18 bold')).place(x=238,y=40)
        bbt1=Button(top,text='Yes',command=Yes, width=35,bg="light blue",fg="black",cursor="hand2",font='TimesNewRoman').place(x=190,y=80)
        bbt2=Button(top,text='No',command=No, width=35,bg="light blue",fg="black",cursor="hand2",font='TimesNewRoman').place(x=190,y=120)
        pass

    sql=("select password from page where username ="''" %s"''"")

    cursor.execute(sql,data)
    ab=cursor.fetchone()

    if (pass1==ab[0]):
        l3.config(text='''Welcome!,logged in successfully''')
        cnx.close()
        r.destroy()
        import logged_in

    else: 
        l3.place(x=200,y=250)
        l3.config(text='''Invalid username or password !''',fg='red') 

def forgot():
    r.destroy()
    import project_input





    
r.geometry('568x340')   

mainl=Label(r,text="Welcome",font=('Bahnschrift Light',18))
mainl2=Label(r,text="Log into your account",font=('Bahnschrift SemiBold',18))
l1=Label(r,text='username',font='TimesNewRoman') 
l2=Label(r,text='password',font='TimesNewRoman') 
l3=Label(r,text=None) 
t1=Entry(r,bd=5,font=('TimesNewRoman',13), width=35)
t2=Entry(r,bd=5,  show = None,font=('TimesNewRoman',13)) 
t2=Entry(r,bd=5,show='*',font=('TimesNewRoman',13),width=35) 
d=Button(r,text='Login',command=submit, width=35,bg="light blue",fg="black",cursor="hand2",font='TimesNewRoman')
e=Button(r,text='Forgot Password ?',command=forgot,width=16,bg='white',fg='blue',cursor='hand2')


# l1.grid(row=0,column=0)     
# l2.grid(row=2,column=0) 
# d.grid(row=3,column=0) 
# t1.grid(row=1,column=0) 
# t2.grid(row=3,column=0) 
mainl.place(x=225,y=8)
mainl2.place(x=164,y=43)

l1.place(x=120, y=115)
t1.place(x=120, y=145)
l2.place(x=120, y=180)
t2.place(x=120, y=210)


r.eval('tk::PlaceWindow . center') 

d.place(x=120, y=280) 
e.place(x=322,y=180)
l3.place(x=218, y=250) 
r.mainloop()



