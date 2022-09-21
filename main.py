import practice_mode
import one_minute_mode
import time
import clearing
from practice_mode import Practice
from game import gameMode

# Game mode objects for different levels
level_one = gameMode('Level One', 1, 5)
level_two = gameMode('Level Two', 1, 7)
level_three = gameMode('Level Three', 1, 10)
level_four = gameMode('Level Four', 1, 12)
level_five = gameMode('Level Five', 1, 15)
level_six = gameMode('Level Six', 1, 20)
level_seven = gameMode('Level Seven', 10, 20)
level_eight = gameMode('Level Eight', 10, 50)
level_nine = gameMode('Level Nine', 10, 100)
level_ten = gameMode('Level Ten', 1, 12)

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
        mode = input('Please choose a mode: \n- Game mode [press g]\n- Practice mode [press p]:\n- One Minute mode [press o]\n- Exit [press e]\n ')
        clearing.clear()
        if mode == 'g' or mode == 'G':
            print('GET READY...\n')
            time.sleep(2)
            print('Let\'s start round one!')
            time.sleep(2)
            clearing.clear()
            while True:
                level_one.game_play()
                # if l == False:
                #     break
                level_two.game_play()
                level_three.game_play()
                level_four.game_play()
                level_five.game_play()
                level_six.game_play()
                level_seven.game_play()
                level_eight.game_play()
                level_nine.game_play()
                level_ten.game_play()
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

        elif mode == 'o' or mode =='O':
            one_minute_mode.one_minute_race()

        elif mode == 'e' or mode == 'E':
            print('Thankyou for practising your multiplication skills!')
            time.sleep(10)
            break

        else:
            print(f"Please type a lowercase 'g' or 'p'")

