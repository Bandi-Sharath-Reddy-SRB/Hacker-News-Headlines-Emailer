# 🌐 Hacker News Headlines Emailer

🚀 This Python script scrapes the top stories from [Hacker News](https://news.ycombinator.com/) and sends them via email to specified recipients. It uses `requests` and `BeautifulSoup` for data extraction and `smtplib` to handle email sending.

## 📖 Project Overview

With this tool, you can:
- 📰 **Fetch** the latest Hacker News headlines.
- 📬 **Enter recipient emails** manually or upload them from a file.
- ✉️ **Send an email** with top stories to a list of recipients.

## 🛠️ Prerequisites

Make sure you have:
- **Python 3.x** installed
- **Gmail Account** (for sending emails)
- Python libraries: `requests`, `bs4` (BeautifulSoup), `smtplib`

## ⚙️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Bandi-Sharath-Reddy-SRB/Hacker-News-Headlines-Emailer.git
cd Hacker-News-Headlines-Emailer
```

### 2. Install Required Libraries

Use `pip` to install all required libraries:

```bash
pip install -r requirements.txt
```

### 3. Create a `requirements.txt` file (if missing)

If `requirements.txt` is missing, create it by running:

```bash
pip freeze > requirements.txt
```

### 4. Enable Less Secure App Access in Gmail

⚠️ To send emails with Gmail, enable **"Less secure app access"** in your Gmail settings. This may need to be re-enabled if your account’s security changes.

## 🚀 Running the Script

1. **Run the Script**  
   ```bash
   python hacker_news_emailer.py
   ```

2. **Enter the Hacker News URL**  
   When prompted, input the Hacker News URL (e.g., https://news.ycombinator.com/).

3. **Provide Your Email Credentials**  
   Enter your Gmail address and password to authenticate for email sending.

4. **Add Recipient Emails**  
   Choose one of two ways to add recipients:
   - **Manual Entry**: Enter emails one by one. Type "EXIT" when done.
   - **File Upload**: Provide the path to a `.txt` file with emails separated by commas or listed one per line.

5. **Confirm Sending**  
   The script will display messages confirming its connection, email sending status, and completion.

### 🔧 Example Commands

- **Clone the Repository**:
  ```bash
  git clone https://github.com/Bandi-Sharath-Reddy-SRB/Hacker-News-Headlines-Emailer.git
  ```
- **Navigate to Project Directory**:
  ```bash
  cd Hacker-News-Headlines-Emailer
  ```
- **Install Requirements**:
  ```bash
  pip install -r requirements.txt
  ```
- **Run the Script**:
  ```bash
  python hacker_news_emailer.py
  ```

## 📝 Notes

- **Security Tip**: Ensure your Gmail account has **"Less secure app access"** enabled to avoid authentication errors.
- **Confidentiality**: Avoid sharing email credentials and the `.txt` file with email addresses publicly.
- **Customization**: This tool scrapes stories from the Hacker News homepage. You can change the URL as needed.
