import game_mode
import practice_mode
import time

# Main code block
name = input('What is your name: ')
print('')
print(f'Welcome {name} to the timesTables Challenge!')
print('')
time.sleep(1)
print('Please choose a mode:')
print('')
time.sleep(1)
mode = input('- Game mode [press g]\n- Practice mode [press p]: ')
print('')
if mode == 'g' or mode == 'G':
    print('')
    print('GET READY')
    time.sleep(3)
    print('Let\'s start round one!')
    time.sleep(3)
    game_mode.round_one()
else:
    difficulty = input('What level do you want to practise?\n- Easy[e]\n- Medium[m]\n- Hard[h]\n')
    print('')
    print('Get ready!')
    time.sleep(2)
    print('')
    if difficulty == 'e' or difficulty == 'E':
        practice_mode.easy_practise()
    elif difficulty == 'm' or difficulty == 'M':
        practice_mode.medium_practise()
    elif difficulty == 'h' or difficulty == 'H':
        practice_mode.hard_practise()
    # else: (Need to factor in user pressing something else)
    #     print('Please type [e], [m] or [h] to choose your difficulty level.')
