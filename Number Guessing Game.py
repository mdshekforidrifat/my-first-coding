import random

secret_number = random.randint(1,20)
guess_count = 0


while True:
    user_input = input('Guess the number 1 between 20 : ')
    if not user_input.isdigit():
        print('Number dew! Text na.')
        continue
    guess = int(user_input)
    guess_count +=1

    if guess < secret_number:
        print('kom hoye giyeche')
    elif guess > secret_number:
        print('beshi hoye giyeche.')
    else:
        print('darun, ekdom thik dorecho!')
        print(f"Tumi {guess_count} bar e guess korecho")
        break
