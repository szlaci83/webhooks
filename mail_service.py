import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from properties import *
from mail_repo import create_mail


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


## rewrite this:
def send_report_mail(to_mail, message, link, add_poster):
    html, text = create_mail(message, link)
    _sendmail(to_mail, SUBJECT_CP, html, text, add_poster)


def send_report_to_all(message, link, add_poster):
    for person in ADDRESSEES:
        send_report_mail(person, message, link, add_poster)


def _example():
    send_report_mail(TEST_EMAIL, "Test", 'http://semmi', add_poster=True)
    send_report_mail(TEST_EMAIL, "Test", 'http://semmi', add_poster=False)


if __name__ == "__main__":
    _example()
