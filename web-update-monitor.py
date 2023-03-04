import schedule
import time

def web_update_monitor():

    import requests
    import smtplib, ssl
    from lxml import etree

    import mysql.connector
    from mysql.connector import Error
    import pandas as pd

    ### Enter the following ###
    port = 465  #SMTP port
    smtp_server = ""  #SMTP server
    sender_email = "" #Sender's email address for message notifications
    email_password = "" #Sender's email password
    mysql_hostname = "" #MySQL Hostname
    mysql_username = "" #MySQL User Name
    mysql_passwd = "" #MySQL Password
    mysql_database = "" #MySQL Database
    check_frequency_min = 180 #The frequency of checking (in minutes)
    ############################
    
    mydb = mysql.connector.connect(
        host = mysql_hostname,
        user = mysql_username,
        passwd = mysql_passwd,
        database = mysql_database
    )

    mydb2 = mysql.connector.connect(
        host = mysql_hostname,
        user = mysql_username,
        passwd = mysql_passwd,
        database = mysql_database
    )

    mydb3 = mysql.connector.connect(
        host = mysql_hostname,
        user = mysql_username,
        passwd = mysql_passwd,
        database = mysql_database
    )

    url_cursor = mydb.cursor()
    receiver_email_cursor = mydb2.cursor()
    check_results_cursor = mydb3.cursor()

    #Load the list of URLs, keywords and wraps to be checked as well as the notification email subjects and contents should there be updates or not
    url_cursor.execute("SELECT serial, URL, name, keyword, wrap, no_update_subject, no_update_message, update_subject, update_message FROM URL_list where check_flag = 1")

    for (serial, URL, name, xpath_keyword, xpath_wrap, no_update_subject, no_update_message, update_subject, update_message) in url_cursor:

            resp = requests.get(URL)

            if resp.status_code == 200:
                dom = etree.HTML(resp.text)
                elements = dom.xpath(xpath_wrap)     
                
                #Find the keyword from the wrapped text and build the email messages for the 3 scenarios (i.e. update in content, no update in content and error)
                try:
                    if xpath_keyword in elements[0].text:
                        message = "Subject: " + no_update_subject + " \n\n " + no_update_message
                        update = 0
                    else:
                        message = "Subject: " + update_subject + " \n\n " + update_message
                        update = 1
                except:
                    message = "Subject: " + update_subject + " \n\n " + update_message
                    update = 1
            else: 
                message = "Subject: " + name + " Checking Error \n\n Please check " + URL
                update = -1

            #Send the messages to email addresses respectively for the 3 scenarios
            if update == 0:
                receiver_email_cursor.execute("SELECT email FROM receiver_email_list WHERE send_when_no_update = 1")
            if update == 1:
                receiver_email_cursor.execute("SELECT email FROM receiver_email_list WHERE send_when_update = 1")
            if update == -1:
                receiver_email_cursor.execute("SELECT email FROM receiver_email_list WHERE send_when_error = 1")
            
            context = ssl.create_default_context()
            with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
                server.login(sender_email, email_password)
                for receiver_email in receiver_email_cursor:
                    server.sendmail(sender_email, receiver_email, message)
                server.quit()
            
            #Update the checked results (0 = Not updated; 1 = Updated; -1 = Error)
            check_results_sql = "INSERT INTO check_results (date_time, url_serial, check_update_flag) VALUES (now(), %s, %s)"
            check_results_val = (serial, update)
            check_results_cursor.execute(check_results_sql, check_results_val)
            mydb3.commit()

    receiver_email_cursor.close()
    url_cursor.close()
    check_results_cursor.close()
    mydb.close()
    mydb2.close()
    mydb3.close()    

#Schedule to run the check with the defined frequency (in minutes)
schedule.every(check_frequency_min).minutes.do(web_update_monitor)

while True:
    schedule.run_pending()
    time.sleep(1)
