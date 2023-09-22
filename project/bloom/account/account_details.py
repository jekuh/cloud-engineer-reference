import csv
import json

def generate_demo_data():
    # Account details
    account_details = [
        {
            'Firstname': 'John',
            'Lastname': 'Doe',
            'Email': 'john.doe@example.com',
            'Password': 'password123',
            'Account ID': '12345'
        },
        {
            'Firstname': 'Jane',
            'Lastname': 'Smith',
            'Email': 'jane.smith@example.com',
            'Password': 'password456',
            'Account ID': '67890'
        }
    ]
    
    # Generate CSV file
    with open('demo.csv', 'w', newline='') as csvfile:
        fieldnames = ['Firstname', 'Lastname', 'Email', 'Password', 'Account ID']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(account_details)
    
    # Generate JSON test data
    with open('test_data.json', 'w') as jsonfile:
        json.dump(account_details, jsonfile, indent=4)

# Call the function to generate the demo data
generate_demo_data()
