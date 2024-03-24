# Email-api



## Quick Start

```python
pip install email-api
```


***Get Email***
```python
email_api.getEmail(arg)
```
***Get Verification Code***
```python
email_api.getEmailCode()
```

\
\
**Custom Email Name**
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
**Random Email Name**
```python
import email_api


print(email_api.getEmail(None))
print(email_api.getEmailCode())

########################################

random@example.com
123456

########################################
```


## Note
### The method 'getEmail()' must carry a parameter
For random email, the parameter is None

For custom email, only set the email name without the suffix

```python
import email_api

# name@example.com

[✓] your_email_name='name' 

[x] your_email_name='name@example.com'
```

### About Verification Code Extraction
* **Supports 4-6 digit verification codes consisting of pure numbers**
* **Does not support mixed alphanumeric or pure alphabetic verification codes**

[Verification Code Extraction section *Line 59* ](email_api/emailapi.py/) 

## Support
* [mail.cx](https://mail.cx/#/)


