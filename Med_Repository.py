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

        