import os, json
print("Content-type:text/html\r\n\r\n")
print
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

print(os.environ)

for param in os.environ.keys():
    #print(param)
    if(param=="QUERY_STRING"):
        print(param)

for param in os.environ.keys():
    #print(param)
    if(param=="HTTP_USER_AGENT"):
        print(param)