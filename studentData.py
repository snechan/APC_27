import tkinter as tk
from tkinter import ttk, messagebox

FILE_NAME = "student.txt"


def submit_data():
    name = name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    college = college_entry.get()
    branch = branch_entry.get()

    if not name or not mobile or not email or not college or not branch:
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    with open(FILE_NAME, "a") as file:
        file.write(name + "|" + mobile + "|" + email + "|" +
                   college + "|" + branch + "\n")

    messagebox.showinfo("Success", "Record saved successfully")

    name_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    college_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)


def read_data():
    window = tk.Toplevel(root)
    window.title("Student Records")
    window.geometry("900x450")

    table = ttk.Treeview(
        window,
        columns=("Name", "Mobile", "Email", "College", "Branch"),
        show="headings"
    )

    table.heading("Name", text="Name")
    table.heading("Mobile", text="Mobile No")
    table.heading("Email", text="Email ID")
    table.heading("College", text="College Name")
    table.heading("Branch", text="Branch")

    table.column("Name", width=150)
    table.column("Mobile", width=150)
    table.column("Email", width=200)
    table.column("College", width=180)
    table.column("Branch", width=120)

    table.pack(fill="both", expand=True, padx=10, pady=10)

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 5:
                    table.insert("", tk.END, values=data)

    except FileNotFoundError:
        messagebox.showinfo("Records", "No records found")


# Main window
root = tk.Tk()
root.title("Student Application")
root.geometry("600x600")


# Heading
title = tk.Label(
    root,
    text="Student Application",
    font=("Arial", 26, "bold")
)
title.pack(pady=30)


# Form
form = tk.Frame(root)
form.pack()


# Name
tk.Label(
    form,
    text="Name",
    font=("Arial", 13),
    width=15,
    anchor="e"
).grid(row=0, column=0, padx=10, pady=10)

name_entry = tk.Entry(
    form,
    width=35,
    font=("Arial", 12)
)
name_entry.grid(row=0, column=1)


# Mobile No
tk.Label(
    form,
    text="Mobile No",
    font=("Arial", 13),
    width=15,
    anchor="e"
).grid(row=1, column=0, padx=10, pady=10)

mobile_entry = tk.Entry(
    form,
    width=35,
    font=("Arial", 12)
)
mobile_entry.grid(row=1, column=1)


# Email ID
tk.Label(
    form,
    text="Email ID",
    font=("Arial", 13),
    width=15,
    anchor="e"
).grid(row=2, column=0, padx=10, pady=10)

email_entry = tk.Entry(
    form,
    width=35,
    font=("Arial", 12)
)
email_entry.grid(row=2, column=1)


# College Name
tk.Label(
    form,
    text="College Name",
    font=("Arial", 13),
    width=15,
    anchor="e"
).grid(row=3, column=0, padx=10, pady=10)

college_entry = tk.Entry(
    form,
    width=35,
    font=("Arial", 12)
)
college_entry.grid(row=3, column=1)


# Branch
tk.Label(
    form,
    text="Branch",
    font=("Arial", 13),
    width=15,
    anchor="e"
).grid(row=4, column=0, padx=10, pady=10)

branch_entry = tk.Entry(
    form,
    width=35,
    font=("Arial", 12)
)
branch_entry.grid(row=4, column=1)


# Submit
tk.Button(
    root,
    text="Submit",
    command=submit_data,
    width=18,
    font=("Arial", 12)
).pack(pady=20)


# Read
tk.Button(
    root,
    text="Read",
    command=read_data,
    width=18,
    font=("Arial", 12)
).pack()


root.mainloop()