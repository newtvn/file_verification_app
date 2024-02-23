import pandas as pd
import re

def is_valid_id(id_number):
    return str(id_number).isdigit() and len(str(id_number)) == 10

def is_valid_mobile(mobile_number):
    return re.match(r'^\+2547\d{8}$', mobile_number) is not None

def is_valid_email(email_address):
    return re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email_address) is not None

df = pd.read_csv('path_to_your_file.csv')

valid_df = df[df.apply(lambda x: is_valid_id(x['ID Number']) and is_valid_mobile(x['Mobile Number']) and is_valid_email(x['Email Address']), axis=1)]
invalid_df = df[~df.apply(lambda x: is_valid_id(x['ID Number']) and is_valid_mobile(x['Mobile Number']) and is_valid_email(x['Email Address']), axis=1)]

writer = pd.ExcelWriter('processed_data.xlsx', engine='xlsxwriter')

for gender, data in valid_df.groupby('Gender'):
    data.to_excel(writer, sheet_name=gender, index=False)

invalid_df.to_excel(writer, sheet_name='Invalid Data', index=False)

writer.save()
