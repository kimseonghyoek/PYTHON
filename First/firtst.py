#This program says hello and asks for my name
print('Hello, world!')
print('What is your name?')
myname = input()
print('It is good to meet you, ' + myname)
print('The length of your name is:')
print(len(myname))
print('What is your age?')
myAge = input()
print('You will be' + str(int(myAge) + 1) + ' in a year.')