from tkinter import *

def button_clicked():
    new_text = float(input.get())
    result = new_text * 1.609347
    the_answer["text"] = result.__round__(3)

window = Tk()
window.title("My First GUI Program")
window.minsize(width=300, height=100)
window.config(padx=50, pady=25)

#entry
input = Entry(width=10, font=("Arial", 12, "normal"))
input.grid(column=1, row=0, padx=10, pady=5)

#label
my_label = Label(text="I Am A Label", font=("Arial", 12, "normal"))
my_label["text"] = "Miles"
my_label.grid(column=2, row=0, padx=10, pady=5)

# is equal
is_equal = Label(text="is equal to", font=("Arial", 12, "normal"))
is_equal.grid(column=0, row=1, padx=10, pady=5)

the_answer = Label(text=0, font=("Arial", 12, "normal"))
the_answer.grid(column=1, row=1, padx=10, pady=5)

unit_answer = Label(text="km", font=("Arial", 12, "normal"))
unit_answer.grid(column=2, row=1, padx=10, pady=5)

#Button
button = Button(text="Calculate", font=("Arial", 12, "bold"), command=button_clicked)
button.grid(column=1, row=2, padx=10, pady=5)












window.mainloop()
