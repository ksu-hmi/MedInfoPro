## Main Code Page for MEDINFOPRO ##
## Instal Pandas ##
pip install pandas

## Import data set ##
import pandas as pd
## Import os if using join to bring in file ##
import os

## Specify the file path to define excel_file_path ##
excel_file_path = 'path/to/your/excel/file.xlsx'

## OR ##

## Create file name and path then join ##
fileName='csv or excel file name'
filePath=r'C:\Users\Carter\Downloads'
file=os.path.join(filePath,fileName) 

## Read the Excel file into a Pandas DataFrame ##
df = pd.read_excel(excel_file_path)
## or this  ##
df=pd.read_csv(file) 
## pd.read depends on how the file is brought into pandas##

## Display the DataFrame ##
print(df)
