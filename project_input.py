from tkinter import*
from tkinter import messagebox

import mysql.connector


cnx = mysql.connector.connect(user='root',password='Pass@123', database='login')
cursor = cnx.cursor()


r = Tk()
f = ("Times bold", 14)
r.title("Sign-in page")
r['bg']="white"
r.geometry('393x450')

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
    
    if any(ch.isdigit() for ch in firstname):
        l7.config(text = 'Invalid Username or Password',fg="red")

    elif any(ch1.isdigit() for ch1 in lastname):
        l7.config(text = 'Invalid Username or Password',fg="red")

    elif(password == cpassword  and username and '@' not in email and password and cpassword and firstname!= "" ):
        l7.place(x=150, y=370)
        l7.config(text = 'Invalid Email',fg="red")   

  
    elif(password == cpassword  and username and '@' in email and password and cpassword and firstname!= "" ):

        cursor.execute(add_page, data_page)
        cnx.commit()
        cursor.close()
        cnx.close()  
        r.destroy()
        import project_login
    if (firstname and lastname and username and email and password and cpassword != "" and password != cpassword):
        l7.place(x=135, y=370)
        l7.config(text="Passwords do not match !",fg='red')


    # if not firstname.isalpha() or not lastname.isalpha():
    #     l7.config(text="Invalid First Name or Last Name !",fg='red')
        # messagebox.showerror("ERROR", "Invalid First name or Last name")

    # if ( username or email or password or cpassword == ""):
    #     l7.config(text="something is missing!",fg='red')
        # messagebox.showerror("ERROR", "something is wrong")
    # if any(ch.isdigit() for ch in firstname):
    #     l7.config(text = 'Name can\'t have numbers',fg="red")


        





mainl=Label(r,text='Register',font=('Bahnschrift SemiBold',18),fg="#340744",bg='white')
l1=Label(r,text="First name",font=('Times New Roman',13),fg="#340744",bg='white')
t1=Entry(r,bd=5,font=('Times New Roman',13),fg="#81599F",bg='white')
l2=Label(r,text="Last name",font=('Times New Roman',13),fg="#340744",bg='white')
t2=Entry(r,bd=5,font=('Times New Roman',13),fg="#81599F",bg='white')
l3=Label(r,text="Username",font=('Times New Roman',13),fg="#340744",bg='white')
t3=Entry(r,bd=5,font=('Times New Roman',13),fg="#81599F",bg='white')
l4=Label(r,text="Email",font=('Times New Roman',13),fg="#340744",bg='white')
t4=Entry(r,bd=5,font=('Times New Roman',13),fg="#81599F",bg='white')
l5=Label(r,text="Password",font=('Times New Roman',13),fg="#340744",bg='white')
t5=Entry(r,bd=5,show=None,font=('Times New Roman',13),fg="#81599F",bg='white')
t5=Entry(r,bd=5,show='*',font=('Times New Roman',13),fg="#81599F",bg='white')
l6=Label(r,text="Confirm-Password",font=('Times New Roman',13),fg="#340744",bg='white')
t6=Entry(r,bd=5,show=None,font=('Times New Roman',13),fg="#81599F",bg='white')
t6=Entry(r,bd=5,show='*',font=('Times New Roman',13),fg="#81599F",bg='white')
bt=Button(r,text="Register",command=lambda: submit(),width=20,bg="#81599F",activebackground="Light blue",fg="black",cursor="hand2",font=('Times New Roman',14))
l7=Label(r,text="",font=('Times New Roman',10),bg="white")

mainl.place(x=150,y=15)
l1.place(x=40,y=80)
l2.place(x=40,y=130)
l3.place(x=40,y=180)
l4.place(x=40,y=230)
l5.place(x=40,y=280)
l6.place(x=40,y=330)
t1.place(x=180,y=80)
t2.place(x=180,y=130)
t3.place(x=180,y=180)
t4.place(x=180,y=230)
t5.place(x=180,y=280)
t6.place(x=180,y=330)
bt.place(x=90, y=395)
l7.place(x=130, y=370)

r.eval('tk::PlaceWindow . center')
r.mainloop()