import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, receiver_email, subject, message_to_send):
    smtp_server = "smtp.example.com"  # Replace with your SMTP server address
    smtp_port = 587  # Replace with your SMTP server port

    # Create a MIME message
    email_message = MIMEMultipart()
    email_message["From"] = sender_email
    email_message["To"] = receiver_email
    email_message["Subject"] = subject

    # Attach the message to the MIME message
    email_message.attach(MIMEText(message, "plain"))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Enable TLS encryption
        server.login(sender_email, sender_password)
        server.send_message(email_message)

# Example usage
sender_email = "yugalmittal07@gmail.com"
sender_password = "......."
receiver_email = "demomail@gmail.com"
subject = "Hello from yugal this mail is demo purpose generated with python"
message = "This is a test email sent from Python."

send_email(sender_email, sender_password, receiver_email, subject, message_to_send)
