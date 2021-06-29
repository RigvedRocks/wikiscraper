import requests
import re
from bs4 import BeautifulSoup
import nltk

class WikiScraper:

    def __init__(self,search_term):
        if search_term == "":
            return 'Please enter a search term'
        wiki_url = 'https://en.wikipedia.org/wiki/'
        self.url = wiki_url + search_term

    def get_data(self,remove_punctuations=False,remove_numbers=False,lower_case=False,remove_citations=False,tokenization=False):
        result = requests.get(self.url).content
        soup = BeautifulSoup(result,'html.parser')
        text = ''
        for paragraph in soup.find_all('p'):
            text += paragraph.text

        
        if remove_citations == True:
            text = re.sub('\[[^0-9]*\]','',text)
            text = re.sub('\s+','',text)

        if remove_numbers == True:
            text = re.sub('\d','',text)
            text = re.sub('\s+','',text)
            
        if lower_case == True:
            text = text.lower()

        if remove_punctuations == True:
            text = re.sub('[^\w\s]','',text)
            text = re.sub('\s+','',text)

        if tokenization == True:
            text = nltk.sent_tokenize(text)
        
        return text
    
    
        