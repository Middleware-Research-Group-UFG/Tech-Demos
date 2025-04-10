import smtplib as smtp
from email.message import EmailMessage
from os import getenv


URL = "smtp.gmail.com"
PORT = 587

login = {
    "email": "rbcmlproject@gmail.com",
    "passwd": getenv("EMAIL_PASSWORD")
}

message = EmailMessage()
message["From"] = login["email"]
message["To"] = "baptistabaptista@discente.ufg.br" 
message["Subject"] = "Using STMP"
message.set_content("Hello World!")


try:
    server = smtp.SMTP(URL, PORT)
    server.starttls()
    server.login(login["email"], login["passwd"])
    server.send_message(message)
    server.quit()
    print("Message sent")

except smtp.SMTPAuthenticationError:
    print("Authentication fail")

except Exception as e:
    print(f"Message not sent\nError: {e}")
