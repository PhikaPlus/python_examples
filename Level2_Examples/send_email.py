import smtplib
import ssl

try:
    port = 465                      # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "SENDER"         # Enter your address
    sender_password = 'PASS'        # Enter your password
    receiver_email = "RECEIVER"     # Enter receiver address
    message = """
    Hi Dear Phika ...
    """

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

except smtplib.SMTPAuthenticationError:
    print('Auth error!\nActive "less secure app access" in Gmail')
