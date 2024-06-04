from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(180, 100)
window.config(padx=25, pady=25)


def button_press():
    final = round(float(entry.get()) * 1.609)
    result.config(text=final)


miles_label = Label(text="Miles", padx=5, pady=5)
miles_label.grid(row=0, column=2)

km_label = Label(text="Km", padx=5, pady=5)
km_label.grid(row=1, column=2)

equal_label = Label(text="is equal to", padx=5, pady=5)
equal_label.grid(row=1, column=0)

result = Label(text="0")
result.grid(row=1, column=1)

entry = Entry(width=7)
entry.grid(row=0, column=1)

button = Button(text="Calculate", command=button_press)
button.grid(row=2, column=1)

window.mainloop()
