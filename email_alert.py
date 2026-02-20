import smtplib, sys, traceback
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
with open("last_log.txt", "rt", encoding="utf-8") as f:
    content = f.read()

def global_exception_handler(exc_type, exc_value, exc_tb):
    tb = ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
    with open(f"email_error_{today}.txt", "w", encoding="utf-8") as f:
        f.write("[错误]：邮件未正常发送\n")
        f.write(tb)
        f.write("\n原始错误内容：\n"+f"{content}")

sys.excepthook = global_exception_handler

if "[错误]" in content:
    # SMTP 配置（以 QQ 邮箱为例）
    smtp_server = 'smtp.qq.com'
    smtp_port = 465
    sender = ''
    password = ''
    receiver = ''

    # 邮件内容
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr((Header('自动签到系统', 'utf-8').encode(), sender))
    msg['To'] = formataddr((Header('管理员', 'utf-8').encode(), receiver))
    msg['Subject'] = Header(f"自动签到错误 {today}", 'utf-8')

    # 发送邮件
    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
