import random
import string

Email_1 = '''Dear User,
Congratulation!! U hav won $1,000,000 in the SUPER CRAZY INTERGALACTIC LOTTERY! To collect ur winning, pls click here: Click Here for Money!!! and enter your personal info.
Do not wait becuz time is running out!!!!!!
Thnks,
Lottery Company'''

Email_2 = '''Dear valued customer,
We detected a suspicious login attempt to your online banking account from an unrecognized device. For your protection, access to your account has been temporarily restricted.
Details of the attempt:
Date/Time: December 13, 2024, 2:34 PM
Location: New York, USA
Device: Windows 10
If this was you, no further action is required. If you do not recognize this activity, please verify your identity immediately to restore access to your account:
Verify My Identity
For your security, do not share this email or the verification link.
Thank you for your prompt attention to this matter.
Sincerely,
American Express'''

Email_3 '''Hello, faithful FakeBank customer. 
We have detected unusual activity on your account and have temporarily suspended access to protect your information. Immediate Action is required to restore your account. 
We have detected numerous failed login attempts from around the globe and have deduced that your account information has been compromised. To restore access to your account, please reply to this email with your social security number, date of birth, and mother's maiden name. After this information is provided, we can restore your account. Please provide this information in a timely fashion. 
Thank you, The staff at FakeBank LLC.'''

def get_random_email():
    emails = [Email_1, Email_2, Email_3]
    body = random.choice(emails)
    return body