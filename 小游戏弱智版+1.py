from random import randint
num = randint(1,20)
print("guess what do i think")
bingo = ("false")

while bingo == ("false"):
    answer = int(input())

    if answer < num:
        print("too small")

    if answer > num:
        print("too much")

    if answer == num:
        print("bingo")
        bingo = ("true")


