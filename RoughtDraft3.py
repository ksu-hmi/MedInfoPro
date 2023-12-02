import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pandas as pd

class DrugInfoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drug Information App")

        # Load Excel file into a DataFrame
        try:
            self.df = pd.read_excel(r"C:\Users\Carter\Documents\GitHub\MedInfoPro\Data\Medicine_description.xlsx")
        except pd.errors.EmptyDataError:
            messagebox.showerror("Error", "The Excel file is empty.")
            return
        except FileNotFoundError:
            messagebox.showerror("Error", "Excel file not found.")
            return

        print(self.df.columns)

        # Remove duplicates based on the 'drug_name' column
        self.df = self.df.drop_duplicates(subset='drug_name')

        # Variables to store user input
        self.name_var = tk.StringVar()
        self.dob_var = tk.StringVar()
        self.medication_var = tk.StringVar()
        self.quantity_var = tk.IntVar()

        # Create GUI components
        self.create_widgets()


    def create_widgets(self):
        # Labels and Entry widgets for user input
        tk.Label(self.root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.name_var).grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Date of Birth:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.dob_var).grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Medication Wanted:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.medication_var).grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Quantity Needed:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        tk.Entry(self.root, textvariable=self.quantity_var, validate="key", validatecommand=(self.root.register(self.validate_quantity), "%P")).grid(row=3, column=1, padx=10, pady=5)

        # Button to retrieve drug information
        ttk.Button(self.root, text="Get Drug Information", command=self.get_drug_info).grid(row=4, column=0, columnspan=2, pady=10)

    def get_drug_info(self):
        # Get user input
        medication_wanted = self.medication_var.get()

        # Convert DataFrame to dictionary
        drug_dict = self.df.set_index('drug_name').to_dict(orient='index')

        # Search for drug information based on the medication wanted
        if medication_wanted in drug_dict:
            drug_info = drug_dict[medication_wanted]
            messagebox.showinfo("Drug Information",
                                f"Drug Name: {medication_wanted}\n"
                                f"Description: {drug_info['description']}\n"
                                f"Quantity: {self.quantity_var.get()}\n"
                                f"Categories: {drug_info['categories']}\n"
                                f"Price: {drug_info['price ']}\n"
                                f"Drug Interactions: {drug_info['drug_interactions']}\n"
                                f"Side Effects: {drug_info['side_effects ']}")
        else:
            messagebox.showinfo("Information", f"No information found for {medication_wanted}.")

    def validate_quantity(self, new_value):
        # Validate that quantity is a positive integer
        try:
            value = int(new_value)
            return value >= 0
        except ValueError:
            return False

if __name__ == "__main__":
    root = tk.Tk()
    app = DrugInfoApp(root)
    root.mainloop()
