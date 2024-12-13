from read_emails_from_file import read_emails_from_file
from send_email import send_email
from getpass import getpass

sender = input("Sender's email address: ")
password = getpass("Sender's password:")
receiver = input("Receiver's email address: ")
emails = read_emails_from_file("emails.txt")

#need code to decide which email to send off
subject = None
body = None

send_email(sender, password, receiver, subject, body)