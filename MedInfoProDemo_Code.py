# Import Pandas For Python File

import pandas as pd

df = pd.read_excel(r"C:\Users\rober\OneDrive\Documents\GitHub\MedInfoPro\Data\Medicine_description.xlsx")

# Create Dataset into dictionary

med_dict = df.to_dict()



