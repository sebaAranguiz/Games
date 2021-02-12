#Juego de adivinanza, usando un algoritmo de "Bisection Search"

low = 0
high = 100
guess = int((high+low)/2)

print('Please think of a number between 0 and 100!')

while True:
    print('Is your secret number ' + str(guess)+'?')
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if ans == 'h':
        high = guess
    elif ans == 'l':
        low = guess
    elif ans == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
    guess = int((high+low)/2)

print("Game over. Your secret number was:",guess)