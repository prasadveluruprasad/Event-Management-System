import email.message
import smtplib

def send(message, subject, emails):

    if emails != []:

        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login("yanyukang29@gmail.com","uwgqzivjaunvtwbv")
        for e in emails:
            msg = email.message.EmailMessage()
            msg ["From"] = "yanyukang29@gmail.com"
            msg ["To"] = e
            msg ["Subject"] = subject
            msg.add_alternative(message, subtype = "html" )

            server.send_message(msg)
        server.close()

