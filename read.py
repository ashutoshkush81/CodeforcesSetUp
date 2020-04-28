#!  /usr/bin/python3
import requests
from bs4 import BeautifulSoup
import sys
import os
from pylatexenc.latex2text import LatexNodes2Text
from sympy import *
import colored
from colored import stylize
import re

def print_centre(s):
    text = ' ' * ((os.get_terminal_size().columns - len(s))//2) + s + '\n'
    color = colored.fg(220) + colored.attr("bold")
    print(stylize(text,color))


# Find url
filename = sys.argv[1] + '.cpp'
try :
    f = open(filename,'r')
    contents = f.read()
    urls = re.findall('(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-?=%.]+', contents)
    url = urls[0]
    f.close()
except :
    print("File not found!")
    sys.exit()
    

page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser' )


# Print Title of the question
title = soup.find(class_='problem-statement').find(class_='header').find(class_='title').contents[0]
print_centre(title)


# Print Problem
problem=soup.find(class_='problem-statement').find(class_='').find_all('p')
for i in problem :
    text = i.contents[0]
    text = ''.join(text.split("$"))
    text = LatexNodes2Text().latex_to_text(text)
    text = ' '.join(text.split(" "))
    print(pretty(text,use_unicode=True))

# Print input Format
color = colored.fg(220) + colored.attr('bold') + colored.attr('underlined')
print(stylize("Input",color))
input_statement = soup.find(class_='problem-statement').find(class_='input-specification').find_all('p')
for i in input_statement :
    text = i.contents[0]
    text = "".join(text.split("$"))
    text = LatexNodes2Text().latex_to_text(text)
    text = ' '.join(text.split())
    print(text)

# Print output Format
color = colored.fg(220) + colored.attr('bold') + colored.attr('underlined')
print(stylize("Output",color))
output_statement = soup.find(class_='problem-statement').find(class_='output-specification').find_all('p')
for i in output_statement :
    text = i.contents[0]
    text = "".join(text.split("$"))
    text = LatexNodes2Text().latex_to_text(text)
    text = ' '.join(text.split())
    print(text)

# Print input and output
color = colored.fg(220) + colored.attr('bold') + colored.attr('underlined')
print(stylize("Example",color))

input_ = soup.find(class_='problem-statement').find(class_='sample-tests').find(class_='sample-test').find_all(class_='input')
output_ = soup.find(class_='problem-statement').find(class_='sample-tests').find(class_='sample-test').find_all(class_='output')
inputtext = []
outputtext = []
for i in input_:
    input__ = i.find_all('pre')
    for j in input__:
       text = j.contents[0]
       inputtext.append(text)

for i in output_:
    output__ = i.find_all('pre')
    for j in output__:
        text = j.contents[0]
        outputtext.append(text)

for i,j in zip(inputtext,outputtext):
    color = colored.fg(177) + colored.attr('bold') + colored.attr('underlined')
    print(stylize("Input",color))
    print(i)
    print(stylize("Output",color))
    print(j)


# Print explnation:

explnation = soup.find(class_='problem-statement').find(class_='note')
if  explnation!=None:
    color = colored.fg(220) + colored.attr('bold') + colored.attr('underlined')
    print(stylize("Note",color))
    explnation = explnation.find_all('p')
    for i in explnation:
        text = i.contents[0]
        text = "".join(text.split("$"))
        text = LatexNodes2Text().latex_to_text(text)
        text = ' '.join(text.split(" "))
        print(pretty(text,use_unicode=True))
        print()

