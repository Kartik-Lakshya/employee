import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class EmployeeManagementSystem:
    def __init__(self, master):
        self.master = master
        master.title("Employee Management System")

        # Create frames for different sections
        self.employee_frame = tk.Frame(master)
        self.employee_frame.pack(pady=10)

        self.details_frame = tk.Frame(master)
        self.details_frame.pack()

        # Labels and entry fields for employee details
        self.name_label = tk.Label(self.employee_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.employee_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.id_label = tk.Label(self.employee_frame, text="ID:")
        self.id_label.grid(row=1, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self.employee_frame)
        self.id_entry.grid(row=1, column=1, padx=5, pady=5)

        self.department_label = tk.Label(self.employee_frame, text="Department:")
        self.department_label.grid(row=2, column=0, padx=5, pady=5)
        self.department_entry = tk.Entry(self.employee_frame)
        self.department_entry.grid(row=2, column=1, padx=5, pady=5)

        self.salary_label = tk.Label(self.employee_frame, text="Salary:")
        self.salary_label.grid(row=3, column=0, padx=5, pady=5)
        self.salary_entry = tk.Entry(self.employee_frame)
        self.salary_entry.grid(row=3, column=1, padx=5, pady=5)

        # Button to add new employee
        self.add_button = tk.Button(self.employee_frame, text="Add Employee", command=self.add_employee)
        self.add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Treeview for displaying employee details
        self.tree = ttk.Treeview(self.details_frame, columns=("ID", "Name", "Department", "Salary"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Department", text="Department")
        self.tree.heading("Salary", text="Salary")
        self.tree.pack()

        # Scrollbar for treeview
        self.scrollbar = tk.Scrollbar(self.details_frame, orient="vertical", command=self.tree.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        # Initialize employee data (replace with your actual data source)
        self.employees = []

    def add_employee(self):
        name = self.name_entry.get()
        id = self.id_entry.get()
        department = self.department_entry.get()
        salary = self.salary_entry.get()

        if name and id and department and salary:
            # Validate salary input (ensure it's a number)
            try:
                salary = float(salary)
            except ValueError:
                messagebox.showerror("Error", "Invalid salary input. Please enter a number.")
                return

            # Add new employee to the list
            self.employees.append({"ID": id, "Name": name, "Department": department, "Salary": salary})

            # Update the treeview
            self.tree.insert("", "end", values=(id, name, department, salary))

            # Clear entry fields
            self.name_entry.delete(0, tk.END)
            self.id_entry.delete(0, tk.END)
            self.department_entry.delete(0, tk.END)
            self.salary_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all the fields.")

root = tk.Tk()
app = EmployeeManagementSystem(root)
root.mainloop()
