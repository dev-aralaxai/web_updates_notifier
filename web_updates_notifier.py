import ssl
import time

import urllib.request
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from bs4 import BeautifulSoup

def send_email(url, mail_body):
    #define here your email server, account and recipient
    ### WARNING!!!, NEVER SHARE THE CODE WITH THOSE FIELDS FILLED!!!!
    smtp_server = "" #SMTP server here
    smtp_port = #SMPT port (should be an integer)
    email = "" #Your email account for sending
    password = "" #Your password
    recipients = #["recipient1@example.com", "recipient2@example.com"] if you want only one recipient just place the adress as a string "recipient1@example.com"

    #create the message
    message = MIMEMultipart()
    message["From"] = email
    message["To"] = ", ".join(recipients) #for multiple recipients, if there is only one recipient, just call the variable, message["To"] = recipients
    message["Subject"] = "" #write the subject here


    message.attach(MIMEText(mail_body, "plain"))

    # Connect to server SMTP and sends message, if there is some error it will notify
    try:
        # Connect to the server through SSL
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(email, password)
            server.sendmail(email, recipients, message.as_string())
            print("Mail sent success.")
    except Exception as e:
        print(f"Error sending mail: {e}")
    finally:
        server.close()  # Close clonnection


def web_scrap():
    try:
        # Ignore SSL certificate errors
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = "" #define the url to scrap here
        html = urllib.request.urlopen(url, context=ctx).read()  # retrieves url code
        soup = BeautifulSoup(html, "html.parser")

        #The next 3 lines are the scrap, you should eyesight the html code of the website
        #Once you know which lines you want to retrieve, define the tag and its string

        events = soup.find(name="h3", string="Eventos") #In my case, I wanted to start scrapping from word "Eventos" inside the h3 tag to below
        events = events.find_all_next(name="span") #In my case, only matters what there is coded inside "span" tag
        events_str = str(events) #Needed to be a string for better comparison

        #Create a temp file with the string retrieved
        writetempfile = open("web_scrap_temp.txt", "w")
        writetempfile.write(events_str)
        writetempfile.close()

        #Read the temp file for compare it with the file where is written the last update
        tempfile = open("web_scrap_temp.txt", "r")
        tempread = tempfile.readlines()

        #In that file is written the last retrieved update
        readfile = open("web_scrap.txt", "r")
        stored_file = readfile.readlines()

        #Check if there is some different between files, if there is, it updates the file and prints a message, then notifies by email
        if tempread == stored_file:
            tempfile.close()
            readfile.close()
            print("\nNo changes on the webpage")
        else:
            tempfile.close()
            readfile.close()
            update_file = open("web_scrap", "w")
            update_file.write(events_str)
            update_file.close()
            mail_body = "Webpage updated!\n\nCheck it on " + url


            send_email(url, mail_body)
    #If something goes wrong, programs prints the error but doesn't stop
    except Exception as e:
        print(f"Execution error: {e}")


#Run the program every hour
while True:
    web_scrap()
    time.sleep(3600)