from tkinter import*
import mysql.connector

cnx = mysql.connector.connect(user='root',password='Pass@123', database='login')
cursor = cnx.cursor()

r=Tk() 
r.title('Login page') 
 
def submit(): 

    user=(t1.get()) 
    pass1=(t2.get()) 
    data=(user,)

    sql=("select password from page where username ="''" %s"''"")
    # sql1=("select username from page")
    cursor.execute(sql,data)
    ab=cursor.fetchone()
    # s=cursor.fetchmany()


    if (pass1==ab[0]):
        l3.config(text='''Welcome!,logged in 
            successfully''')
        cnx.close()
        r.destroy() 

        import logged_in 
    elif(user or pass1 == ""):
        l3.config(text="Something is missing !", fg='red')
        pass
    # elif(user or pass1 != s):
    #     l3.config(text='Invalid username or password !') 
    else: 
        l3.config(text='Invalid username or password !',fg='red') 
        



    
r.geometry('268x140')   
# e1 = tk.Entry(window, show=None, font=('Arial', 14))   
# e2 = tk.Entry(window, show='*', font=('Arial', 14))
l1=Label(r,text='username',font='TimesNewRoman') 
l2=Label(r,text='password',font='TimesNewRoman') 
l3=Label(r,text=None) 
t1=Entry(r,bd=5,font=('TimesNewRoman',13) )
t2=Entry(r,bd=5,  show = None,font=('TimesNewRoman',13)) 
t2=Entry(r,bd=5,show='*',font=('TimesNewRoman',13)) 
d=Button(r,text='Login',command=submit, width=21,bg="light blue",fg="black",cursor="hand2",font='TimesNewRoman')
# Button(win, text="Button-1",height= 5, width=10).pack()
l1.grid(row=0,column=0)     
l2.grid(row=1,column=0) 
# d.grid(row=3,column=0) 
t1.grid(row=0,column=1) 
t2.grid(row=1,column=1) 
# l3.grid(row=2,column=1) 
r.eval('tk::PlaceWindow . center') 
# d.pack(side=BOTTOM, padx=15, pady=20) 
d.place(x=25, y=90) 
l3.place(x=70, y=60) 
r.mainloop()



