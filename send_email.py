import smtplib
from email.message import EmailMessage
from read_emails_from_file import read_emails_from_file

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

if __name__ == "__main__":
    sender_email = ""
    sender_password = ""

    subject =""
    body = ""

    email_list = "emails.txt"
    recipient_emails = read_emails_from_file("email-address-list")

    if recipient_emails:
        send_email(sender_email, sender_password, recipient_emails, subject, body)
    else:
        print("No more recipients found.")

    
