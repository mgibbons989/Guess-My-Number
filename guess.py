import random
def guess(num,tries):
    guess = None

    while guess != num and tries > 0:
        guess = int(input('Guess: '))
        if guess > num:
            print('Nope! Too high!')
            print(f'You have {tries-1} tries left!')
            tries -= 1
        elif guess < num:
            print('Nope! Too low!')
            print(f'You have {tries-1} tries left!')
            tries -= 1
        
    if guess == num:
        print('Hey! You got it! Congratulations!')
        again = input('Play Again? ')
    elif tries == 0:
        print('Awe! Better luck next time! :(')
        print(f'The number was {num}.')
        again = input('Play Again? ')
    return again.lower()

print('Welcome to our Number Guessing game!')
print('You have seven tries to guess our number(1-50) with the clues given!')
print('Let\'s get going!')
num = random.randint(1,50)
tries = 7
again = guess(num,tries)
while again == 'yes':
    print('Welcome back! You know the rules! Let\'s get into this!')
    num = random.randint(1,100)
    tries = 7
    again = guess(num,tries)
print("Thanks for playing! Have a nice day!")