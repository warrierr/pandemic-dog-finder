from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

class DogFinder(ABC):

    def __init__(self, base_url, multiple_pages=True, starting_page_index=1):
        self.base_url = base_url 
        self.multiple_pages = multiple_pages
        self.starting_page_index = starting_page_index
        self.dogs = []
        self.needs_webdriver = False

    def run(self):
        curr_index = self.starting_page_index

        while True:
            url = self.base_url
            if self.multiple_pages:
                url = f'{url}{curr_index}'

            content = self._fetch_page_content(url)
            dog_htmls = self._extract_dog_htmls(content)
            
            if not dog_htmls: return

            for dog_html in dog_htmls:
                if self._is_adoptable(dog_html):
                    self._add_dog(dog_html)

            if not self.multiple_pages: return
            curr_index += 1

    def _is_adoptable(self, dog_html):
        return True

    def _fetch_page_content(self, url):
        if self.needs_webdriver:
            driver = webdriver.Chrome(executable_path='/Users/ryanwarrier/src/pandemic-dog-finder/chromedriver')
            driver.get(url)
            content = driver.page_source
        else:
            content = requests.get(url).text
        return BeautifulSoup(content, features="html.parser")        

    @abstractmethod
    def _extract_dog_htmls(self, content):
        pass

    @abstractmethod
    def _add_dog(self, dog_html):
        pass
