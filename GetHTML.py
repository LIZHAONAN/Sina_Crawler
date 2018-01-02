# encoding=utf-8

import requests
import GetCookies as GC
import UserAgent as UA
import random

users = {
    '' : '',
    '' : ''
}

cookies = []
for (account, psw) in users.items():
    cookie = GC.get_cookie(account, psw)
    cookies.append(GC.convert_to_dict(cookie))

def getHTML(url):
    cookie = random.choice(cookies)
    header = {'User-Agent': random.choice(UA.agents)}
    r = requests.get(url, cookies=cookie, headers=header)
    return r.text

