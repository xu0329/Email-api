import json
import random
import re
import string
import time
import requests

#########################
#### mail.cx邮箱配置 ####



def _init_mailcx(mail):

    global mailcx_header
    global mailcx_cookie
    global mailcx_email
    global mailcx_content

    global Email

    mailcx_header= {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization":"",
            "Cookie": "",
    }

    # 此邮箱需要auth验证，此链接用于获取auth，方法post
    mailcx_Auth = "https://api.mail.cx/api/v1/auth/authorize_token"

    # 需要先 get请求在网站生成邮箱
    mailcx_email = 'https://api.mail.cx/api/v1/mailbox/{}'

    # get，邮件/邮件id
    mailcx_content = "https://api.mail.cx/api/v1/mailbox/{}/{}"


    mailcx_email = mailcx_email.format(mail)
    auth = requests.post(mailcx_Auth).json()
    mailcx_cookie = 'auth_token={}; mtd_address={};'.format(auth,mail)
    mailcx_header['Authorization'] = "Bearer {}".format(auth)
    mailcx_header['Cookie'] = mailcx_cookie
    requests.get(mailcx_email, headers=mailcx_header)
    Email=mail
    

def _create_mailcx(temp):
    num=["{}@yzm.de","{}@qabq.com","{}@end.tw","{}@uuf.me"]
    if temp==None:
        temp=num[random.randint(0, 3)].format(''.join(random.sample(string.ascii_letters + string.digits, 8)))
        _init_mailcx(temp)
        return temp 
    else:
        temp=num[random.randint(0, 3)].format(temp)
        _init_mailcx(temp)
        return temp
    
def _extract_verification_code(text):
    # 匹配4位、5位或6位纯数字
    pattern1 = r'\b\d{4,6}\b'

    # 在文本中搜索匹配的模式
    match1 = re.search(pattern1, text)
    
    # 如果找到匹配的验证码且不包含特定单词和联系方式，则返回第一个匹配到的结果
    if match1:
        return match1.group()
    else:
        return None

def _get_emailcx_code():
    while True:
        try:
            get_mailcx_id=requests.get(mailcx_email, headers=mailcx_header)

            # 获取最新邮件的id
            mailcx_id = json.loads(get_mailcx_id.text)[-1]['id']

            if mailcx_id:
                get_mailcx_content = requests.get(mailcx_content.format(Email,mailcx_id), headers=mailcx_header)
                get_mailcx_content = json.loads(get_mailcx_content.text)

                # 邮件内容
                mailcx_content_temp = get_mailcx_content['body']['text']

                # 提取验证码，匹配模式为4-6位数字
                mailcx_code = _extract_verification_code(mailcx_content_temp)
                if mailcx_code:
                    return mailcx_code
                else:
                    pass

            time.sleep(5)

        except:
            pass


def getEmail(email):
    if email==None:
        return _create_mailcx(None)
    else:
        return _create_mailcx(email)

def getEmailCode():
    return _get_emailcx_code()