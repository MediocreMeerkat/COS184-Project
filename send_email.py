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

if __name__ == "__main__":
    sender_email = ""
    sender_password = ""

    subject ="Important Notice: Account Suspended Due to Unusual Activity"
    body = "Hello, faithful FakeBank customer. We have detected unusual activity on your account and have temporarily suspended access to protect your information. Immediate Action is required to restore your account. We have detected numerous failed login attempts from around the globe and have deduced that your account information has been compromised. To restore access to your account, please reply to this email with your social security number, date of birth, and mother's maiden name. After this information is provided, we can restore your account. Please provide this information in a timely fashion. Thank you, The staff at FakeBank LLC."

    email_list = "emails.txt"
    recipient_emails = read_emails_from_file(email-address-list)

    if recipient_emails:
        send_email(sender_email, sender_password, recipient, subject, body)
    else:
        print("No more recipients found.")

    
