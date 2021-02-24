import os, requests, json, logging

POKEMON_API = '{base_url}/{version}/pokemon/'

class PokeAPI:
    def __init__(self):
        self.api_url = POKEMON_API.format(base_url=os.environ['POKE_API_URL'], version=os.environ['POKE_API_VERSION'])

    def get_info_pokemon(self, pokemon):
        url = self.api_url + pokemon 
        logging.info('Make request to ' + url)

        response = requests.get(url)
        if response.status_code == 200:
            pokemon = self.__parse_to_pokemon__(response)
            logging.info('Parsed of response {res}'.format(res=pokemon))

            return pokemon
        else:
            print('here')
            logging.info('Pokemon {} not found'.format(pokemon))
            return None
        
    def __parse_to_pokemon__(self, response):
        data = json.loads(response.text)
        pokemon = Pokemon()

        # extract needed props of pokemon
        pokemon.set_name(self.__extract_name__(data))
        pokemon.set_type(self.__extract_type__(data))
        pokemon.set_weight(self.__extract_weight__(data))
        pokemon.set_height(self.__extract_height__(data))
        pokemon.set_image_url(self.__extract_image_url__(data))

        return pokemon

    def __extract_name__(self, data):
        return data['name']

    def __extract_type__(self, data):
        return data['types'][0]['type']['name']

    def __extract_weight__(self, data):
        return data['weight']

    def __extract_height__(self, data):
        return data['height']

    def __extract_image_url__(self, data):
        return data['sprites']['other']['official-artwork']['front_default']


class Pokemon:
    def set_name(self, name):
        self.name = name

    def set_type(self, poke_type):
        self.type = poke_type

    def set_weight(self, weight):
        self.weight = weight

    def set_height(self, height):
        self.height = height

    def set_image_url(self, image_url):
        self.image_url = image_url

    def __repr__(self):
        return "Pokemon name: {}, type: {}, weight: {}, height: {}, image_url: {}".format(self.name, 
            self.type, self.weight, self.height, self.image_url)

    def to_dict(self):
        return {
            'name': self.name,
            'type': self.type,
            'height': self.height,
            'weight': self.weight,
            'image_url': self.image_url
        }


api = PokeAPI()
api.get_info_pokemon('1')