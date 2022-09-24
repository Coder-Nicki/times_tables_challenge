
import time
from random import randint
import clearing

class gameMode:
    def __init__(self, name, x, y, time):
        self.name = name
        self.x = x
        self.y = y
        self.time = time
    
    def get_numbers(self):
        num1 = randint(self.x, self.y)
        num2 = randint(self.x, self.y)
        return num1, num2 

    def game_play(self):
        correct_count = 0
        incorrect_count = 0
        print(f'{self.name}: \n')
        time.sleep(2)
        start_time = time.time()
        while incorrect_count < 3:
            num = self.get_numbers()
            while True:
                try: 
                    answer = int(input(f'{num[0]} * {num[1]} = '))
                except ValueError:
                    print('Input must be an integer')
                else:
                    break
            if num[0] * num[1] == answer:
                correct_count += 1
                if correct_count == 10:
                    duration = round(time.time() - start_time, 2)
                    if duration < self.time:
                        print(f'Well done you have completed {self.name} in {duration} seconds!')
                        time.sleep(3)
                        clearing.clear()
                        return True
                    else:
                        print(f'Sorry, your time of {duration} seconds was too slow. You are out of the game!')
                        return False
                else:
                    continue
                        
            else:
                print('Incorrect answer')
                incorrect_count += 1
                if incorrect_count == 3:
                    print('Sorry you are out of the game! Better luck next time!')
                    time.sleep(3)
                    return False


