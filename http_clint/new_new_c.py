#!/usr/bin/python 
#coding:utf-8

import urllib2
import sys
import re
import requests

#获取网页源代码

def get_httpdoc(url):
    r=requests.get(url)
    http_doc=r.text
    return http_doc

#解析源代码，获取链接中高清图片链接

def jiexi_url(http_doc):
    tem_img_url=re.findall('/tupian/yanwo_v43788/pic_\d{6}.html',http_doc)
    imgurl=[]
    for img in tem_img_url:
        new_img = 'http://www.ivsky.com'+img
        imgurl.append(new_img)
        img_url=list(set(imgurl))
    return img_url

#从高清图片链接中获取图片地址



def get_HDurl(img_url):
    HD_url=[]
    for l in img_url:
        new_ldoc=get_httpdoc(l)
        try:
            tem_l=re.findall('http://img.ivsky.com/img/tupian/pre/201709/17/yanwo-{0,1}\d{0,3}.jpg',new_ldoc)[0]
        except Exception , e:
            pass
        HD_url.append(tem_l)
    return HD_url


#下载高清图片


def download(HDurl):
    print HDurl
    r=requests.get(HDurl)
    fd=r.content
    filename = HDurl.rsplit('/',1)[-1]
    fd1=open(filename,'w+')
    fd1.write(fd)
    fd1.close()



url='http://www.ivsky.com/tupian/yanwo_v43788/'
http_doc = get_httpdoc(url) #获取网页源代码

img_url = jiexi_url(http_doc)
print img_url
HD_url = get_HDurl(img_url)  #获取高清图片的链接
print HD_url

import threading #引入多进程

threads=[]
for l in HD_url:
    t=threading.Thread(target=download,args=(l,))
    threads.append(t)

for t in threads:
    t.start()
for t in threads:
    t.join()


#for HDpic in HD_url:     #下载高清图片
 #   download(HDpic)




