#!/usr/bin/env python
#coding:utf-8

import socket
import os

HOST=raw_input()
PORT=80
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((HOST,PORT))

http_str=''
http_str +='GET / HTTP/1.1 \r\n'
http_str +='Host:'+HOST+'\r\n\r\n'

c.send(http_str)
s=c.recv(1024)
print s
