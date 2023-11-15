import pandas as pd
## Import os if using join to bring in file ##
import os

## Specify the file path to define excel_file_path ##
excel_file_path = r'C:\Users\Carter\Documents\GitHub\MedInfoPro\Data\Medicine_description.xlsx'

## Read the Excel file into a Pandas DataFrame ##
df = pd.read_excel(excel_file_path)

print(df)

### Now that the data set works and is defined as 'excel_file_path' we can upload the repository for the GUI ###
from Medication import Medication

class MedicationRepository:
    def __init__(self) -> None:
        self.__med_list = []
        self.__db = pd.read_excel(excel_file_path)

        ## define functions for interface ##
    def get_quantity_and_price(self) -> list[Medication]: 
        drug_name_to_search = self.entry.get()

        # Use the Medication class to retrieve quantity and price
        result = get_quantity_and_price(drug_name_to_search, medication_list)

        # Display the result in a messagebox
        if result is not None:
            quantity, price = result
            messagebox.showinfo("Medication Info", f"Drug: {drug_name_to_search}\nQuantity: {quantity}\nPrice: ${price}")
        else:
            messagebox.showwarning("Medication Info", f"{drug_name_to_search} not found in the medication list")

        