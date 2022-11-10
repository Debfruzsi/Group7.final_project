import random
import requests

def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
        }

def game():

    my_pokemon = random_pokemon()
    print('Your pokemon is {}'.format(my_pokemon['name']))
    print('ID: ' + str(my_pokemon['id']))
    print('Height: ' + str(my_pokemon['height']))
    print('Weight: ' + str(my_pokemon['weight']))

    stat_choice = input('Which stat do you want to use? (id, height, weight) ')
    opponent_pokemon = random_pokemon()
    print('Your opponents pokemon is {}'.format(opponent_pokemon['name']))
    print('ID: ' + str(opponent_pokemon['id']))
    print('Height: ' + str(opponent_pokemon['height']))
    print('Weight: ' + str(opponent_pokemon['weight']))

    my_stat = my_pokemon[stat_choice]
    opponent_stat = opponent_pokemon[stat_choice]

    if my_stat > opponent_stat:
        print('You Win!')

    elif my_stat < opponent_stat:
        print('You Lose!')

    else:
        print('Draw!')
#game()

def replay():
    while True:
        response = input('Do you want to play another round? (y/n)')
        if response == 'y':
            game()
        else:
            break
#replay()

def main():
    print('Welcome to the Pokemon card game!')
    response = input('Would you like to open your surprise pokeball? (y/n)')
    if response == 'y':
        game()
        replay()
    else:
        print('Then you must be Team Rocket!')

main()