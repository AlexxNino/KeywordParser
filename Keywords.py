import bs4
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


#defining stuff and parse
my_url = 'https://www.marketwatch.com/latest-news?mod=top_nav'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")
words = page_soup.findAll(attrs={"class" : "article__headline"})
i=0
keywordsList = [None] * len(words)
for keywords in words:
	keywordsList[i] = keywords.text.split()
	i+=1



#converting the 2d to 1d array
Wordlist = []
WordCounter = []
for x in range(len(words)):
	for y in range(len(keywordsList[x])):
		if keywordsList[x][y] not in Wordlist:
			Wordlist.append(keywordsList[x][y])
			WordCounter.append(0)
		if keywordsList[x][y] in Wordlist:
			WordCounter[Wordlist.index(keywordsList[x][y])]+=1



#sort the keywords			
def bubbleSort(countie,wordy): 
    n = len(countie) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if countie[j] < countie[j+1] : 
                countie[j], countie[j+1] = countie[j+1], countie[j]
                wordy[j],wordy[j+1] = wordy[j+1],wordy[j]

bubbleSort(WordCounter,Wordlist)



#print the lists
for i in range(len(WordCounter)):
	print(Wordlist[i] , ":" , WordCounter[i])
