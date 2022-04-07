from tkinter import messagebox, simpledialog, Tk

# Create an if-main code block 
if __name__ == '__main__':
    
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # Ask the user for their name and save it to a variable
    name = simpledialog.askstring(title='Fricker', prompt="What is your name?")
    
    # Show a message box with your message using the .showinfo() method
    messagebox.showinfo(title='Fricker', message='Frick You '+name)
    # Print your message to the console using the print() function
    print('This is a Poop Box '+name)
    # Show an error message using messagebox.showerror()
    messagebox.showerror(title= 'Fricker', message='This is an error, Frick You '+name)
    # Run the window's .mainloop() method

    window.mainloop()
    pass
