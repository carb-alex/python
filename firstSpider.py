#-*- coding : utf-8 -*-
#尝试第一个爬虫
import re
import urllib

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

getHtml("https://www.baidu.com/")
