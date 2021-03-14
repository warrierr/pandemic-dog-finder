import requests


class ShelterluvFinder:

    def __init__(self, base_url):
        self.base_url = base_url
        self.dogs = []

    def run(self):
        response = requests.get(self.base_url)
        json_response = response.json()
        dogs = json_response['animals']
        for dog in dogs:
            new_dog = {}
            new_dog['name'] = dog['name']
            new_dog['link'] = dog['public_url']
            new_dog['breed'] = dog['breed']
            if isinstance(dog['photos'], dict):
                for key, photo in dog['photos'].items():
                    if photo['isCover']:
                        new_dog['image_url'] = photo['url']
                        break
            else:
                for photo in dog['photos']:
                    if photo['isCover']:
                        new_dog['image_url'] = photo['url']
                        break

            self.dogs.append(new_dog)
