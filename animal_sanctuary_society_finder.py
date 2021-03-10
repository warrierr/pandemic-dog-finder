from dog_finder import DogFinder


class AnimalSanctuarySocietyFinder(DogFinder):


    def _extract_dog_htmls(self, content):
        return content.find_all("div", {"class": "views-col"})


    def _add_dog(self, dog_html):
        dog = {}
        a = dog_html.find("div", {"class": "views-field-field-animalname"}).find('a', href=True)
        dog['link'] = f'https://www.animalsanctuarysociety.org{a["href"]}'
        dog['name'] = a.text
        dog['breed'] = 'Unknown'
        dog['image_url'] = f'https://www.animalsanctuarysociety.org{dog_html.find("img")["src"]}'
        self.dogs.append(dog)
