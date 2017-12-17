#!/usr/bin/env python
# coding=utf-8
import requests


def download(HDurl):
    print HDurl
    r=requests.get(HDurl)
    fd=r.content
    filename = HDurl.rsplit('/',1)[-1]
    fd1=open(filename,'w+')
    fd1.write(fd)
    fd1.close()

HDurl = 'http://www.ivsky.com/download_pic.html?picurl=/img/tupian/pic/201709/17/yanwo.jpg'

download(HDurl)

