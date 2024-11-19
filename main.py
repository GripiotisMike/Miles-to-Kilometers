# Importing the tkinter module, which is used for creating GUI applications in Python
from tkinter import *

# Create the main window for the application
window = Tk()
window.title("Mile to Km Converter")  # Set the window title
window.minsize(180, 100)  # Set the minimum size of the window
window.config(padx=25, pady=25)  # Add padding around the window's contents

# Function that will be called when the button is pressed
def button_press():
    # Retrieve the value entered in the Entry widget, convert it to a float, and multiply by 1.609 to convert miles to kilometers
    final = round(float(entry.get()) * 1.609)
    # Update the text of the result label with the calculated value
    result.config(text=final)

# Label for "Miles" text, positioned with padding
miles_label = Label(text="Miles", padx=5, pady=5)
miles_label.grid(row=0, column=2)  # Place it in the first row, third column of the grid

# Label for "Km" text, positioned with padding
km_label = Label(text="Km", padx=5, pady=5)
km_label.grid(row=1, column=2)  # Place it in the second row, third column of the grid

# Label displaying "is equal to", positioned with padding
equal_label = Label(text="is equal to", padx=5, pady=5)
equal_label.grid(row=1, column=0)  # Place it in the second row, first column of the grid

# Label that will display the result of the conversion, initially set to "0"
result = Label(text="0")
result.grid(row=1, column=1)  # Place it in the second row, second column of the grid

# Entry widget where the user can input the number of miles to convert
entry = Entry(width=7)
entry.grid(row=0, column=1)  # Place it in the first row, second column of the grid

# Button that will trigger the conversion when clicked
button = Button(text="Calculate", command=button_press)
button.grid(row=2, column=1)  # Place it in the third row, second column of the grid

# Start the tkinter main loop to run the GUI application
window.mainloop()
