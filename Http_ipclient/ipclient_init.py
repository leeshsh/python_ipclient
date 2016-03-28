#!/usr/bin/env python
# coding=utf-8
# init
# 登陆地址
WEBSITE = "http://gl.666gps.com/JP/PublicServices/gdjp/log.aspx"
# 获取验证码的地址
CAPTCHA_URL="http://gl.666gps.com/JP/PublicServices/gdjp/checkimage.aspx?t=1447674157008"
# 验证码生成目录
CAPTCHA_PATH="./"
# 用户学号
USERID = ""
# 用户密码
PASSWD = ""
#自己设置User-Agent（可用于伪造获取，防止某些网站防ip注入）
HEADER ={"User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
