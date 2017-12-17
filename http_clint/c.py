#!/usr/bin/python 
#coding:utf-8

import urllib2
import sys
import re

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





doc=get_httpdoc(url)
img_all=jiexi_url(doc)
for img in img_all:
    download(img)


