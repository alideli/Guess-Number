import random

def rand_num(a,b):
    random_num = random.randint(a,b)
    return random_num

print("Please enter two numbers to specify a range of numbers")
try:
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    guess = 5
    while(guess != 0):
        print("Guess remaining:", guess)
        num = int(input("Your guess: "))
        if(num == rand_num(a,b)):
            print("Your guess is right!!!")
            break
        elif(num > rand_num(a,b)):
            print("Your guess is bigger than the number\nTry again!")
            guess -= 1
        elif(num < rand_num(a,b)):
            print("Your guess is smaller than the number\nTry again!")
            guess -= 1
    if(guess == 0):
            print("You lost!!!\nThe number was", rand_num(a,b))
except:
    print("Error ===> Please enter numbers!")