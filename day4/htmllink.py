import re

html_open = open('day4/file.html','r')
file = html_open.read()

file1=re.sub('<.*?>','',file)
file_write=open('day4/file.txt','x')
file_write.write(file1)

html_open.close()
