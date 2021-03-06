# -*- coding: UTF-8 -*-
"""
@Author ：WangJie
@Date   ：2020/12/22 16:20 
@Desc   ：VJTJIHIQSYIWLQNU
"""
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '13772137174@163.com'  # 发件人邮箱账号
my_pass = 'VJTJIHIQSYIWLQNU'  # 发件人邮箱的授权码
my_user = '1457011008@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret= True
    try:
        msg = MIMEText('验证码为：123456', 'plain', 'utf-8')
        msg['From'] = formataddr(["王洁", my_sender]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["", my_user]) # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "验证码" # 邮件的主题，也可以说是标题
        server = smtplib.SMTP("smtp.163.com") # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的ret=False
        ret = False
    return ret
if __name__ == '__main__':
    ret = mail()
    if ret:
        print("邮件发送成功")
    else:
        print("邮件发送失败")