#!  /usr/bin/python3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from html.parser import HTMLParser
import re
import sys
import os
import subprocess
from termcolor import colored, cprint

#Getting urls from the file 
filename = sys.argv[1] + '.cpp'
try :
    f = open(filename,'r')
    contents = f.read()
    urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', contents)
    urls = urls[0]
    f.close()
except :
    cprint("File not found!",'red','on_magenta',attrs=['bold','underline','blink'])
    sys.exit()

#Getting data from the urls
class problem_parser(HTMLParser):
  def __init__(self):
    HTMLParser.__init__(self)
    self.reading = False
    self.input = []
    self.output = []
    self.buffer = ""

  def handle_starttag(self, tag, attrs):
    if tag == "pre":
      self.reading = True

  def handle_endtag(self, tag):
    if tag == "pre":
      self.reading = False
      if len(self.input) == len(self.output):
        self.input.append(self.buffer)
      else:
        self.output.append(self.buffer)
      self.buffer = ""

  def handle_data(self, data):
    if self.reading:
      self.buffer += data + '\n'

while True:
  problem = urlopen(urls)
  if problem.geturl() != urls:
    break
  else:
    text = problem.read()
    parser = problem_parser()
    parser.feed(text.decode('utf-8'))
    inputnumber = 1
    if len(parser.input) != len(parser.output):
      cprint("Error with problem!",'red','on_black',attrs=['bold','underline','blink'])
    else:
        for test_case,output in zip( parser.input,parser.output):
            print()
            cprint("Sample-Test-Case "+str(inputnumber),'yellow','on_blue',attrs=['bold','dark'])
            print(test_case)
            cprint("Your Output",'yellow','on_blue',attrs=['bold','dark'])
            data , temp = os.pipe()
            os.write(temp,bytes(test_case,'utf-8'))
            os.close(temp)
            try :
                s = subprocess.check_output("g++ "+ filename,shell=True)
                if s.decode('utf-8')!=None:
                    s = subprocess.check_output("./a.out",stdin=data,shell=True)
                    print(s.decode('utf-8'))
            except :
                cprint("error in compilation !",'red','on_cyan',attrs=['bold','underline','blink'])
                sys.exit()

            cprint("Expected Output",'yellow','on_blue',attrs=['bold','dark'])
            print(output)
            inputnumber=inputnumber+1
            flag = True
            for i , j in zip(output.strip(),s.decode('utf-8').strip()):
                if i!=j:
                    cprint('Wrong Answer!','red','on_grey',attrs=['bold','underline','blink'])
                    flag = False
                    break
            if flag:
                cprint('Accepted','green','on_grey',attrs=['bold','underline','blink'])


  sys.exit()
