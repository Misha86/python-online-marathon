"""5 question 4 sprint"""


class Gallows:
    """
    Gallows is class for game
    """
    def __init__(self):
        self.words = []
        self.game_over = False

    def play(self, word):
        if not self.words or (not self.words.count(word) and self.words[-1][-1] == word[0]):
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over"

    def restart(self):
        self.words.clear()
        self.game_over = False
        return "game restarted"


if __name__ == '__main__':
    my_gallows = Gallows()
    print(my_gallows.play('apple'))  # ['apple']
    print(my_gallows.play('ear'))  # ['apple', 'ear']
    print(my_gallows.play('rhino'))  # ['apple', 'ear', 'rhino']
    print(my_gallows.words)  # ['apple', 'ear', 'rhino']
    # Words should be accessible.
    print(my_gallows.restart())  # "game restarted"
    # Words list should be set back to empty.
    print(my_gallows.play('hostess'))  # ['hostess']
    print(my_gallows.play('stash'))  # ['hostess', 'stash']
    print(my_gallows.play('hostess'))  # "game over"
    print(my_gallows.restart())  # "game restarted"
    # Words cannot have already been said.
    print(my_gallows.play('apple'))  # ['apple']
    print(my_gallows.play('ear'))  # ['apple', 'ear']
    print(my_gallows.play('rhino'))  # ['apple', 'ear', 'rhino']
    # Corn does not start with an "o".
    print(my_gallows.play('corn'))  # game over"
    print(my_gallows.words)  # ['apple', 'ear', 'rhino']
    print(my_gallows.restart())  # "game restarted"
    print(my_gallows.words)  # []
