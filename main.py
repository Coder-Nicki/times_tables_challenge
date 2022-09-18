import game_mode
import practice_mode
import time


# Main code block
name = input('What is your name: ')
print(f'Welcome {name} to the timesTables Challenge!')
time.sleep(1)
print('')
print('Please choose a mode:')
mode = input('- Game mode [press g]\n- Practice mode [press p]: ')
if mode == 'g' or mode == 'G':
    print('')
    print('GET READY')
    time.sleep(3)
    print('Let\'s start round one!')
    time.sleep(3)
    game_mode.round_one()
else:
    practice_mode = input('What level do you want to practise?\n- Easy[e]\n- Medium[m]\n- Hard[h]\n')
    if practice_mode == 'e':
        practice_mode.easy_practise()
        print('Okay. Great Choice! Let\'s get ready to begin!\nAnytime you want to end the game please type in [quit]')
        practice_mode.easy_practise()
        print(f'Well done you got {correct_count} answers right and made {incorrect_count} answers wrong!')
    elif practice_mode == 'm':
        print('Okay. Great Choice! Let\'s get ready to begin!\nAnytime you want to end the game please type in [quit]')
        time.sleep(3)
        practice_mode.medium_practise()
        print(f'Well done you got {correct_count} answers right and made {incorrect_count} answers wrong!')
    elif practice_mode == 'h':
        print('Okay. Great Choice! Let\'s get ready to begin!\nAnytime you want to end the game please type in [quit]')
        time.sleep(3)
        practice_mode.hard_practise()
        print(f'Well done you got {correct_count} answers right and made {incorrect_count} answers wrong!')
    else:
        print('Please type in a letter for your choice of practice level, [e], [m] or [h]: ')




