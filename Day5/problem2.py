import re

links = []
url = ''
with open('file.html', 'r') as file:
	url = file.read()
	
links = re.findall("(https?://[^\s]+)", url)


for link in links:
    print(link)
