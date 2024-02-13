# File Verification Application

## Overview
The File Verification Application is designed to validate and process CSV files containing user data. It ensures that each entry in the CSV file has a valid ID number, mobile number, and email address as per the specified formats. This application is beneficial for maintaining the integrity of user data by segregating valid and invalid records.

## Features

- **ID Number Validation**: Checks if the ID numbers consist only of digits.
- **Mobile Number Validation**: Validates mobile numbers against a specified format (modifiable as per country-specific formats).
- **Email Address Validation**: Ensures email addresses are in a proper format.
- **Data Segregation**: Separates valid and invalid entries into different sheets.
- **Excel Output**: Exports processed data into an Excel file with separate sheets for valid entries, invalid entries, and entries sorted by gender.

## Requirements

- Python 3
- Pandas Library
- Regular Expressions (re module)

## Installation

Before running the application, ensure that you have Python installed on your system. Then, install the required Python packages using pip:

```bash
pip install pandas
pip install xlsxwriter
```

## Usage

To use the application, place your CSV file in the project directory and ensure it has the columns 'ID Number', 'Mobile Number', 'Email Address', and 'Gender'. Then, run the script with the following command:

```bash
python file_verification_application.py
```

The script will process the data and save the output in an Excel file named `processed_data.xlsx` with the following sheets:

- `Invalid Records`: Contains all entries that failed validation checks.
- Gender-specific sheets: Each valid entry is sorted into sheets named after the genders specified in the data.

## Customization

You can customize the validation logic in the functions `validate_id`, `validate_mobile`, and `validate_email` to suit your data format requirements.

## Contributions

Contributions to this project are welcome. You can contribute by improving the validation functions, adding new features, or reporting bugs.

## License

This project is open source and available under the [MIT License](LICENSE.md).