import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.marketwatch.com/latest-news?mod=top_nav'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html,"html.parser")

words = page_soup.findAll(attrs={"class" : "article__headline"})

print(type(words))

i=0
keywordsList = [None] * len(words)
for keywords in words:
	keywordsList[i] = keywords.text.split()
	i+=1

#print(keywordsList)

#for x in range(len(words)):
#	print(keywordsList[x]," ")

Wordlist = []
WordCounter = []


for x in range(len(words)):
	for y in range(len(keywordsList[x])):
		if keywordsList[y] not in Wordlist:
			Wordlist.append(keywordsList[x][y])

		#print(keywordsList[y]," ")

print(Wordlist)