import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

print("**************************")

num_users = int(input("How many users do you want to send OTPs to? "))
for _ in range(num_users):

    print("*****************************")
    
    name = input("Enter Your Name: ")
    otp = random.randint(10000 ,99999)
    body = f"OTP For Verification is {otp}"

    msg = MIMEMultipart()
    msg ["From"] = "kotiabhishek944@gmail.com"
    msg ["To"] = input("Enter Your Email Id: ")
    msg ["Subject"] = "OTP For Validation"
    msg.attach(MIMEText(body,"plain"))

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("kotiabhishek944@gmail.com","xuve lmqh qins uaew")
    server.send_message(msg)
    server.quit()
    attempts = 3
    while attempts > 0:
        confirmotp = int(input("Enter OTP Recieved: "))
        if otp == confirmotp:
            print("OTP Verification Success")
            break
        else:
            attempts -= 1
            print(f"Invalid OTP. You have {attempts} attempt(s) left.")
    
    if attempts == 0:
        print(f"OTP verification failed for {name}. Please try again later.")
    print("\n--- End of Verification ---\n")








