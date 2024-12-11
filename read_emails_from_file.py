def read_emails_from_file(filename):
    try:
        with open(filename, 'r') as file:
            emails = [line.strip() for line in file if line.strip()]
        return emails
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []