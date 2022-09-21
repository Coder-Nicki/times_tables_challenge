import game_mode
import practice_mode
import time
import clearing
from practice_mode import Practice

# Practice mode objects for each difficulty level
easy = Practice(1, 7)
medium = Practice(1, 12)
hard = Practice(1, 20)

# Main code block
if __name__ == '__main__':
    clearing.clear()
    name = input('What is your name: ')
    clearing.clear()
    print(f'Welcome {name} to the timesTables Challenge!')
    while True:
        time.sleep(3)
        clearing.clear()
        mode = input('Please choose a mode: \n- Game mode [press g]\n- Practice mode [press p]:\n- Exit Application [press e]\n ')
        clearing.clear()
        if mode == 'g' or mode == 'G':
            print('GET READY...\n')
            time.sleep(2)
            print('Let\'s start round one!')
            time.sleep(2)
            clearing.clear()
            game_mode.round_one()
            time.sleep(3)

        elif mode == 'p' or mode == 'P':
            while True:
                difficulty = input('What level do you want to practise?\n- Easy[e]\n- Medium[m]\n- Hard[h]\n')
                clearing.clear()
                print('Let\'s get ready...\n')
                time.sleep(1)
                print('Please type [q] when you want to exit the practice mode')
                time.sleep(3)
                clearing.clear()
                if difficulty == 'e' or difficulty == 'E':
                    easy.practise_mode()
                    break
                elif difficulty == 'm' or difficulty == 'M':
                    medium.practise_mode()
                    break
                elif difficulty == 'h' or difficulty == 'H':
                    hard.practise_mode()
                    break
                else:
                    print('Please type in a lowercase letter e, m or h')

        elif mode == 'e' or mode == 'E':
            print('Thankyou for practising your multiplication skills!')
            time.sleep(10)
            break

        else:
            print(f"Please type a lowercase 'g' or 'p'")

