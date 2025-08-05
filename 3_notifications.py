import smtplib
import os

from dotenv import load_dotenv

load_dotenv()

MAIL_LOGIN = os.getenv("MAIL_LOGIN")
APP_PASSWORD_MAIL = os.getenv("APP_PASSWORD_MAIL")
CONTEXT = os.getenv("CONTEXT")


def send_emails(email_list):
    mail_smtp = smtplib.SMTP("smtp.gmail.com", 587)
    mail_smtp.starttls()
    mail_smtp.login(MAIL_LOGIN, APP_PASSWORD_MAIL)
    mail_smtp.sendmail(MAIL_LOGIN, email_list, CONTEXT)
    mail_smtp.quit()
