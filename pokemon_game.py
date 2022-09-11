import random
print("Guess the pokemon game!")
entry = input("Wanna play? yes/no: ").lower()
wanna_play = False
list = ['Pikachu','charizard','blastoise','venasaur']
toatl_pokemon = []
total_points = 1000
pokemons = {
    'pikachu' : '''Also called the mouse pokemon.
Evlove form of pichu.
Fampus attacks are thunderbolt and Agillity.''',
    'charizard' : '''Final evolution of the kanto pokemon charmender.
Face of the famous game pokemon red.
 Fire blast and flamethrower are some of its famous attacks.''',
    'venasaur' : '''Grass/poison type pokemon.
Evolved from ivysaur.
Its most powerful attack is solar beam.''',
    'blastoise' : '''It crushes its foe under its heavy body to cause fainting. 
In a pinch, it will withdraw inside its shell.
It's shell is really hard and is a water type pokemon.'''
}
if entry == 'yes':
    wanna_play = True
    print('''Rules:
    You will be given hints and traits of a pokemon and you have to guess its name.
    You'll be provided 1000 points from the starting.
    You get 300 points and that pokemon if guessed right.
    On doing the wrong guess you'll loose 100 points.
    To exit type quit.
    Let's get started!''')
else:
    quit()
while wanna_play:
    number = random.randint(0, 3)
    pick = list[number].lower()
    print(pokemons.get(pick))
    guess = input("Who's that pokemon: ").lower()
    if guess == pick:
        print(f"Woah you were right it was indeed {pick}.")
        if pick in toatl_pokemon:
            pass
        else :
            toatl_pokemon.append(pick)
        total_points += 300
    elif guess == 'quit':
        break
    else:
        print("Oops! you failed.")
        total_points -= 100
print(f"You earned a total of {total_points} points.")
print('total pokemons caught: ')
output = ''
for i in toatl_pokemon:
        print(i.upper())
print("Thank you")
