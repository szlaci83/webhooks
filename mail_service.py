import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_properties import *
from mail_repo import create_mail


def _sendmail(to, subject, html, text):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = FROM_ADDR
    msg['To'] = to

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)

    server = smtplib.SMTP('smtp.gmail.com')
    server.ehlo()
    server.starttls()
    server.login(FROM_ADDR, PW)
    server.sendmail(FROM_ADDR, to, msg.as_string())
    server.quit()


def send_report_mail(to_mail, message, link):
    html, text = create_mail(message, link)
    _sendmail(to_mail, SUBJECT, html, text)


def send_report_to_all(message, link):
    for person in ADDRESSEES:
        send_report_mail(person, message, link)


def _example():
    send_report_mail(TEST_EMAIL, "Test", 'http://semmi')


if __name__ == "__main__":
    _example()

