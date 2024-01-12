import random

p = random.randrange(1,100)
l = int(input("please Guess a Number:--"))
print("your random number:--", p)

if(p==l):
    print("You guess correct number")
elif(p<l):
    print("you guess to big number")
else:
    print("you guess a small number")
