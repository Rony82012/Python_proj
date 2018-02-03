epsilon = 0.01
y = 24.0
guess = y/2.0
numguesses = 0

while abs(guess*guess -y) >= epsilon:
    numguesses +=1
    guess = guess - (((guess ** 2) - y)/(2*guess))
print('numguesses = ' + str(numguesses))
print('Square root of ' +str(y)+ 'is about ' + str(guess)


