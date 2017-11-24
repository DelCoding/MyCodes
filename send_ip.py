# -*- coding:utf-8 -*-
import socket
import fcntl
import struct
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from smtplib import SMTP

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

def send_email(SMTP_host, from_account, from_passwd, to_account, subject, content):
    print "sending..."
    email_client = SMTP(SMTP_host, 25)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


ip = get_ip_address('ens3')
from_addr = "from_email"	#发送人的邮箱
password = ""	#发送人邮箱的密码
to_addr = "1044987878@qq.com"	#接收人邮箱
smtp_server = "smtp.sina.com"	#发送人的smtp服务器

#ip = 'hello,this is a test'
#ip = ip.replace('.', '')
ip = '你的新地址为：' + ip +'。请尽快查收！'
print ip

send_email(smtp_server, from_addr, password, to_addr, "地址更新邮件", ip)
