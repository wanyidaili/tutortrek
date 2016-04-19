#!/usr/local/bin/python2.7

# CS304 Final Project TutorTrek(Emma Hower & Wanyi Li)
# Author: Wanyi Li

import sys
import os
import cgi
import cgitb; cgitb.enable()
import cgi_utils_sda

def main():
  fillers = {}
  fillers['scriptname'] = os.environ['SCRIPT_NAME'] if 'SCRIPT_NAME' in os.environ else ''

  fs = cgi.FieldStorage()
  if "uid" not in fs or "choice" not in fs: 
    print "Message: Please fill in the following fields if you want to log in."
  else:
    fillers['uid'] = cgi.escape(fs["uid"].value)
    fillers['choice'] = cgi.escape(fs["choice"].value)
    if fillers['choice'] == "Tutor":
      page = cgi_utils_sda.file_contents('tutortrek_tutor.html')
    if fillers['choice'] == "Admin":
      page = cgi_utils_sda.file_contents('tutortrek_admin.html')
    if fillers['choice'] == "Tutee":
      page = cgi_utils_sda.file_contents('tutortrek_tutee.html')

  return page

if __name__ == '__main__':
  print 'Content-type: text/html\n'
  print main()