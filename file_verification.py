import pandas as pd
import re

# Function to validate ID numbers (customize this as per your requirements)
def validate_id(id_number):
    # Assuming id_number is a string of digits, replace with your validation logic
    return id_number.isdigit()

# Function to validate mobile numbers (customize this as per your country's mobile number format)
def validate_mobile(mobile_number):
    # Example: Validates an Indian mobile number; update regex as per requirement
    return bool(re.match(r'^\+?1?\d{9,15}$', mobile_number))

# Function to validate email addresses
def validate_email(email):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

# Load CSV file
df = pd.read_csv('path_to_your_csv_file.csv')

# Apply validation functions and create a 'valid' column
df['valid'] = df.apply(lambda x: validate_id(x['ID Number']) and validate_mobile(x['Mobile Number']) and validate_email(x['Email Address']), axis=1)

# Separate valid and invalid data
valid_df = df[df['valid']]
invalid_df = df[~df['valid']].drop(columns=['valid'])

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('processed_data.xlsx', engine='xlsxwriter')

# Export invalid records to a separate sheet
invalid_df.to_excel(writer, sheet_name='Invalid Records', index=False)

# Loop through unique genders and save each to a different sheet
for gender in valid_df['Gender'].unique():
    gender_df = valid_df[valid_df['Gender'] == gender]
    gender_df.drop(columns=['valid']).to_excel(writer, sheet_name=gender, index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
