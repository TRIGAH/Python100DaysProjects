from tkinter import *

KM = 1.60934

window = Tk()
window.title("Miles to KM Coverter")
window.minsize(width=300,height=300)

converter_entry = Entry(width=10)
converter_entry.insert(END, string="0")
converter_entry.grid(row=0,column=1)

miles_label = Label()
miles_label.grid(row=0,column=2)
miles_label.config(text="Miles")

converter_label = Label()
converter_label.grid(row=1,column=1)
converter_label.config(text="0")

equal_label = Label()
equal_label.grid(row=1,column=0)
equal_label.config(text="is equal to")

km_label = Label()
km_label.grid(row=1,column=2)
km_label.config(text="KM")

def calculate():
    km_distance= int(converter_entry.get()) * KM
    converter_label.config(text=str(km_distance))
    

converter_button = Button(text="Calculate", command=calculate)
converter_button.grid(row=2,column=1)

window.mainloop()