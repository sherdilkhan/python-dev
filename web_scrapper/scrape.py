from email_validator import validate_email, EmailNotValidError

# Define a list of email addresses to verify
emails = ["email1@example.com", "email2@example.com", "seherdikjfks_sfsf_53535_GDgd@gmail.com", "samofcity@gmail.com"]

# Verify the email addresses in bulk
results = {}
for email in emails:
    try:
        # Validate the email address
        valid = validate_email(email)
        
        # If the email address is valid, add it to the results dictionary with the value "valid"
        results[email] = "valid"
    except EmailNotValidError as e:
        # If the email address is not valid, add it to the results dictionary with the error message as the value
        results[email] = str(e)

# Print the verification results
for email, result in results.items():
    print(f"{email}: {result}")
