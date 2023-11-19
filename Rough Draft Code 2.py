import tkinter as tk
from tkinter import messagebox
import pandas as pd


class MedInfoProInterface:
    def __init__(self, master,medication_repository):
        self.master = master
        self.medication_repository = medication_repository
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

        # Load medication data from CSV file
        #try:
            #file_path = r'C:\Users\Carter\Documents\GitHub\MedInfoPro\Data\Medicine_description.xlsx'
            #self.medication_data = pd.read_excel(file_path)
        #except FileNotFoundError:
            #self.medication_data = pd.DataFrame()  # Create an empty DataFrame
            #messagebox.showerror("File Not Found", "Medicine_description.xlsx not found. Please check the file path.")

    def submit_info(self):
        # Get user input
        name = self.entry_name.get()
        dob = self.entry_dob.get()
        medication_name = self.entry_medication.get()
        quantity = self.entry_quantity.get()

        # Look up medication information from the loaded CSV file
        medication_info = self.medication_repository.get_medication_info(medication_name)

        # Perform some action with the input (you can replace this with your logic)
        result = f"Patient Name: {name}\nDate of Birth: {dob}\nMedication Name: {medication_name}\nQuantity: {quantity}\n\n"

        # Append addictional fields to the result
        result += f"Medication Information: {medication_info}\n"

        if not medication_info.empty:
            # Append additional fields to the result
            result += f"Drug Name: {medication_info.loc[0, 'Drug_Name']}\n"
            result += f"Categories: {medication_info.loc[0, 'Categories']}\n"
            result += f"Description: {medication_info.loc[0, 'Description']}\n"
            result += f"Quantity: {medication_info.loc[0, 'Quantity']}\n"
            result += f"Price: {medication_info.loc[0, 'Price']}\n"
            result += f"Drug Interactions: {medication_info.loc[0, 'Drug Interactions']}\n"
            result += f"Side Effects: {medication_info.loc[0, 'Side effects']}"
        else:
            result += "Medication information not found."

        # Show a message box with the result
        messagebox.showinfo("MedInfoPro Result", result)

    
class MedicationRepository:
        ## define functions for interface ##
    def __init__(self, excel_file_path):
        # Load the Excel dataset into a pandas DataFrame
        self.medication_data = pd.read_excel(excel_file_path)

    def get_medication_info(self, medication_name):
        # Retrieve information from the DataFrame based on the medication name
        medication_info = self.medication_data.loc[
            self.medication_data['Medication Name'] == medication_name, 'Information'].values

        if len(medication_info) > 0:
            return medication_info[0]
        else:
            return "Information not available for this medication."
        
    def get_medication_info(self, medication_name):
        print("Column names:", self.medication_data.columns)

        try:
            return self.medication_data[self.medication_data['Medication Name'] == medication_name]
        except KeyError:
            print(f"Error: Column 'Medication Name' not found in DataFrame.")
            return pd.DataFrame()


# Create the main application window
root = tk.Tk()

#Load data
excel_file_path = r'C:\Users\Carter\Documents\GitHub\MedInfoPro\Data\Medicine_description.xlsx'
# Instantiate the MedicationRepository with the Excel dataset path
med_repository = MedicationRepository(excel_file_path)

# Instantiate the interface
med_info_pro_interface = MedInfoProInterface(root, med_repository)

# Run the application
root.mainloop()
