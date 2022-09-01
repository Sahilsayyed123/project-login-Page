# # from tkinter import *
# # from PIL import ImageTk, Image
# # # master = Tk()

# # # w = Canvas(master, width=250, height=200)
# # # w.create_rectangle(0, 0, 100, 100, fill="blue", outline = 'blue')
# # # w.create_rectangle(50, 50, 100, 100, fill="red", outline = 'blue') 
# # # w.pack()
# # # master.mainloop()

# # # Imports PIL module 
# # from PIL import Image
  
# # # open method used to open different extension image file
# # im = Image.open(r"C:/Users/ilmuser/Downloads/wallpaperflare.com_wallpaper.jpg")
# # # This method will show image in any image viewer 
# # im.show() 
# # Create an instance of tkinter window
# # win = Tk()

# # # Define the geometry of the window
# # win.geometry("700x500")

# # frame = Frame(win, width=600, height=400)
# # frame.pack()
# # frame.place(anchor='center', relx=0.5, rely=0.5)
# # canvas= Canvas(win, width= 600, height= 400)
# # canvas.pack()
# # # Create an object of tkinter ImageTk
# # img = ImageTk.PhotoImage(Image.open("C:/Users/ilmuser/Downloads/wallpaperflare.com_wallpaper.jpg"))
# # resized_image= img.resize((300,205), Image.ANTIALIAS)
# # new_image= ImageTk.PhotoImage(resized_image) 
# # canvas.create_image(10,10, anchor=NW, image=new_image)
# # # Create a Label Widget to display the text or Image
# # label = Label(frame, image = img)
# # label.pack()

# # win.mainloop()

# #Import tkinter library
# from tkinter import *
# from PIL import Image, ImageTk
# #Create an instance of tkinter frame
# win= Tk()
# #Set the Geometry
# win.geometry("750x250")
# #Open a New Image
# image= Image.open("C:/Users/ilmuser/Downloads/wallpaperflare.com_wallpaper.jpg")
# #Resize Image using resize function
# resized_image= image.resize((300,225), Image.ANTIALIAS)
# #Convert the image into PhotoImage
# img = ImageTk.PhotoImage(resized_image)
# #Create a label for the image
# Label(win,image= img).pack(pady=20)
# win.mainloop()

# import webbrowser

    

# def callback():
#     webbrowser.open_new(r"http://www.google.com")

# root = Tk()
# frame = Frame(root, bg="white")
# frame.pack(expand=True, fill="both")

#     # Creates a button that, when clicked, calls the function that sends you to your hyperlink.
# link=Button(frame, text="Google Hyperlink",command=callback)
# link.pack(padx=10, pady=10)
# root.mainloop()


#Import the required library
from tkinter import*

#Create an instance of tkinter frame
win= Tk()

#Define geometry of the window
win.geometry("750x250")

#Define a function to close the popup window
def close_win(top):
   top.destroy()
def insert_val(e):
   e.insert(0, "Hello World!")

#Define a function to open the Popup Dialogue
def popupwin():
   #Create a Toplevel window
   top= Toplevel(win)
   top.geometry("750x250")

   #Create an Entry Widget in the Toplevel window
   entry= Entry(top, width= 25)
   entry.pack()

   #Create a Button to print something in the Entry widget
   Button(top,text= "Insert", command= lambda:insert_val(entry)).pack(pady= 5,side=TOP)
   #Create a Button Widget in the Toplevel Window
   button= Button(top, text="Ok", command=lambda:close_win(top))
   button.pack(pady=5, side= TOP)
#Create a Label
label= Label(win, text="Click the Button to Open the Popup Dialogue", font= ('Helvetica 15 bold'))
label.pack(pady=20)

#Create a Button
button= Button(win, text= "Click Me!", command= popupwin, font= ('Helvetica 14 bold'))
button.pack(pady=20)
win.mainloop()