from wiki_scraper import WikiScraper
import unittest
import re
from unittest.case import TestCase
import nltk
from bs4 import BeautifulSoup
import requests

class WikiScraperTestCase(unittest.TestCase):
    def setUp(self):
        self.url = WikiScraper('India')

    def test_get_data(self):
        result = requests.get('https://en.wikipedia.org/wiki/India').content
        soup = BeautifulSoup(result,'html.parser')
        text = ''
        for paragraph in soup.find_all('p'):
            text += paragraph.text
        text = re.sub('\[[^0-9]*\]','',text)
        text = re.sub('\s+','',text)
        text = re.sub('\d','',text)
        text = re.sub('\s+','',text)
        text = text.lower()
        text = re.sub('[^\w\s]','',text)
        text = re.sub('\s+','',text)
        text = nltk.sent_tokenize(text)
        result = self.url.get_data(remove_citations=True,remove_numbers=True,remove_punctuations=True,tokenization=True,lower_case=True)    
        self.assertEqual(result,text)




if __name__=="__main__":
    unittest.main()