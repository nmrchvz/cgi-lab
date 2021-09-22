#!/usr/bin/env python3
import cgi, cgitb
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password
form = cgi.FieldStorage()
input_username = form.getvalue('username')
input_password = form.getvalue('password')

print("Set-Cookie:UserID = "+input_username+";")
print("Set-Cookie:Password ="+input_password+";")
print("Content-type:text/html\r\n\r\n")
if (username == input_username and password == input_password):
    print(secret_page(username=input_username, password=input_password))
else:
    print(after_login_incorrect())

#print("<p>Username %s , Password %s</p>" % (username, password))
