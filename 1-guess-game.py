# Reuven M. Lerner, Python Workout, упражнение № 1, игра на угадывание


import random, json


def num_guessing_game():
    number = random.randint(0,100)
    num_base = random.randint(2,16)

    print(f'The number base is {num_base}, keep that in mind')
    try:
        guess = int(input('Try to guess the number between 1 and 100: '), num_base)
    except ValueError:
        print('wrong number base bro')
        exit()
    counter = 1
        
    while guess != number and counter < 3:
        if guess > number:
            print('too big')
        else:
            print('too small')
        counter += 1
        try:
            guess = int(input('Try again: '), num_base)
        except ValueError:
            print('wrong number base bro')
            exit()

    if counter >= 3 and guess != number:
        print('Well, you are out if tries')
    else:
        print('Just right! Thanks for playing!')


def word_guessing_game():
    game_dict = {}
    with open('short_dictionary.json', 'r') as f:
        game_dict = json.load(f)
    key_list = list(game_dict.keys())
    
    range_bottom = random.randint(0, len(key_list)-25)
    range_top = range_bottom + 25
    guessed_word_idx = random.randint(range_bottom, range_top+1)

    guessed_word = key_list[guessed_word_idx]
    guessed_word_def = game_dict[guessed_word]

    dashes = '-'*34

    print(f'\n{dashes}\nAlright then, this one can be hard\n{dashes}')
    print('\nYour word is somewhere within this range:')
    print(key_list[range_bottom:range_top])
    print("\nYour word's definition goes as following:")
    print(f'{guessed_word_def}\n')
    guess = input('Now enter your guess here (all lowercase): ')
    for i in range(1,4):
        if guess == guessed_word:
            print("Nicely done! It's a spot-on guess!")
            break
        else:
            if key_list.index(guess) > guessed_word_idx:
                location = 'earlier'
            else:
                location = 'later'
            print(f'Your word is {location} on the list')
            if i == 3:
                break
            else:
                guess = input(f'(Try num. {i+1}: Your guess (all lowercase): ')

if __name__ == '__main__':
    game_choice = int(input('1 - Number game \n2 - Word game \nYour choice: '))
    num_guessing_game() if game_choice == 1 else word_guessing_game()