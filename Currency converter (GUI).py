from currency_converter import CurrencyConverter
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("455x400")
root.title("Currency Converter")

c = CurrencyConverter()
def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = from_currency_combo.get()
        to_currency = to_currency_combo.get()
        converted_amount = c.convert(amount, from_currency, to_currency)
        result_label.config(text=f"Converted Amount:  {converted_amount:.2f} {to_currency}")
    except ValueError:
        result_label.config(text="Please enter a valid amount!!!...")

# Create and configure labels
title_label = tk.Label(root, text="Currency Converter", font=("Math bold", 24, "bold"), bg="orange", fg="blue")
title_label.place(x=80, y=18)

amount_label = tk.Label(root, text="Enter amount:", font=("Math bold", 15))
amount_label.place(x=32, y=105)

from_currency_label = tk.Label(root, text="From currency:", font=("Math bold", 15))
from_currency_label.place(x=32, y=155)

to_currency_label = tk.Label(root, text="To currency:", font=("Math bold", 15))
to_currency_label.place(x=32, y=205)

result_label = tk.Label(root, text="", font=("Math bold", 18), fg="green")
result_label.place(x=48, y=325)

# Create and configure entry widgets
entry_amount = tk.Entry(root,width=23)
entry_amount.place(x=278, y=110)

# Create and configure currency selection dropdowns
currencies = list(c.currencies) 
from_currency_combo = ttk.Combobox(root, values=currencies)
from_currency_combo.place(x=278, y=160)
from_currency_combo.set("USD") 

to_currency_combo = ttk.Combobox(root, values=currencies)
to_currency_combo.place(x=278, y=210)
to_currency_combo.set("INR") 

convert_button = tk.Button(root, text="Convert", font="Times 14",fg="red", command=convert_currency)
convert_button.place(x=190, y=265)

root.mainloop()
