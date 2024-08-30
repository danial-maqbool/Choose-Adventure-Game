paths = {
    '0': '\nJust as you start your adventure, you come across a cross-road.\nYou find a sign-board saying:-\nLeft: '
         'Danger!\nRight: Path of Heroes! ',
    '0.1': '\nAs you go on the left path, you find the way to be blocked by a river, filled with alligators. You are '
           'scared  to go further but you see a treasure chest on the other side of river. You are tempted to swim and '
           'fight through the alligators ',
    '0.1.1': '\nYou tried to swim through but alligators got you. "That was a dumb move", you thought to yourself as '
             'the alligators devour you. ',
    '0.1.2': '\nYou are back to the crossroads. Do you want to go right or do you plan to go back to left path? ',
    '0.2': '\nYou go on The Path of Heroes.',
    '0.1.2.2': '\nYou go on The Path of Heroes.'
    }

choices = {
    '0.1': 'Left',
    '0.2': 'Right',
    '0.1.1': 'Swim',
    '0.1.2': 'Go Back',
    '0.1.2.1': 'Left',
    '0.1.2.2': 'Right'
    }

deaths = ['0.1.1',]
oneStepBack = ['0.1.2.1']
wins = ['0.2', '0.1.2.2']

user_position = '0'
user_choice = '0.1'
choice1 = '.1'
choice2 = '.2'

while True:
    print(paths[user_position])

    user_choice = input(f'\nChoose: "{choices[user_position+choice1]}" or "{choices[user_position+choice2]}" >> ').lower()

    if user_choice == choices[user_position+choice1].lower():
        user_position = user_position + choice1
        if user_position in oneStepBack:
            user_position = user_position[:-4]
            continue
        if user_position in deaths:
            print(paths[user_position])
            print('\nYOU ARE DEAD!!!')
            break
        continue

    elif user_choice == choices[user_position+choice2].lower():
        user_position = user_position + choice2
        if user_position in wins:
            print(paths[user_position])
            print('\nCongratulations! You walked on to the path of Heroes!! You are a HERO!!!')
            break
        continue

    else:
        print('\n\n\n\n\n\n\nEnter either of the two choices only please!')
        continue

print('Thank you for Playing!\nGame produced by DaBooTi!!')
