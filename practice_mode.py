from random import randint
import time

# Practice mode functions

class Practice:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def practise_mode(self):
        correct_count = 0
        incorrect_count = 0
        start_time = time.time()
        while correct_count < 100:
            num = self.get_numbers()
            answer = input(f'{num[0]} * {num[1]} = ')
            if answer == 'q' or answer == 'Q':
                duration = round(time.time() - start_time, 2)
                if correct_count > 20 and incorrect_count < 3:
                    print(f'You are AMAZING! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                    break
                elif correct_count == 100:
                    print(f'You are a champion! You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!!')
                    break
                else:
                    print(f'You got {correct_count} correct and made {incorrect_count} error/s in {duration} seconds!')
                    break
            elif num[0] * num[1] == int(answer):
                correct_count += 1
                num = self.get_numbers()
                continue
            else:
                incorrect_count += 1
                num = self.get_numbers()
                continue

    def get_numbers(self):
        num1 = randint(self.x, self.y)
        num2 = randint(self.x, self.y)
        return num1, num2 

easy = Practice(1, 7)
medium = Practice(1, 12)
hard = Practice(1, 20)

easy.practise_mode()

