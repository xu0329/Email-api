# Email-api


中文 | [English](README_en.md)




## 快速开始

```python
pip install email-api
```


***获取邮箱***
```python
email_api.getEmail(arg)
```
***获取验证码***
```python
email_api.getEmailCode()
```

\
\
**自定义邮箱名称**
```python
import email_api


your_email_name='name'  # name@example.com
print(email_api.getEmail(your_email_name))
print(email_api.getEmailCode())

########################################

name@example.com
123456

########################################
```

\
**随机邮箱名称**
```python
import email_api


print(email_api.getEmail(None))
print(email_api.getEmailCode())

########################################

random@example.com
123456

########################################
```


## 注意
### 方法 getEmail() 必须携带参数
随机邮箱参数为None

自定义邮箱只需设置邮箱名称，不能带入后缀

```python
import email_api

# name@example.com

[✓] your_email_name='name' 

[x] your_email_name='name@example.com'
```

### 关于验证码提取
* **支持纯数字的4-6位验证码**
* **暂不支持混合数字字母或纯字母的验证码**

[验证码提取部分 *Line 59* ](email_api/emailapi.py/) 

## 支持
* [mail.cx](https://mail.cx/#/)


