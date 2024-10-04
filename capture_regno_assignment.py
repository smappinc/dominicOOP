# Dominic Muhairwe M23B13/024 BSIT-2
class Student:
    
    # Constructor function for Student class
    def __init__(self, regno, name):
        self.regno = regno
        self.name = name
    
    # Method to display entered Values
    def display(self):
         
        # An if statement to check if the entered value for name is not a digit 
        if not self.name.isdigit():
            print(f"Your Registration Number is: {self.regno}\n Your Name is: {self.name}")
        
        # If the entered value for name is a digit, it returns this print statement
        else:
            print(f"Error: Please input characters for name")

# Variables to capture values for regno and name
regno = input("Please enter your Registration Number:\n")
name = input("Please enter your Name:\n")

# Object of the class Student 
capture = Student(regno, name)
capture.display()

