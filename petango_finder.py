import re
from dog_finder import DogFinder


class PetangoFinder(DogFinder):


    def _extract_dog_htmls(self, content):
        return content.find_all("div", {"class": "animal-template"})


    def _add_dog(self, dog_html):
        dog = {}
        dog['link'] = dog_html.find('a', {"class": "mini-profile-link"}, href=True)['href']
        dog['name'] = dog_html.find('span', attrs={'data-bind': 'text: name'}).text
        dog['breed'] = dog_html.find('span', attrs={'data-bind': 'text: breed'}).text
        dog['image_url'] = re.search('\"(.*)\"', dog_html.find("div", {"class": "animal-image"})['style']).group(1)
        self.dogs.append(dog)
