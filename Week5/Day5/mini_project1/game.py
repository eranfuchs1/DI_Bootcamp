from random import choice


class Game:
    def __init__(self):
        self.input_msg = 'select (r)rock (p)aper or (s)cissors: '
    def get_user_item(self):
        self.choice = input(self.input_msg)
        return self.choice if self.choice in list('rps') else self.get_user_item()
    def get_computer_item(self):
        self.computer_choice = choice(list('rps'))
        return self.computer_choice
    def get_game_result(self, user_item=None, computer_item=None):
        if not user_item:
            user_item = self.choice
        if not computer_item:
            computer_item = self.computer_choice
        rps = 'rps'
        user = rps.index(user_item)
        computer = rps.index(computer_item)
        res = user - computer
        self.result = 'draw' if res == 0 else 'computer' if res == -1 or res == 2 else 'user'
        print('you:', self.choice, 'computer:', self.computer_choice, 'result:', self.result)
        return self.result
    def play(self):
        self.get_user_item()
        self.get_computer_item()
        self.get_game_result()
        return self
