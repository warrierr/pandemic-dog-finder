import re
from dog_finder import DogFinder


class ProvidenceFinder(DogFinder):

    def __init__(self, base_url, multiple_pages=True, starting_page_index=1):
        super(ProvidenceFinder, self).__init__(base_url, multiple_pages=multiple_pages)
        self.needs_webdriver = True

    def _extract_dog_htmls(self, content):
        return content.find_all("div", {"class": "pet-grid-item"})

    def _add_dog(self, dog_html):
        dog = {}
        dog['link'] = dog_html.find("a")["href"]
        dog['name'] = dog_html.find("h3").text
        dog['breed'] = dog_html.find("p").text
        dog['image_url'] = re.search("\'(.*)\'", dog_html.find("div", {"class": "pet-grid-img"})['style']).group(1)
        self.dogs.append(dog)
