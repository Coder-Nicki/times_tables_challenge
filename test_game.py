from game import gameMode

# These tests test that the 2 numbers generated and multiplied will equal the correct answer each time.
inputs = iter([5, 10, 1, 9, 0, 5,])

def fake_input():
    return next(inputs)

class TestLevels:
    def test_positive(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        num1 = fake_input()
        num2 = fake_input()
        assert num1 * num2 == 50
        num1 = fake_input()
        num2 = fake_input()
        assert num1 * num2 == 9

# This tests what happens when 0 is a number being multiplied
    def test_zero(self, monkeypatch):
        monkeypatch.setattr('builtins.input', fake_input)
        num1 = fake_input()
        num2 = fake_input()
        assert num1 * num2 == 0


 
   

