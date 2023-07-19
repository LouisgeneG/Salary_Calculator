"""
Author  : Louisgene Guillaumette  
Date    : 7/19/2023
Program : salaryGUI_LG.py  (Final Project)

Instructions: Create a GUI-based version of the "Salary Calculator" program that we have 
created in the past. This program should allow the user to input an employee's hourly pay 
and also the amount of hours worked. A button should be used to actually calculate and
display that employee's earnings.
Requirements:
    1. Program must run with a GUI.
    2. GUI must run on the load of the module.
    2. Function to calculate the employee's salary should be handled by a button-click event in the GUI
    3. GUI design should be neat, creative and easy to read.
    4. Code should be documented adequately with docstrings and comments as needed.
        5. Please save this file as :  "salaryGUI" followed by an underscore with your initials.
           For example, my file would be named ("salaryGUI_GM.py"). You do NOT have to also send me
           the breezypythongui.py file (I already have it)

"""

from breezypythongui import EasyFrame
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
# Other imports go here

# Class header (application name will change project to project)
class SalaryCalculator(EasyFrame):
    # Definition of our class constructor method
    def __init__(self):
        #Call to the Easy Frame constrctor method
        EasyFrame.__init__(self, title = "Salary Calculator", width = 350, height = 300, resizable = False, background = "purple")
        self.normalFont = Font(family = "Times New Roman", size = 16)

        #Add the various components to the window
        self.addLabel(text = "Salary Calculator", row = 0, column = 0, columnspan = 2, background = "purple", sticky = "NSEW",
         foreground = "white",  font = Font(family = "Times New Roman", size = 26))
        self.addLabel(text ="Hourly Wage", row = 1, column = 0,sticky = "NW", background = "purple", foreground = "white", font = self.normalFont )
        self.hourlyWage = self.addFloatField(value = 0.0, row = 1, column = 0, sticky = "NE", width = 10)        
        self.addLabel(text ="No. of Hours Worked", row = 2, column = 0,sticky = "NW", background = "purple", foreground = "white", font = self.normalFont )
        self.hoursWorked = self.addFloatField(value = 0, row = 2, column = 0, sticky = "NE", width = 10)

        #Add command button
        self.button = self.addButton(text = "calculate", row = 3, column = 0, columnspan = 2, command = self.calculate)

        #Add a Label and textfield for the result
        self.addLabel(text = "The Employee's Salary is: ", row = 4, column =0, sticky = "NW", background = "purple", foreground = "white", font = self.normalFont)
        self.total = self.addFloatField(value = 0.0, row = 4, column = 0, sticky = "NE",  state = "readonly", width = 10)

    #definition of the calculate() function
    def calculate(self):
        #grab the user input from the GUI window
        rate = self.hourlyWage.getNumber()
        hours = self.hoursWorked.getNumber()
        message = ""
        if rate < 0 or hours < 0:
            messagebox.showinfo("Error", "Hourly pay and hours worked must be positive numbers.")
        if rate == 0 or hours == 0:
            messagebox.showinfo("Information", "All field required.")
        if rate > 0 and hours > 0:
            result = rate * hours
            #display phase
            self.total.setNumber(result)

#Definition of CenterScreenGui() class to put the window on the center Screen
class CenterScreenGui:
    def __init__(self, root):
        self.root = root
        self.root.title("Centered Window")

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y coordinates for the window
        x = (screen_width // 2) - (500 // 2)  # Center horizontally
        y = (screen_height // 2) - (300 // 2)  # Center vertically

        # Set the window size and position
        self.root.geometry(f"500x300+{x}+{y}")

# Global definition of the main() method
def main():
    # instantiate an object from the class into mainloop()
    SalaryCalculator().mainloop()

# Create an instance of Tkinter root window
root = tk.Tk()
# Create an instance of the CenterScreenGui class
app = CenterScreenGui(root)

# Global call to main() for program entry
if __name__ == '__main__':
    main()