import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smtp_host = "smtp.gmail.com"
smtp_port = 587
sender_email = 'aybek.09.1984@gmail.com'
sender_password = "krhiuceqogwxhrhs"

receiver_email = "a90baev@gmail.com"
subject = "Это тествое сообщение"

try:
    server = smtplib.SMTP(smtp_host, smtp_port)
    server.starttls()
    server.login(sender_email, sender_password)
    for i in range(10):
        try:
            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = subject

            body = "Это тестовое сообщение от 3 месяца"
            message.attach(MIMEText(body, 'plain'))


            text = message.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Успешно отправлена")
        except Exception as e:
            print("ОШибка", e)
finally:
    server.quit()