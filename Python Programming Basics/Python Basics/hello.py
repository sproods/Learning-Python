#This program says hello and asks for my name.

print('\nHello world!')
print('What is your name?')     # ask for my name.
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is', len(myName))
# print(len(myName))
print('What is your age?')      # asd for my age.
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')
