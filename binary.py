from tkinter import *

# setting the root
root = Tk()

# setting screen size
root.geometry('700x700')

# setting the title
root.title('Convert text to binary')

# setting background color
root.config(bg="#B2BEB5")

welcome = Label(root, text='Welcome to Text to binary.',
                bg='#B2BEB5', font=('Arial', 12))
welcome.pack()

enter = Entry(root, bg='#B2BEB5', borderwidth=5)
enter.pack()

# create a label widget to display the binary representation
binary_output = Label(root, text='', bg='#B2BEB5', font=('Arial', 12))
binary_output.pack()

# Convert user's input to binary


def user():
    text = enter.get()
    output = "".join(format(ord(char), "08b") for char in text)
    binary_output.config(
        text="Binary representation of: " + text + " is " + output)


submit = Button(root, text='Convert', bg='#B2BEB5',
                command=user, borderwidth=5, font=('Arial', 12))
submit.pack()

root.mainloop()
