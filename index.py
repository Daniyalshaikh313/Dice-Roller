import random
while True:
    Common = input("Roll the Dice (y/n):" " ").lower()
    if Common == "y":
        di1 = random.randint(1, 6)
        di2 = random.randint(1, 6)
        print(f'[{di1}, {di2}]')
    elif Common == "n":
        print("Thanks for playing")
        break
    else:
        print("Invalid Input")
          