from tkinter import*


def calculate_result():
    miles = float(input_miles.get())
    result = miles * 1.609
    result_label.config(text=f"{format(result, '.3f')}")


screen = Tk()
screen.config(padx=20, pady=20)
screen.title("Mile to KM converter")

# input
input_miles = Entry(width=10)
input_miles.grid(row=0, column=1)

# labels
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_to = Label(text="equals = ")
equal_to.grid(row=1, column=0)

result_label = Label(text="0")
result_label.grid(row=1, column=1)

kilometer_label = Label(text="KM")
kilometer_label.grid(row=1, column=2)

#button
calculate_button = Button(text="calculate", command=calculate_result)
calculate_button.grid(row=2, column=1)


screen.mainloop()