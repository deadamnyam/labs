# упражнение 1
import random


def guessing_game():
    answer = random.randint(0, 100)
    while True:
        user_ans = int(input("Ваш вариант "))

        if user_ans == answer:
            print("Правильно. Ответ:", user_ans)
            break

        if user_ans < answer:
            print("Число", user_ans, "должно быть больше")
        else:
            print("Число", user_ans, "должно быть меньше")


guessing_game()
