
def cutString(str):
	while('<' in str):
		start = str.find('<')
		stop = str.find('>')
		smaller = str[:start] + str[stop+1:]
		return cutString(smaller)
	else:
		return str


# needed packages
import os
from bs4 import BeautifulSoup

#getting the current working directory and the book data
place = os.getcwd()
foldername = "HtmlBooks"
data = os.listdir(place + "/" + foldername + "/")
books = []


# getting the html with souping
for name in data:
	if (name[-6:] == ".xhtml"):
		with open(place + "/" + foldername + "/" + name,"r") as f:
			books = books + [BeautifulSoup(f,"html.parser")]


# now one can do whatever with the books:
for b in books:
	#trying to find all of the paragraphs and cut out all of the "<>"
	tags = b.find_all("p")

	for t in tags:
		print(cutString(str(t)))



