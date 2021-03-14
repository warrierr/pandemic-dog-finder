from dog_finder import DogFinder


class MorrisAnimalRefugeFinder(DogFinder):

    def _extract_dog_htmls(self, content):
        return content.find_all("div", {"class": "card-inner"})

    def _add_dog(self, dog_html):
        dog = {}
        dog['link'] = f'https://www.morrisanimalrefuge.org{dog_html.find("a")["href"]}'
        dog['name'] = dog_html.find("div", {"class": "card-info-title"}).text
        dog['breed'] = 'Unknown'
        dog['image_url'] = f'https://www.morrisanimalrefuge.org{dog_html.find("img")["src"]}'
        self.dogs.append(dog)
