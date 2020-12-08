import urllib.request
import re

link=urllib.request.urlopen('http://ramakrishnavivekananda.info/')
file=link.read()
data = file.decode('utf-8')

text=re.sub('<.*?>','',data)
with open('file.txt','w',encoding='utf-8') as f:
    f.write(text)