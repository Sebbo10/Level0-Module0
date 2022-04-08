from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    answer = simpledialog.askinteger(title = 'earth' , prompt = 'How many people are on earth? use number')
    if answer==8000000000:
        score = score + 1
        print(score)
    else:
        score = score - 1
    #      // 3.  Use an if statement to check if their answer is correct
    answer = simpledialog.askstring(title = 'Minecraft' , prompt = 'Who is the best minecraft speedrunner?')
    if answer== 'Cube1337x':
        score = score + 1
        print(score)
    else:
        score = score - 1
    #      // 4.  if the user's answer was correct, add one to their score 
    answer = simpledialog.askinteger(title = 'Cars' , prompt = 'what number is lightning macqueens number')
    if answer== 95:
        score = score + 1
        print(score)
    else:
        score = score - 1
    # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
    #      // Option: Subtract a point from their score for a wrong answer
 
    # After all the questions have been asked, tell the user their final score
    # remember to convert your variable to a string using the str() function 
    
    # Run the window's .mainloop() method
