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
    # sql=('''select username from page''')
    # cursor.execute(sql)
    # result=cursor.fetchall()
    # for i in result:
    #     print(i[0])



    



    add_page = ("INSERT INTO page "
               "(first_name, last_name, username, email, password, cpassword) "
               "VALUES (%s, %s, %s, %s, %s, %s)")
    data_page = (firstname, lastname, username, email, password, cpassword)
    

    
    # if(username==i[0]):
    #     l7.config(text="name already taken",fg='red')
    if(password == cpassword  and username and '@'in email and password and cpassword and firstname!= "" ):

        cursor.execute(add_page, data_page)

        cnx.commit()

        cursor.close()
        cnx.close()  
        r.destroy()
        import project_login      
  
    if (firstname and lastname and username and email and password and cpassword != "" and password != cpassword):
        l7.config(text="passwords do no match!",fg='red')

    if not firstname.isalpha() or not lastname.isalpha():
        l7.config(text="Invalid firstname or lastname",fg='red')

    else:
        l7.config(text="something is missing!",fg='red')
r.geometry('393x250')
l1=Label(r,text="First name",font=('Times New Roman',13))
t1=Entry(r,bd=5,font=('Times New Roman',13))
l2=Label(r,text="Last name",font=('Times New Roman',13))
t2=Entry(r,bd=5,font=('Times New Roman',13))
l3=Label(r,text="Username",font=('Times New Roman',13))
t3=Entry(r,bd=5,font=('Times New Roman',13))
l4=Label(r,text="Email",font=('Times New Roman',13))
t4=Entry(r,bd=5,font=('Times New Roman',13))
l5=Label(r,text="Password",font=('Times New Roman',13))
t5=Entry(r,bd=5,show=None,font=('Times New Roman',13))
t5=Entry(r,bd=5,show='*',font=('Times New Roman',13))
l6=Label(r,text="Confirm-Password",font=('Times New Roman',13))
t6=Entry(r,bd=5,show=None,font=('Times New Roman',13))
t6=Entry(r,bd=5,show='*',font=('Times New Roman',13))
bt=Button(r,text="Submit",command=lambda: submit(),width=10,bg="light blue",fg="black",cursor="hand2")
l7=Label(r,text="",font=('Times New Roman',10))

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
bt.place(x=153, y=190)


l7.place(x=137, y=166)

r.mainloop()