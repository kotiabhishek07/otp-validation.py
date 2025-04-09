OTP EMAIL VERIFICATION CONSOLE BASED PROJECT

OTP Verification System:

This Python script allows the sending of one-time passwords (OTPs) to multiple users via email for verification purposes. It generates random 4-digit OTPs, sends them to user-provided email addresses, and prompts the user to enter the OTP received for validation.

Features:

1.Multi-user support: The script allows sending OTPs to multiple users at once.
2.Email integration: Uses Gmail's SMTP server to send OTPs.
3.OTP generation: A random 4-digit OTP is generated for each user.
4.Verification: The user is prompted to enter the OTP they received. They have up to 3 attempts to enter the correct OTP.
5.Failure handling: After 3 incorrect attempts, the verification for that user fails, and the process is terminated for that user.

Requirements:

1.Python 3.x
2.The smtplib library (built-in with Python)
3.email.mime library (built-in with Python)

How to Use:

1.Run the script.
2.Enter the number of users you want to send OTPs to.
3.For each user, input their name and email address.
4.The script will send an OTP to the email address and ask the user to input it.
5.The user will have 3 attempts to input the correct OTP. If successful, the user will receive a success message. If the OTP is incorrect after 3 attempts, the verification will fail.

Security Considerations:

1.Email Credentials: The script requires access to an email account (abc@gmail.com in the example). You should replace this with your own email credentials for production use. It's highly recommended to use an App Password for your Gmail account instead of your main account password for security reasons.
