#!/usr/bin/python3

print("content-type: text/html")
print()

import subprocess as sp,cgi

form=cgi.FieldStorage()
osname=form.getvalue("x")
osimage=form.getvalue("i")
print(osname)
print()

cmd= "sudo docker run -d -i -t --name {0} ubuntu:14.04".format(osname)

output=sp.getstatusoutput(cmd)
status=output[0]
out=output[1]

if status==0:
  print("OS Launched named {} ... ".format(osname))
else:
  print("Some Error : {}".format(out))
