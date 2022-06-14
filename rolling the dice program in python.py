import random

def roll(min,max):
    while True:
        n=random.randint(min,max)
        print("number after rolling",n)
        choice=input("want to roll it again ?(y/n)")
        if choice.lower()=='n':#it will break the loop if you input n
            break
roll(1,6)
