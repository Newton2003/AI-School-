import re
from collections import Counter as count

text = """my name is jack i am 18 year old, 2010 june 2.
this is a new line 
another new  line
"""

#this expression is to find any digit from 0-9
expression = re.findall(r'\d+',text)

#this is to find any word character but with the +, this will has one or more 
c = re.findall(r'\w+',text)

#this is to find all white space 
white_space = re.findall(r'\s',text)

#this if to find all characters except the one in new line 
new_line = re.sub(r'Newton','Jack',text)



freq= count(expression)
print(expression)
print(c)
print(white_space)
print(new_line)
