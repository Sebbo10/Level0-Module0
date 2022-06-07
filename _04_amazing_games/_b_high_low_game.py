from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print.random_num()
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(9)
        # 4. Ask the user for a guess using a pop-up window, and save their response
        message = simpledialog.askstring(title="guess",prompt="Guess the number")
        # 5. If the guess is correct
        if message == random_num:
            sys.exit(0)
        # 6. Win. Use 'sy to end the program
        if message > random_num:
            messagebox(title= "high", message="Your guess is high")
        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low
        if message < random_num

#do da thing that you want to do
    #11. Outside of the loop, tell the user they lost

    window.mainloop()
