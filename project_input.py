from tkinter import*
import mysql.connector

cnx = mysql.connector.connect(user='root',password='Pass@123', database='login')
cursor = cnx.cursor()

r = Tk()
f = ("Times bold", 14)
r.title("Sign-in page")
def submit():
    firstname=(t1.get())
    lastname=(t2.get())
    username=(t3.get())
    email=(t4.get())
    password=(t5.get())
    cpassword=(t6.get())
    
    add_page = ("INSERT INTO page "
               "(first_name, last_name, username, email, password, cpassword) "
               "VALUES (%s, %s, %s, %s, %s, %s)")

    data_page = (firstname, lastname, username, email, password, cpassword)
    
    cursor.execute(add_page, data_page)


    cnx.commit()

    cursor.close()
    cnx.close()
    
    
    if(password == cpassword and lastname and username and email and password and cpassword and firstname != ""):
        r.destroy()
        import project_login
    elif(firstname and lastname and username and email and password and cpassword != "" and password != cpassword):
        l7.config(text="passwords do no match!")
    else:
        l7.config(text="something is missing!")
r.geometry('393x250')
l1=Label(r,text="First name")
t1=Entry(r,bd=5,font=('Arial',13))
l2=Label(r,text="Last name")
t2=Entry(r,bd=5,font=('Arial',13))
l3=Label(r,text="Username")
t3=Entry(r,bd=5,font=('Arial',13))
l4=Label(r,text="Email")
t4=Entry(r,bd=5,font=('Arial',13))
l5=Label(r,text="Password")
t5=Entry(r,bd=5,show=None,font=('Arial',13))
t5=Entry(r,bd=5,show='*',font=('Arial',13))
l6=Label(r,text="Confirm-Password")
t6=Entry(r,bd=5,show=None,font=('Arial',13))
t6=Entry(r,bd=5,show='*',font=('Arial',13))
bt=Button(r,text="Submit",command=lambda: submit())
l7=Label(r,text="")

l2.grid(row=0,column=1)
t2.grid(row=1,column=1)
l4.grid(row=2,column=1)
t4.grid(row=3,column=1)
l6.grid(row=4,column=1)
t6.grid(row=5,column=1)
l1.grid(row=0,column=0)
t1.grid(row=1,column=0)
l3.grid(row=2,column=0)
t3.grid(row=3,column=0)
l5.grid(row=4,column=0)
t5.grid(row=5,column=0)

r.eval('tk::PlaceWindow . center')
bt.place(x=168, y=176)
l7.place(x=135, y=154)
r.mainloop()