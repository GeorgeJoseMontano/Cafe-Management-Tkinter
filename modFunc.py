from tkinter import messagebox

# Function to check if the user input is empty and give it value of zero
def chkForNull(food):
    if food == "":
        return "0"
    else:
        return food

# Function to convert the string to float
def floaty(x):
    try:
        return float((chkForNull(x.get())))
    except ValueError:
        return 0