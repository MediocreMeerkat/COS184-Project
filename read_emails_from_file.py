def read_emails_from_file(filename):
    with open(filename, 'r') as file:
        emails = [line.strip() for line in file if line.strip()]
    return emails
