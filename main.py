import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

def fetch_image(url):
    response = requests.get(url)
    img = ImageTk.PhotoImage(Image.open(BytesIO(response.content)))
    return img

# Fetch images using the function
icon_url = "https://upcdn.io/W142iQE/raw/imageApi/icon.png"
bg_url = "https://upcdn.io/W142iQE/raw/imageApi/bg.jpg"
login_url = "https://upcdn.io/W142iQE/raw/imageApi/login.png"
uname_url = "https://upcdn.io/W142iQE/raw/imageApi/uname.png"
pass_url = "https://upcdn.io/W142iQE/raw/imageApi/pass.png"

def login():
    if uname_entry.get() == '' or pass_entry.get() == '': 
        messagebox.showerror('ERROR', 'Please enter your credentials')
    elif uname_entry.get() == 'admin' and pass_entry.get() == 'admin@123':
        root.destroy()
        import sms
    else:
        messagebox.showerror('ERROR', 'Please Enter Correct Credentials')
        
root = tk.Tk()

# create window
root.geometry('1280x720+275+100')
root.resizable(0,0)
root.title('Sistem Manajemen Siswa')

#icon for the window
icon = fetch_image(icon_url)
root.iconphoto(False, icon)

# add background image
bg_img = fetch_image(bg_url)

bg_label = tk.Label(root, image=bg_img)
bg_label.place(x=0, y=0)

# create a frame
login_frame = tk.Frame(root, bg='#f5f5f5')
login_frame.place(x=425, y=250)

# load the login logo image
login_img = fetch_image(login_url)

# create a label widget to display the login logo image
login_label = tk.Label(login_frame, image =login_img, width=128, height=128)
login_label.grid(row=3, column=0, padx=20, pady=10)


# create username
uname_img = fetch_image(uname_url)

uname_label = tk.Label(login_frame, image=uname_img, text='Username', compound='left', font=('Comic Sans MS', 15, 'bold'))
uname_label.grid(row= 1, column=0, padx=20, pady=10)
uname_entry = tk.Entry(login_frame, font=('Comic Sans MS', 15, 'bold'), bd=3, fg='#a713da')
uname_entry.grid(row=1, column=1)


# create password
pass_img = fetch_image(pass_url)

pass_label = tk.Label(login_frame, image = uname_img, text='Password', compound='left', font=('Comic Sans MS', 15, 'bold'))
pass_label.grid(row= 2, column=0, padx=20, pady=10)
pass_entry = tk.Entry(login_frame, font=('Comic Sans MS', 15, 'bold'), bd=3, fg='#a713da')
pass_entry.grid(row=2, column=1)

# create login button
login_button = tk.Button(login_frame, text='LOGIN', font=('Comic Sans MS', 13, 'bold'), width=13, cursor='hand2', command=login)
login_button.grid(row=3,column=1, pady=10)

root.mainloop()
