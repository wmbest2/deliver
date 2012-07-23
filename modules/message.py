import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

def add_file(msg, deliverable, new_name):
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(deliverable, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
           'attachment; filename="%s"' % new_name)
    msg.attach(part)

class Message:
    message = ''
    files   = []
    names   = []
    recipients = ''

    def append_html(self, html):
        self.message += html

    def append_file(self, filename, newname):
        self.files.append(filename)
        if newname:
            self.names.append(newname)
        else:
            self.names.append(filename)

    def set_recipients(self, recipients):
        self.recipients = ', '.join(recipients)

    def log(self):
        print "HERHHERHE"

    def send(self, username, password):
        msg = MIMEMultipart()

        msg['From'] = username
        msg['To'] = self.recipients
        msg['Subject'] = 'Deliverable'

        for i, filename in enumerate(self.files):
            add_file(msg, filename, self.names[i])

        msg.attach(MIMEText(self.message, 'html'))

        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(username, password)

        mailServer.sendmail(username, self.recipients, msg.as_string())
        mailServer.close()
