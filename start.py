import requests
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')

url = 'http://techcrunch.com/2016/05/26/snapchat-series-f/'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
title = soup.find('title').get_text()
document = ' '.join([p.get_text() for p in soup.find_all('p')])
print(title)
print(document)

document = re.sub('[^A-Za-z .-]+', ' ', document)
document = ' '.join(document.split())
document = ' '.join([i for i in document.split() if i not in stop])