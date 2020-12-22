# -*- coding: UTF-8 -*-
"""
@Author ：WangJie
@Date   ：2020/12/22 16:57 
@Desc   ：
"""
import http.client
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C50588521"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "829d94e9f1e462333b8b65b67df3f327"

def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    #需要接受短信的目标手机号
    mobile = "17809296351"
    #短信内容
    text = "验证码为：【5211314】，您正在尝试变更重要信息，请妥善保管账户信息。"
    ret = send_sms(text, mobile).decode('utf-8')
    import json
    ret = json.loads(ret)
    print(ret)