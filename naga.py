Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... 
... print("🎲 Welcome to the Number Guessing Game!")
... number = random.randint(1, 10)
... attempts = 0
... 
... while True:
...     guess = int(input("Guess a number between 1 and 10: "))
...     attempts += 1
... 
...     if guess == number:
...         print(f"🎉 Correct! You guessed it in {attempts} attempts.")
...         break
...     elif guess < number:
...         print("Too low. Try again.")
...     else:
...         print("Too high. Try again.")
