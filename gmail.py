import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


mail_content = """ Hii Shivani,
 I am writing on behalf of IPEM college.
 Please join our college event on 2 oct 2022
 Thankn You,

 """

# The mail addresses and password
sender_address = 'shivani.140026gmail.com'
sender_pass = 'opq$987'
receiver_address = 'shivangishivani.5854@gmail.com'
# setup the MIME 
message = MIMEMultipart()
message['From'] = 'shivani<shivani.140026gmail.com>'
message['To'] = receiver_address
message['subject'] = ' A mail sent by the python programmer '
# subject time
# body and attachments for the mail.
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'hello.txt' 
attach_file = open(attach_file_name, 'rb')
payload = MIMEBase('application','octate-system')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)
payload.add_header('content-disposition','attachment')
message.attach(payload)

session = smtplib.SMTP('smtp.gmail.com', 587)
session.starttls()
session.login(sender_address, sender_pass)
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('mail sent ')