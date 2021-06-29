Wikipedia Scraper

A library for scraping data from Wikipedia. Can be useful in Natural Language Processing, text processing etc. The library can also perform certain tasks on the scraped text such as removing punctutations,numbers,citations, converting text into lower case and tokenization

Installation

pip install wiki-scraper

Getting Started

How to scrape data from the wikipedia article using this library

from wiki_scraper import WikiScraper

scraper = WikiScraper('India')

text = WikiScraper.get_data(remove_punctuations=False,remove_numbers=False,lower_case=False,remove_citations=False,tokenization=False)

