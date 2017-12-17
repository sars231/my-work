#!/usr/bin/python 
#coding:utf-8

import urllib2
import sys
import re
import requests


def get_httpdoc(url):
    f=urllib2.urlopen(url)
    return f.read()

def jiexi_url(doc):
    return re.findall('http://img.ivsky.com/img/tupian/t/201709/17/yanwo-{0,1}\d{0,3}.jpg',doc)


def download(img_url):
    fd=urllib2.urlopen(img_url)
    filename = img_url.split('/')[-1]
    fd2=open(filename,'w+')
    fd2.write(fd.read())
    fd2.close()


url='http://www.ivsky.com/tupian/yanwo_v43788/'

r=requests.get(url)
print r.status_code

doc = r.text

img_url = jiexi_url(doc)
for img in img_url:
    download(img)




