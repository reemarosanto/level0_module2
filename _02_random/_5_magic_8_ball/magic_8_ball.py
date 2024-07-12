import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    question = simpledialog.askstring(title='Magic 8 Ball', prompt="Ask a question for the Magic 8 Ball")
    # Make a variable and initialize it to a random number between 0 and 3
    number = random.randint(0, 3)
    # If the random number is 0
    if number == 0:
        messagebox.showinfo(message="Yes")
    elif number == 1:
        messagebox.showinfo(message="No")
    elif number == 2:
        messagebox.showinfo(message="Maybe you should ask Google?")
    elif number == 3:
        messagebox.showinfo(message="You will soon see...")
        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
