import tkinter as tk
from tkinter import ttk
from prime_calc import prime_tal

class App():
    def __init__(self):
        self.root = tk.Tk() # makes self.root a tk window

        self.root.geometry('380x300') # sets window size

        self.root.title('Prime Numbers') # sets the text att the top bar of the program

        self.mainframe = tk.Frame(self.root, background='white') # a frame to put stuff in
        self.mainframe.pack(fill='both', expand=True) # makes the frame cover the whole window

        self.header = ttk.Label(self.mainframe, text='Prime Numbers', 
                    background='white', font=("Brass Mono", 30)) # a text box placed in mainframe
        self.header.grid(row=1, column=0,pady=10,padx=10) # puts the text in the grid

        text1 = 'Enter an integer representing\n the highest number you want\n to check if its a prime number'
        self.text1 = ttk.Label(self.mainframe, text=text1, 
                    background='white', font=("Brass Mono", 10)) # a text box placed in mainframe
        self.text1.grid(row=2, column=0,padx=10) # puts the text in the grid

        self.In_File = tk.BooleanVar() # a boolean that checks if the program calls self.In_File.get()
        self.Check_Button = tk.Checkbutton(self.mainframe, text='In .txt file',variable=self.In_File, 
                                 onvalue=True, offvalue=False) # the checkbutton
        self.Check_Button.grid(row=2,column=1) # the position of the checkbutton

        self.set_text_field = ttk.Entry(self.mainframe) # a field where you can enter text
        self.set_text_field.grid(row=3,column=0, pady=5, padx=10, sticky='NWES') # places the text box in rhe grid

        set_text_button = ttk.Button(self.mainframe, text='Enter', command=self.get_n) # makes a button
        set_text_button.grid(row=3, column=1, pady=5) # places the button next to the text box

        self.text2 = ttk.Label(self.mainframe, text="", 
                    background='white', font=("Brass Mono", 10),
                    wraplength=350) # a text box placed in mainframe
        self.text2.grid(row=4, column=0, columnspan = 2, sticky = tk.W+tk.E, pady=5, padx=10) # puts the text in the grid

        self.root.mainloop() # makes the tk window apper on screen
        
    
    def get_n(self):
        if __name__ == "__main__":
            if self.In_File.get():
                f=open('..\prime_numbers.txt','w')
                f.write(prime_tal(int(self.set_text_field.get())))
                self.set_text_field.delete(0, 'end')
            else:
                output = prime_tal(int(self.set_text_field.get()))
                self.text2.config(text=output)
                self.set_text_field.delete(0, 'end')

if __name__ == "__main__":
    App()