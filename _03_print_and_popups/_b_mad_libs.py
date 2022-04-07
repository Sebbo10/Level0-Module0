from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Put this sentence in a pop-up message box:
    # "If you find yourself having to cross a piranha-infested river, here's how to do it..."
    messagebox.showinfo(title='Piranha River', message= "If you find yourself having to cross a piranha-infested river, here's how to do it...")
    # Get the player to enter an adjective
    adj = simpledialog.askstring(title= 'Piranha River' , prompt= 'Adjective')
    # Get the player to enter a type of liquid
    top = simpledialog.askstring(title= 'Piranha River' , prompt= 'Type of Liquid')
    # Get the player to enter a body part
    bp = simpledialog.askstring(title= 'Piranha River' , prompt= 'Body Part')
    # Get the player to enter a verb
    v = simpledialog.askstring(title= 'Piranha River' , prompt= 'Verb')
    # Get the player to enter a place
    p = simpledialog.askstring(title= 'Piranha River' , prompt= 'Place')
    # The story below has has been written as a group of Strings joined
    # together by + signs. The story contains place holders, indicated
    # by [** **] which you need to replace with the values entered by the
    # player.
    # Hint: You will need to add more + signs to join the variables to the
    #       other parts of the story.

    story = (
        "Piranhas are more " +adj+ " during the day, so cross the river at\n"
        "night. Piranhas are attracted to fresh " +top+ " and will most\n"
        "likely take a bite out of your " +bp+ " if you " +v+ " Whateveryou do, if you have an open wound, try to find another way to get "
        "back to the " +p+". Good luck!"
    )

    # Make a pop-up that contains the final story. The \n escape characters add
    # line breaks to the story. If you need to, move them around to make your
    # story look better in the pop-up
    messagebox. showerror(title='story', message= "Piranhas are more" +adj+ "during the day, so cross the river at\n"
        "night. Piranhas are attracted to fresh" +top+ "and will most\n"
        "likely take a bite out of your" +bp+ "if you" +v+ "Whatever\n"
        "you do, if you have an open wound, try to find another way to get "
        "back to the" +p+". Good luck!")
    # If you want to write your own Madlib story, just change the story variable
    # and ask the player different questions.

    # Run the window's .mainloop() method

    pass
