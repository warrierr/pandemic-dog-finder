from dog_finder import DogFinder


class PetstablishedFinder(DogFinder):


    def _extract_dog_htmls(self, content):
        return content.find_all("div", {"class": "pet-container"})

    def _is_adoptable(self, dog_html):
        if 'pending adoption' in dog_html.text.lower(): return False
        if 'no longer taking new applications' in dog_html.text.lower(): return False
        return True

    def _add_dog(self, dog_html):
        dog = {}
        a = dog_html.find('a', href=True)
        dog['link'] = f'https://petlover.petstablished.com{a["href"]}'
        dog['name'] = dog_html.find('h3').text
        dog['breed'] = dog_html.find('i', attrs={'class': None}).find(text=True, recursive=False)
        dog['image_url'] = dog_html.find("div", {"class": "pet-thumbnail"})['data-bg']
        self.dogs.append(dog)
