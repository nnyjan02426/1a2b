# 1A2B game
"""
guess a four digit number.
If a number is correct and at the right place,
"A" + 1

If a number is correct but at the wrong spot,
"B" + 1

If number == answer (A == 4),
You Won!
"""

import random

get_ans = True
game_start = False
guesses = 1


# check if any number is unique
def num_is_unique(num):
    lst_1 = [num[i] for i in range(4)]
    lst_2 = []

    for i in range(4):
        if lst_1[i] in lst_2:
            return False
        lst_2.append(lst_1[i])

    return True


# check if there is any input errors
def input_error(string):
    try:
        string_int = int(string)
    except ValueError:
        print("[ERROR] Enter a four number digit\n")
        return True

    if len(string) != 4:
        print("[ERROR] Enter a four number digit\n")
        return True

    if not num_is_unique(string):
        print("[ERROR] Numbers must not be repeated\n")
        return True

    return False


# generate a random four digit number as answer
# numbers must not be repeated
while get_ans:
    ans = str(random.randint(100, 9999))

    if len(ans) == 3:
        ans = "0" + ans

    if num_is_unique(ans):
        game_start = True
        get_ans = False

    print(ans)

while game_start:
    guess = input(str(guesses) + ": ")
    a = 0
    b = 0

    # main
    if not input_error(guess):
        for i in range(4):
            for n in range(4):
                if guess[i] == ans[n]:
                    if i == n:
                        a += 1
                    else:
                        b += 1

        if a == 4:
            print("\nCongratulations! You Win!")
            print("Guesses: " + str(guesses) + "\n")
            game_start = False

        else:
            print("{a}A{b}B\n".format(a=a, b=b))
            guesses += 1
