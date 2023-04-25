import tkinter as tk


def convert():
    miles = float(miles_entry.get())
    kilometers = round(miles * 1.609, 3)
    km_converted_label.config(text=kilometers)


window = tk.Tk()
window.title("Mile to Km Converter")
window.resizable(width=False, height=False)
window.config(padx=25, pady=25)

miles_entry = tk.Entry(width=7)
miles_entry.insert(index="end", string="0")
miles_entry.grid(column=1, row=0)

miles_label = tk.Label(text="Miles", font=("Arial", 20, "bold"))
miles_label.grid(column=2, row=0)

equal_label = tk.Label(text="is equal to", font=("Arial", 20))
equal_label.grid(column=0, row=1)

km_converted_label = tk.Label(text="0", font="Arial")
km_converted_label.grid(column=1, row=1)

km_label = tk.Label(text="Km", font=("Arial", 20, "bold"))
km_label.grid(column=2, row=1)

calculate_button = tk.Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()
