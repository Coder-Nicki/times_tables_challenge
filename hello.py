from random import randint

class game_mode:
    def __init__(self, round):
        self.round = round
    def round_one(self):
        correct_count = 0
        incorrect_count = 0
        while correct_count < 10:
            num1 = randint(1, 5)
            num2 = randint(1, 5)
            answer = int(input(f'{num1} * {num2} = '))
            if num1 * num2 == answer:
                correct_count += 1
                if correct_count == 10:
                    print('Well done you have completed round 1!')
                    round_two()
                else:
                    continue
                    
            else:
                incorrect_count += 1
                if incorrect_count == 3:
                    print('Sorry you are out of the game! Better luck next time!')
                    continue

class round_two(game_mode):
    def __init__(self, round):
        super().__init__(round)
    def round_one(self):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
