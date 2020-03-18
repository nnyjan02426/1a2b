import random


def unique(num):
    lst_1 = [num[i] for i in range(4)]
    lst_2 = []

    for i in range(4):
        if lst_1[i] in lst_2:
            return False
        lst_2.append(lst_1[i])

    return True


def input_error(string):
    try:
        string_int = int(string)
    except ValueError:
        print("[ERROR] Please enter a four number digit\n")
        return True

    if len(string) != 4:
        print("[ERROR] Please enter a four number digit\n")
        return True

    if not unique(string):
        print("[ERROR] Numbers must not be repeated\n")
        return True

    return False


def get_a_b(str1, str2):
    """
    :param str1: guess (str)
    :param str2: ans (str)
    :return: a, b (int)
    """
    a = 0
    b = 0

    if not input_error(str1):
        for i in range(4):
            for n in range(4):
                if str1[i] == str2[n]:
                    if i == n:
                        a += 1
                    else:
                        b += 1
    return a, b


class Game:
    def __init__(self):
        self.get_ans = True
        self.game_start = False
        self.guesses = 1

    def ans_func(self):
        while self.get_ans:
            ans = str(random.randint(100, 9999))

            if len(ans) == 3:
                ans = "0" + ans

            if unique(ans):
                self.game_start = True
                self.get_ans = False
        return ans

    def game(self):
        ans = self.ans_func()
        while self.game_start:
            guess = input(str(self.guesses) + ": ")

            a, b = get_a_b(guess, ans)

            if a == 4:
                print("\nCongratulations! You Win!")
                print("Guesses: " + str(self.guesses) + "\n")
                self.game_start = False

            else:
                print("{a}A{b}B\n".format(a=a, b=b))
                self.guesses += 1


game = Game()
game.game()
