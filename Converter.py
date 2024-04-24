import tkinter as tk

def convert():
    try:
        value = entry.get()
        if radio_var.get() == 1:  # Binary to Decimal and Hexadecimal
            decimal_value = int(value, 2)
            hex_value = hex(decimal_value).upper()[2:]
            result_label.config(text=f"Decimal: {decimal_value}\nHexadecimal: {hex_value}")
        elif radio_var.get() == 2:  # Decimal to Binary and Hexadecimal
            decimal_value = int(value)
            binary_value = bin(decimal_value)[2:]
            hex_value = hex(decimal_value).upper()[2:]
            result_label.config(text=f"Binary: {binary_value}\nHexadecimal: {hex_value}")
        elif radio_var.get() == 3:  # Hexadecimal to Binary and Decimal
            decimal_value = int(value, 16)
            binary_value = bin(decimal_value)[2:]
            result_label.config(text=f"Binary: {binary_value}\nDecimal: {decimal_value}")
    except ValueError:
        result_label.config(text="Invalid input!")

root = tk.Tk()
root.title("Number Converter")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry = tk.Entry(frame)
entry.grid(row=0, column=0, padx=5, pady=5)

convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=0, column=1, padx=5, pady=5)

radio_var = tk.IntVar()
radio_var.set(1)  # Default selection

radio_bin_to_dec_hex = tk.Radiobutton(frame, text="Binary to Decimal and Hex", variable=radio_var, value=1)
radio_bin_to_dec_hex.grid(row=1, column=0, padx=5, pady=5, sticky="w")

radio_dec_to_bin_hex = tk.Radiobutton(frame, text="Decimal to Binary and Hex", variable=radio_var, value=2)
radio_dec_to_bin_hex.grid(row=2, column=0, padx=5, pady=5, sticky="w")

radio_hex_to_bin_dec = tk.Radiobutton(frame, text="Hexadecimal to Binary and Decimal", variable=radio_var, value=3)
radio_hex_to_bin_dec.grid(row=3, column=0, padx=5, pady=5, sticky="w")

result_label = tk.Label(frame, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()