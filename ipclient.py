#!/usr/bin/env python
# coding=utf-8
import os
import urllib2
import urllib
import cookielib
import pytesser
import time
import re
import ipclient_init

cj=cookielib.CookieJar()   #获取cookiejar实例
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)

def get_user_info():
    ipclient_init.USERID = raw_input("请输入用户名:")
    ipclient_init.PASSWD = raw_input("请输入密码:")

def get_cookie():
    opener.open(ipclient_init.WEBSITE)

def get_captcha():
    CAPTCHA=""
    while CAPTCHA == "":
        req=urllib2.Request(ipclient_init.CAPTCHA_URL,'',ipclient_init.HEADER)
        gif=opener.open(req)
        f=open(os.path.join(ipclient_init.CAPTCHA_PATH,'captcha.gif'),'wb')
        f.write(gif.read())
        f.close()
        CAPTCHA = pytesser.image_to_string('./captcha.gif')
    return CAPTCHA

def login():
    match=None
    while match is None:
        time.sleep(1)
        CAPTCHA=get_captcha()
        CAPTCHA=CAPTCHA.strip()
        data={"userid":ipclient_init.USERID,"passwd":ipclient_init.PASSWD,"validnum":CAPTCHA,"imageField.x":0,"imageField.y":0}  #登陆用户名和密码
        post_data=urllib.urlencode(data)   #将post消息化成可以让服务器编码的方式
        req=urllib2.Request(ipclient_init.WEBSITE,post_data,ipclient_init.HEADER)
        content=opener.open(req)
        # 因为重定向，所以要获得最后的url
        token=content.geturl()
        # 判断是否登陆成功
        match=re.match(r'.*tempstr.*',token)
    return token

def keep_alive(token):
    while True:
        res=urllib2.urlopen(token)
        print "保持在线状态"
        time.sleep(50)


if __name__ == '__main__':
    get_user_info()
    get_cookie()
    print "获取cookie成功"
    token = login()
    print "登陆成功"
    keep_alive(token)
