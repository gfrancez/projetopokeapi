import requests

def conn(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    r = requests.get(url)
    poke = r.json()
    return poke


def get_id(pokemon):
    poke = conn(pokemon)
    return poke['id']


def get_stats(pokemon):
    poke = conn(pokemon)
    poke_list = []
    for i in poke['stats']:     
        poke_list.append({i['stat']['name']:i['base_stat']})
    
    return poke_list 


def get_moves(pokemon):
    poke = conn(pokemon)
    poke_list = []
    for i in poke['abilities']:
        poke_list.append(i['ability']['name'])
    
    return poke_list


def get_sprite(pokemon):
    poke = conn(pokemon)
    return poke['sprites']['other']['official-artwork']['front_default']


if __name__ == '__main__':
    print(get_stats({'ditto'}))
