import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

from string import Template

MY_ADDRESS = "shah.visheshshah@gmail.com"
PASSWORD = "Vishesh25$"


# This function returns the name and e-mail id from a file


def get_contacts(filename):
    names = []
    emails = []

    with open(filename, mode='r', encoding='utf-8') as contact_file:
        for a_contact in contact_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


# Template string is returned to rename the title name in e-mail


def read_templates(filename):
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def mail_report(user, mail):
    try:
        name, email, date = str(user), mail, datetime.now()
        print(name, email)
        message_template = read_templates('L:\Lambton College\Term 1\AML 1214- Python Programming\Workspace\Stock_Portfolio\static\message.txt')

        # enables the SMTP connection with host and port number
        s = smtplib.SMTP("smtp.gmail.com", 587)

        # puts the connection in transport layer and commands are in encrypted format
        s.starttls()
        s.login(MY_ADDRESS, PASSWORD)

        msg = MIMEMultipart()
        # substitutes the name of the receiver
        body = message_template.substitute(PERSON_NAME=name.title(),
                                           DATE_TIME="{0} {1}".format(date.strftime("%x"), date.strftime("%X")))

        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = "Your stock report of the day!"

        # attach the body instance to variable
        msg.attach(MIMEText(body, "plain"))

        # open the file to be sent
        filename1 = "L:\Lambton College\Term 1\AML 1214- Python Programming\Workspace\Stock_Portfolio\Stock Report.xlsx"
        attachment = open(filename1, "rb")

        # instance of MIMEBase and named as p
        p = MIMEBase('application', 'octet-stream')

        # To change the payload into encoded form
        p.set_payload(attachment.read())

        # encode into base64
        encoders.encode_base64(p)
        filename = "Stock Report.xlsx"
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        # attach the instance 'p' to instance 'msg'
        msg.attach(p)

        # sends the mail to the receiver
        s.send_message(msg)
        del msg
        # closes the SMTP connection
        s.quit()
        return True
    except Exception:
        raise Exception
