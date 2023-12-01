import tkinter as tk
from tkinter import messagebox
import pandas as pd


class Medication:
    def __init__(self, drug_name: str, description: str, quantity: int, categories: str, price: int,
                 drug_interactions: str, side_effects: str) -> None:
        self.__drug_name = drug_name
        self.__description = description
        self.__quantity = quantity
        self.__categories = categories
        self.__price = price
        self.__drug_interactions = drug_interactions
        self.__side_effects = side_effects

    @property
    def drug_name(self) -> str:
        return self.__drug_name

    @property
    def description(self) -> str:
        return self.__description

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def categories(self) -> str:
        return self.__categories

    @property
    def price(self) -> int:
        return self.__price

    @property
    def drug_interactions(self) -> str:
        return self.__drug_interactions

    @property
    def side_effects(self) -> str:
        return self.__side_effects


class MedInfoProInterface:
    def __init__(self, master, medication_repository):
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
        try:
            file_path = r'C:\Users\Carter\Documents\GitHub\MedInfoPro\Data\Medicine_description.xlsx'
            self.medication_data = pd.read_excel(file_path)
        except FileNotFoundError:
            self.medication_data = pd.DataFrame()  # Create an empty DataFrame
            messagebox.showerror("File Not Found", "Medicine_description.xlsx not found. Please check the file path.")

    def submit_info(self):
        # Get user input
        name = self.entry_name.get()
        dob = self.entry_dob.get()
        drug_name = self.entry_medication.get()
        quantity = self.entry_quantity.get()

        print(f"User input drug name: {drug_name}")

        # Look up medication information from the MedicationRepository
        medication_info = self.medication_repository.get_medication_info(drug_name)

        if medication_info is not None:
            # Directly construct the message for the messagebox
            message = (
                f"Patient Name: {name}\n"
                f"Date of Birth: {dob}\n"
                f"Medication Name: {drug_name}\n"
                f"Quantity: {quantity}\n\n"
                f"Medication Information: {medication_info}\n"
                f"Drug Name: {medication_info.drug_name}\n"
                f"Categories: {medication_info.categories}\n"
                f"Description: {medication_info.description}\n"
                f"Quantity: {medication_info.quantity}\n"
                f"Price: {medication_info.price}\n"
                f"Drug Interactions: {medication_info.drug_interactions}\n"
                f"Side Effects: {medication_info.side_effects}"
             )
        else:
            message = "Medication information not found."
        # Show a message box with the result
        messagebox.showinfo("MedInfoPro Result", message)

class MedicationRepository:
    def __init__(self, excel_file_path):
         try:
            # Load the Excel dataset into a pandas DataFrame
            self.medication_data = pd.read_excel(excel_file_path)
            print("Loaded DataFrame:")
            print(self.medication_data)

            self.medication_objects = self.create_medication_objects()
         except FileNotFoundError:
            print(f"Error: File not found at path {excel_file_path}")
         except Exception as e:
            print(f"An error occurred: {e}")

    def create_medication_objects(self):
        # Create Medication objects from the DataFrame rows
        medication_objects = []
        required_columns = ['Drug_Name', 'Description', 'Quantity', 'Categories', 'Price',
                            'Drug Interactions', 'Side effects']

        if set(required_columns).issubset(self.medication_data.columns):
            for _, row in self.medication_data.iterrows():
                medication_objects.append(
                    Medication(
                        drug_name=row['Drug_Name'],
                        description=row['Description'],
                        quantity=row['Quantity'],
                        categories=row['Categories'],
                        price=row['Price'],
                        drug_interactions=row['Drug Interactions'],
                        side_effects=row['Side effects']
                    )
                )
        else:
            print("Required columns are missing in the Excel file.")

        return medication_objects

    def get_medication_info(self, drug_name):
        drug_name = drug_name.lower()  # Convert to lowercase for case-insensitive comparison
        for medication in self.medication_objects:
            if medication.drug_name.lower() == drug_name:
                return medication
        return None


# Example usage:
root = tk.Tk()
med_repo = MedicationRepository(r'C:\Users\Carter\Documents\GitHub\MedInfoPro\Data\Medicine_description.xlsx')
app = MedInfoProInterface(root, med_repo)
root.mainloop()

