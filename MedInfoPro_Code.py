import tkinter as tk
from tkinter import messagebox

class MedInfoProInterface:
    def __init__(self, master):
        self.master = master
        master.title("MedInfoPro")

        # Create labels
        self.label_name = tk.Label(master, text="Patient Name:")
        self.label_dob = tk.Label(master, text="Date of Birth:")
        self.label_medication = tk.Label(master, text="Medication Name:")
        self.label_quantity = tk.Label(master, text="Quantity:")

        # Create entry widgets
        self.entry_name = tk.Entry(master)
        self.entry_dob = tk.Entry(master)
        self.entry_medication = tk.Entry(master)
        self.entry_quantity = tk.Entry(master)

        # Create submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_info)

        # Grid layout
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.label_dob.grid(row=1, column=0, padx=10, pady=10)
        self.label_medication.grid(row=2, column=0, padx=10, pady=10)
        self.label_quantity.grid(row=3, column=0, padx=10, pady=10)

        self.entry_name.grid(row=0, column=1, padx=10, pady=10)
        self.entry_dob.grid(row=1, column=1, padx=10, pady=10)
        self.entry_medication.grid(row=2, column=1, padx=10, pady=10)
        self.entry_quantity.grid(row=3, column=1, padx=10, pady=10)

        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

    def submit_info(self):
        # Get user input
        name = self.entry_name.get()
        dob = self.entry_dob.get()
        medication = self.entry_medication.get()
        quantity = self.entry_quantity.get()

        # Perform some action with the input (you can replace this with your logic)
        result = f"Patient Name: {name}\nDate of Birth: {dob}\nMedication Name: {medication}\nQuantity: {quantity}\n\n"

        # Additional fields
        medication_info = "Medication Information: Some information about the medication."
        drug_interactions = "Potential Drug Interactions: Information about potential drug interactions."
        side_effects = "Side Effects: Information about side effects."
        price_details = "Price Details: Information about the cost of the medication."


        # Append additional fields to the result
        result += f"{medication_info}\n{drug_interactions}\n{side_effects}\n{price_details}"

        # Show a message box with the result
        messagebox.showinfo("MedInfoPro Result", result)


# Create the main application window
root = tk.Tk()

# Instantiate the interface
med_info_pro_interface = MedInfoProInterface(root)

# Run the application
root.mainloop()
