import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from properties import *
from mail_repo import create_cp_mail, create_tr_mail, create_sonarr_mail


def _sendmail(to, subject, html, text, add_poster):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = FROM_ADDR
    msg['To'] = to

    if add_poster:
        with open('temp.jpg', 'rb') as f:
            mime = MIMEBase('image', 'jpg', filename='temp.jpg')
            mime.add_header('Content-Disposition', 'attachment', filename='temp.jpg')
            mime.add_header('X-Attachment-Id', '0')
            mime.add_header('Content-ID', '<0>')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)

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


def send_cp_mail(to_mail, html, text, add_poster):
    _sendmail(to_mail, SUBJECT_CP, html, text, add_poster)


def send_cp_mail_to_all(message, link, add_poster):
    html, text = create_cp_mail(message, link)
    for person in ADDRESSEES:
        send_cp_mail(person, html, text, add_poster)


def send_tr_mail(to_mail, html, text):
    _sendmail(to_mail, SUBJECT_TR, html, text, False)


def send_tr_mail_to_all(message):
    html, text = create_tr_mail(message)
    for person in ADDRESSEES:
        send_tr_mail(person, html, text)


def send_sonarr_mail(to_mail, html, text):
    _sendmail(to_mail, SUBJECT_SONARR, html, text, False)


def send_sonarr_mail_to_all(message):
    html, text = create_sonarr_mail(message)
    for person in ADDRESSEES:
        send_tr_mail(person, html, text)


def _example():
    #send_cp_mail(TEST_EMAIL, "Test", 'http://semmi', add_poster=True)
    #send_cp_mail(TEST_EMAIL, "Test2", 'http://semmi', add_poster=False)
    send_tr_mail_to_all("Testinggg")

if __name__ == "__main__":
    _example()
