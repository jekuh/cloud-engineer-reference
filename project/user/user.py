from tkinter import *

def register_user():
    username = entry_username.get()
    password = entry_password.get()

    # Save the username and password to a file or database
    # You can add additional validation or processing here

    print("Registration Successful!")
    root.destroy()

root = Tk()
root.title("User Registration")

# Create labels and entry fields for username and password
label_username = Label(root, text="Username")
label_username.pack()

entry_username = Entry(root)
entry_username.pack()

label_password = Label(root, text="Password")
label_password.pack()

entry_password = Entry(root, show="*")  # Show * instead of plain text
entry_password.pack()

# Create a button to register the user
register_button = Button(root, text="Register", command=register_user)
register_button.pack()

root.mainloop()
