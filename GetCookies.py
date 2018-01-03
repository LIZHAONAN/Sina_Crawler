# encoding=utf-8

import base64
import json

import requests
import sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

reload(sys)
sys.setdefaultencoding('utf8')

dcap = dict(DesiredCapabilities.PHANTOMJS)  
dcap["phantomjs.page.settings.userAgent"] = (
    "Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"
)

def get_cookie(account, password):
   
    loginURL = "https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)"
    username = base64.b64encode(account.encode("utf-8")).decode("utf-8")
    postData = {
        "entry": "sso",
        "gateway": "1",
        "from": "null",
        "savestate": "30",
        "useticket": "0",
        "pagerefer": "",
        "vsnf": "1",
        "su": username,
        "service": "sso",
        "sp": password,
        "sr": "1440*900",
        "encoding": "UTF-8",
        "cdult": "3",
        "domain": "sina.com.cn",
        "prelt": "0",
        "returntype": "TEXT",
    }
    session = requests.Session()
    r = session.post(loginURL, data=postData)
    jsonStr = r.content.decode("gbk")
    info = json.loads(jsonStr)
    if info["retcode"] == "0":
        print 'Get Cookie Success! User name: %s' % account
        cookie = session.cookies.get_dict()
        return json.dumps(cookie)
    else:
        print 'Get Cookie Failed!'
        return ""

def convert_to_dict(input):
    input = input[1:-2]
    pair = input.split(',')
    dict = {}
    for line in pair:
        key = str(line.split(':')[0]).strip()[1:-1]
        val = str(line.split(':')[1]).strip()[1:-1]
        dict[key] = val
    return dict



