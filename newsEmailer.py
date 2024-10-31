import requests  # HTTP requests
from bs4 import BeautifulSoup  # Web Scraping
import smtplib  # Email sending
from email.mime.multipart import MIMEMultipart  # Email body
from email.mime.text import MIMEText
import datetime  # System date and time manipulation
import os  # File handling

# Get the current date and time
now = datetime.datetime.now()

# Get website URL from user
web_url = input("Enter the Hacker News URL: ")
content = ""

# Function to extract news from the given website
def extract_news(url):
    print("Extracting Hacker News Stories...")
    news_content = "<b>Hacker News Top Stories:</b>\n<br>" + "-" * 50 + "<br>"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    for i, tag in enumerate(soup.find_all("td", attrs={"class": "title", "valign": ""})):
        if tag.text != "More":
            news_content += f"{i + 1} :: {tag.text}<br>"
    return news_content

# Call the function to extract news and build email content
content += extract_news(web_url)
content += "<br>------<br><br>End of Message"

# Get email details from the user
from_email = input("Enter your email address: ")
password = input("Enter your email password: ")

# Choosing the email input method
email_addresses = []
choice = input("Do you want to (1) Enter email addresses manually or (2) Upload a file? Enter 1 or 2: ")

if choice == '1':
    print("Enter email addresses one at a time. Type 'EXIT' when you are finished:")
    while True:
        email = input("Enter email address: ")
        if email.lower() == "exit":
            break
        email_addresses.append(email.strip())
else:
    file_path = input("Enter the path to the .txt file: ")
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            data = file.read()
            email_addresses = [email.strip() for email in data.split(',')]
    else:
        print("Invalid file path. Please restart the script and enter a valid .txt file.")

# Prepare the email
print("Composing Email...")
msg = MIMEMultipart()
msg['Subject'] = f'Top News Stories from Hacker News [Automated] - {now.day}-{now.month}-{now.year}'
msg['From'] = from_email
msg['To'] = ", ".join(email_addresses)
msg.attach(MIMEText(content, 'html'))

# Sending the email
try:
    print("Connecting to email server...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(from_email, password)
    print("Sending email...")
    server.sendmail(from_email, email_addresses, msg.as_string())
    print("Email Sent Successfully!")
except smtplib.SMTPAuthenticationError:
    print("Authentication failed. Please check your email and password.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    server.quit()

