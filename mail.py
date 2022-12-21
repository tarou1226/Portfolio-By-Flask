import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

def send_mail():
    text = "テスト本文"
    msg = MIMEText(text, "plain", "utf-8")

    msg.replace_header("Content-Transfer-Encoding", "base64")
    msg["Subject"] = "件名"
    msg["From"] = "自分のアドレス"
    msg["To"] = "相手のアドレス"
    msg["Cc"] = "カーボンコピー"
    msg["Bcc"] = ""
    msg["Date"] = formatdate(None,True)

    host = "smtp.gmail.com"
    nego_combo = ("starttls", 587)

    smtpclient = smtplib.SMTP(host, nego_combo[1], timeout=10.0)
    smtpclient.ehlo()
    smtpclient.starttls()
    smtpclient.ehlo()
    # logが発生
    smtpclient.set_debuglevel(2)

    username = "gmailのアカウント"
    password = "googleアプリのパスワード?"
    smtpclient.login(username, password)

    smtpclient.send_message(msg)
    smtpclient.quit()