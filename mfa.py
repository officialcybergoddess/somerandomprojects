import random
import smtplib
from email.mime.text import MIMEText

# Simulated user database
user_database = {
    "user1": {"password": "password123", "email": "user1@example.com"},
    "user2": {"password": "securepass", "email": "user2@example.com"},
}

# Function to send OTP via email
def send_otp_email(email, otp):
    from_email = "your.email@gmail.com"  # Replace with your email
    smtp_server = "smtp.gmail.com"  # Use the appropriate SMTP server
    smtp_port = 587  # Use the appropriate SMTP port
    smtp_username = "your.email@gmail.com"  # Replace with your email
    smtp_password = "your_password"  # Replace with your email password

    msg = MIMEText(f"Your OTP is: {otp}")
    msg["From"] = from_email
    msg["To"] = email
    msg["Subject"] = "Multi-Factor Authentication OTP"

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(from_email, [email], msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Failed to send OTP email: {str(e)}")
        return False

# Function to generate a random OTP
def generate_otp():
    return str(random.randint(1000, 9999))

# Simulated login process with MFA
def login(username, password):
    if username not in user_database:
        return "User not found"

    user_info = user_database[username]

    if password != user_info["password"]:
        return "Invalid password"

    otp = generate_otp()
    if send_otp_email(user_info["email"], otp):
        user_input_otp = input("Enter the OTP sent to your email: ")
        if user_input_otp == otp:
            return "Login successful"
        else:
            return "Invalid OTP"
    else:
        return "Failed to send OTP"

# Simulated login attempt
username = input("Enter your username: ")
password = input("Enter your password: ")
result = login(username, password)
print(result)
