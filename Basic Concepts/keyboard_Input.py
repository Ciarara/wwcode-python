#Keyboard input will stop the program flow and asks the user for an input.
#Keyboard input has the ff. syntax: input()
#It can have an optional prompt string: input('Enter your age:')




name = input('Your name: ')
tweet = input('Tweet your day: ')
print('{} tweeted {}' .format(name, tweet)) #String formatting replaces {} with variable values
#print(f'{name} tweeted {tweet}') # New string formatting added on Python 3.6
