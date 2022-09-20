from game_mode import round_one

inputs = iter([5, 10, 1, 9, 0, 5,])

def fake_input():
    return next(inputs)

class TestRoundOne:
# Testing that num1 multiplied by num2 will give a correct answer
    def test_positive(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        num1 = fake_input()
        num2 = fake_input()
        assert num1 * num2 == 50
        num1 = fake_input()
        num2 = fake_input()
        assert num1 * num2 == 9

    def test_zero(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        num1 = fake_input()
        num2 = fake_input()
        assert num1 * num2 == 0


 
   

