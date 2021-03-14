import re
from dog_finder import DogFinder


class HomeAtLastFinder(DogFinder):


    def __init__(self, base_url, multiple_pages=True, starting_page_index=1):
        super(HomeAtLastFinder, self).__init__(base_url, multiple_pages=multiple_pages)
        self.needs_webdriver = True

    def _extract_dog_htmls(self, content):
        return content.find_all("a", {"class": "details"})

    def _add_dog(self, dog_html):
        dog = {}
        dog['link'] = f'https://www.homeatlastdogrescue.com/adoptable/{dog_html["href"]}'
        dog['name'] = dog_html.find('h1').text
        dog['breed'] = 'Unknown'
        image_div = dog_html.parent
        img_postfix = re.search('\(..(.*)\)', image_div['style']).group(1)
        dog['image_url'] = f'https://www.homeatlastdogrescue.com{img_postfix}'
        self.dogs.append(dog)
