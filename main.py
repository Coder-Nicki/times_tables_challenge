import practice_mode
import one_minute_mode
import time
import clearing
from practice_mode import Practice
from game import gameMode
import menu

# Game mode objects for different levels
level_one = gameMode('Level One', 1, 5, 30)
level_two = gameMode('Level Two', 1, 7, 30)
level_three = gameMode('Level Three', 1, 10, 30)
level_four = gameMode('Level Four', 1, 12, 30)
level_five = gameMode('Level Five', 1, 15, 60)
level_six = gameMode('Level Six', 1, 2, 60)
level_seven = gameMode('Level Seven', 10, 20, 120)
level_eight = gameMode('Level Eight', 10, 50, 120)
level_nine = gameMode('Level Nine', 10, 100, 300)
level_ten = gameMode('Level Ten', 10, 900, 600)

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
        choice = menu.main()
        if choice == 'Game Mode':
            print('GET READY...\n')
            time.sleep(2)
            print('Let\'s start round one!')
            time.sleep(2)
            clearing.clear()
                
            while True:
                result = level_one.game_play()
                if result == False:
                    break
                result = level_two.game_play()
                if result == False:
                    break
                result = level_three.game_play()
                if result == False:
                    break
                result = level_four.game_play()
                if result == False:
                    break
                result = level_five.game_play()
                if result == False:
                    break
                result = level_six.game_play()
                if result == False:
                    break
                result = level_seven.game_play()
                if result == False:
                    break
                result = level_eight.game_play()
                if result == False:
                    break
                result = level_nine.game_play()
                if result == False:
                    break
                result = level_ten.game_play()
                if result == False:
                    break
                time.sleep(3)

        elif choice == 'Practice Mode':
            while True:
                difficulty = menu.practice_level()
                clearing.clear()
                print('Let\'s get ready...\n')
                time.sleep(1)
                print('Please type [q] when you want to exit the practice mode')
                time.sleep(3)
                clearing.clear()
                if difficulty == 'Easy':
                    easy.practise_mode()
                    break
                elif difficulty == 'Medium':
                    medium.practise_mode()
                    break
                elif difficulty == 'Hard':
                    hard.practise_mode()
                    break
                else:
                    print('Please type in a lowercase letter e, m or h')

        elif choice == 'One Minute Challenge':
            one_minute_mode.one_minute_race()

        elif choice == 'Exit':
            print('Thankyou for practising your multiplication skills!')
            time.sleep(10)
            break

        else:
            print(f"Please type a lowercase 'g' or 'p'")

