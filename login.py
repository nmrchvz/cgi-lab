#!/usr/bin/python
import os, json

import cgi, cgitb
from templates import login_page, secret_page, after_login_incorrect
print("Content-type:text/html\r\n\r\n")

print(login_page())

#print(secret_page(username=asd, password=zxc))