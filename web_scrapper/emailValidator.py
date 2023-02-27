import requests

# Replace with your Mailgun API key and domain
API_KEY = '32c2a4fe9e411d680212236e632ebf0c-52d193a0-498e70e6'
DOMAIN = 'sandbox0b7ce96578ce4c3883b2b69945109125.mailgun.org'

# Replace with the filename of your email list
EMAIL_LIST_FILE = 'email_list.txt'

# Define the Mailgun API endpoint for email validation
API_ENDPOINT = f'https://api.mailgun.net/v3/{DOMAIN}/address/validate'

# Set the HTTP basic authentication credentials
auth = ('api', API_KEY)

# Open the email list file and read all the lines
with open(EMAIL_LIST_FILE, 'r') as f:
    email_list = f.readlines()

# Loop through each email address in the list
for email in email_list:
    # Remove any trailing whitespace or newline characters
    email = email.strip()
    
    # Make a GET request to the Mailgun API endpoint with the email address
    response = requests.get(API_ENDPOINT, auth=auth, params={'address': email})
    
    # Check the response status code
    if response.status_code == 200:
        # If the API returns a status code of 200, the email address is valid
        response_data = response.json()
        if response_data['is_valid']:
            print(f'{email} is a valid email address')
        else:
            print(f'{email} is an invalid email address')
    else:
        # If the API returns a status code other than 200, the email address is invalid
        print(f'{email} is bad request')
