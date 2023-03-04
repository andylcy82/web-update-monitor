# web-update-monitor

## Author
[Andy Lee] - https://github.com/andylcy82

## Purpose
This Python script "web-update-monitor.py" is designed to check a list of websites for updates of a specified keyword / key phrase at a frequency (e.g. every 6 hours) and send email notifications to specified recipients based on the update status.

## Getting Started
Before running this script, you will need to make sure that you have Python installed on your machine, along with the following libraries:

schedule
requests
smtplib
ssl
lxml
mysql-connector-python
pandas
You can install these libraries using pip, by running the following command in your terminal or command prompt:

pip install schedule requests smtplib ssl lxml mysql-connector-python pandas

Once you have the required libraries installed, you can clone this repository or download the web_update_checker.py file to your local machine.

## Usage
To use this script, you will need to provide the following information:

SMTP server information (smtp_server, port)
Sender's email address (sender_email) and password (email_password)
MySQL database information (mysql_hostname, mysql_username, mysql_passwd, mysql_database)
List of URLs to check (URL_list table in the MySQL database)
List of email recipients (receiver_email_list table in the MySQL database)
To configure the script, open the web_update_checker.py file in a text editor and update the following lines with your own information:

port = 465  #SMTP port
smtp_server = ""  #SMTP server
sender_email = "" #Sender's email address for message notifications
email_password = "" #Sender's email password
mysql_hostname = "" #MySQL Hostname
mysql_username = "" #MySQL User Name
mysql_passwd = "" #MySQL Password
mysql_database = "" #MySQL Database
check_frequency_min = 360 #The frequency of checking (in minutes)

The GitHub repository also includes an SQL dump file named "web_update_monitor.sql" that contains the necessary code to create the MySQL database tables. Sample rows are inserted into tables "receiver_email_list" and "url_list" for your reference and further amendment.

You can use this SQL dump file to create the necessary database tables for the web application. To do so, create a new database, copy the SQL dump code and paste it into a new MySQL query tab in your preferred database management tool. Then, execute the query to create the tables.

Once you have updated the necessary information, save the file and run it using the following command:

python web_update_monitor.py

The script will run indefinitely, checking the URLs at the specified frequency and sending email notifications when updates are detected. You can stop the script by pressing CTRL+C in your terminal or command prompt.

## License
This Python script is licensed under the GNU General Public License v3.0. You can find a copy of the license in the LICENSE file included with the project. This license grants you the freedom to use, modify, and distribute the code, subject to the terms and conditions of the license. It also requires that any modifications or derivative works of the code be released under the same license.

## Disclaimer
This script is provided as-is, without any warranties or guarantees of any kind. The author is not responsible for any damages or losses that may arise from the use of this script. Use at your own risk.

