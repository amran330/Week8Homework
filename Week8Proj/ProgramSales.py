#Amran Rahim (Start) - 3/6/24
import csv
import json
import tkinter as tk
from tkinter import messagebox

# Step 1:empty list as "sales_data"
sales_data = []

# Step 2: convert the CSV file to JSON format
with open('SalesJan2009.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader, None)  # Skip the header 

    for row in csv_reader:
        transaction_date = row[0]
        product = row[1]
        price = int(row[2])
        payment_type = row[3]
        name = row[4].strip('"')
        city = row[5].strip('"')
        state = row[6].strip('"')
        country = row[7].strip('"')

        data_dict = {
            'Transaction_date': transaction_date,
            'Product': product,
            'Price': price,
            'Payment_Type': payment_type,
            'Name': name,
            'City': city,
            'State': state,
            'Country': country
        }
        sales_data.append(data_dict)

with open('transaction_data.json', 'w') as json_file:
    json.dump(sales_data, json_file, indent=4)

# (UI)
root = tk.Tk()
root.title("Sales Data Converter")
# title label
title_label = tk.Label(root, text="Sales Data Converter APP", font=("Helvetica", 16), bg="sea green", fg="gold")
title_label.pack(pady=10)

root.geometry("400x200")
root.configure(bg="sea green")  

def quit_program():
    if messagebox.askokcancel("Exit", "Are you sure you want to quit this program?"):
        root.quit()

quit_button = tk.Button(root, text="EXIT", command=quit_program)
quit_button.pack()

# end UI

root.mainloop()
#Amran Rahim (End) - 3/7/24