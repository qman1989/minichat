#!/usr/bin/env python2
# coding=utf-8
import hashlib
import markdown2
import datetime

def gravatar(email, size="80", default="identicon"):
    if not email: return None
    '''生成GravatarURL'''
    email = email.encode('utf-8')
    email = hashlib.md5(email).hexdigest()
    url = "http://1.gravatar.com/avatar/%s?s=%s&d=%s&r=G" % (
        email,size,default)
    return url

def escape(raw):
    '''HTML转义'''
    escape_dict = {
        "<": "&lt;",
        ">": "&gt;",
        "\"": "&quot;",
        "\'": "&apos;",
        "&": "&amp;",
    }
    for key in escape_dict:
        raw = raw.replace(key, escape_dict[key])
    return raw

def markdown_to_html(raw):
    """将markdown格式文本转换为HTML"""
    html = markdown2.Markdown().convert(raw)
    return html

def strtime(time, time_format="%y-%m-%d %H:%M"):
    '''时间格式化，strftime的重命名，但是带默认参数'''
    return datetime.datetime.strftime(time, time_format)
