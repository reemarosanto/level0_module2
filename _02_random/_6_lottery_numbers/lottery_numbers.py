import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':

    window = Tk()
    window.withdraw()

    # TODO 1) Get 6 random numbers to put on your lottery ticket
    lottery_number = random.randint(0, 100)
    lottery_number_2 = random.randint(0, 100)
    lottery_number_3 = random.randint(0, 100)
    lottery_number_4 = random.randint(0, 100)
    lottery_number_5 = random.randint(0, 100)
    lottery_number_6 = random.randint(0, 100)
    # TODO 2) Display the selected numbers to the user in a pop-up
    messagebox.showinfo(message="Your lottery numbers are \n" + str(lottery_number) + " " + str(lottery_number_2) + " " + str(lottery_number_3) + " " + str(lottery_number_4) + " " + str(lottery_number_5) + " " + str(lottery_number_6))
    # TODO 3) BONUS: Set the title of the pop-up to show it is a lottery ticket
