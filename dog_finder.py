from abc import ABC,abstractmethod
from bs4 import BeautifulSoup
import requests

class DogFinder(ABC):

    def __init__(self, base_url, multiple_pages=False, starting_page_index=1):   
        self.base_url = base_url 
        self.multiple_pages = multiple_pages
        self.starting_page_index = starting_page_index
        self.dogs = []

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
        r = requests.get(url)
        return BeautifulSoup(r.text, features="html.parser")

    @abstractmethod
    def _extract_dog_htmls(self, content):
        pass

    @abstractmethod
    def _add_dog(self, dog_html):
        pass
