#!/usr/bin/env python
# coding=utf-8
# init
# 登陆地址
WEBSITE = "http://172.16.12.11/ipmanager/index0.jsp"
# 获取验证码的地址
CAPTCHA_URL="http://172.16.12.11/ipmanager/servlet/randomnum?t=1447674157008"
# 验证码生成目录
CAPTCHA_PATH="./"
# 用户学号
USERID = ""
# 用户密码
PASSWD = ""
#自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）
HEADER ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
