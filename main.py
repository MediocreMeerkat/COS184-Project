from os import read
from read_emails_from_file import read_emails_from_file
from send_email import send_email
from getpass import getpass


while True:
    try:
        sender = input("Sender's email address:")
        if sender == None or sender == "":
            raise Exception
    except Exception:
        print("You have not provided an appropriate email. Please try again.")
        continue
    break
while True:
    try:
        password = getpass("Sender's password:")
    except Exception:
        print("Error please input your password again")
        continue
    break
while True:
    try:
        filename = input("File with reciever emails:")
        receivers = read_emails_from_file(filename)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please try again.")
        continue
    break

#need code to decide which email to send off
subject = "hello"
body = "hello"

for item in receivers:
    send_email(sender, password, item, subject, body)