import game_mode
import practice_mode
import time
import clearing

# Main code block
name = input('What is your name: ')
clearing.clear()
print(f'Welcome {name} to the timesTables Challenge!')
while True:
    mode = input('Please choose a mode: \n- Game mode [press g]\n- Practice mode [press p]: ')
    if mode == 'g' or mode == 'G':
        clearing.clear()
        print('GET READY')
        time.sleep(3)
        print('Let\'s start round one!')
        time.sleep(3)
        game_mode.round_one()
    elif mode == 'p' or mode == 'P':
        while True:
            difficulty = input('What level do you want to practise?\n- Easy[e]\n- Medium[m]\n- Hard[h]\n')
            if difficulty == 'e' or difficulty == 'E':
                practice_mode.easy_practise()
            elif difficulty == 'm' or difficulty == 'M':
                practice_mode.medium_practise()
            elif difficulty == 'h' or difficulty == 'H':
                practice_mode.hard_practise()
            else:
                print('Please type in a lowercase letter e, m or h')
    else:
        print(f"Please type a lowercase 'g' or 'p'")

