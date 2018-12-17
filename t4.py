import smtplib

host ="smtp.gmail.com"
port =587
username="katiematri7@gmail.com"
password = "Tavoluku25"

from_email = username
to_list = [ "hivauz@gmail.com"]

email_conn = smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

the_msg = MIMEMultipart("alternative")
the_msg['Subject'] = "helo there"
the_msg["From"] = from_email
the_msg["To"] = to_list[0]
plain_txt = "testing the msg"
html_txt = """\
<html>
    <head> </head>
    <body>
        <p>Hey! <br>
        testgin this email <b> mesg </b>. Made by <a href='https;dfs'> team erj</a>
        </p>
    </body>
</html>
    """

part1 = MIMEText(plain_txt,'plain')
part2 = MIMEText(html_txt, "html")

the_msg.attach(part1)
the_msg.attach(part2)

print(the_msg.as_string())

email_conn.sendmail(from_email, to_list, the_msg.as_string())
email_conn.quit()
