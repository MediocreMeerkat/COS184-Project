import smtplib
from email.message import EmailMessage

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        msg = EmailMessage()
        msg['from'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.set_content(body)

        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls() 
            server.login(sender_email, sender_password)
            server.send_message(msg)
            print(f"Email sent successfully to {recipient_email}")
    except Exception as e:
        print(f"Error sending email to {recipient_email}: {e}")

def read_emails_from_file(filename):
    try:
        with open(filename, 'r') as file:
            emails = [line.strip() for line in file if line.strip()]
        return emails
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return []
