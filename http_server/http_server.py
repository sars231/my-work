#!/usr/bin/env python
#coding:utf-8
import socket
import os
HOST="0.0.0.0"
PORT=80
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
def do_http(sock):
    str1=sock.recv(1024)
    print str1
    http_str = ""
    http_str +='HTTP/1.1 200 OK \r\n'
    http_str +='Content-Type: text/html;charset=utf-8\r\n'
    http_str +='Server:bo-uncle\r\n\r\n'
    str2 = str1.split('\r\n')[0].split(' ')[1]
    if str2 == "/":
        fd1=open('index.html','r')
        http_str += fd1.read()
        fd1.close()
    elif str2 == "/about":
        fd2=open('about.html','r')
        http_str +=fd2.read()
        fd2.close()
    else:
        fd3=open('error.html','r')
        http_str +=fd3.read()
        fd3.close()
    sock.send(http_str)
    sock.close()
while 1:
    sock,addr=s.accept()
    p=os.fork()
    if p==0:
        print addr
        do_http(sock)
    else:
        sock.close()
