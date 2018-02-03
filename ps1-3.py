best = ''
test = ''
for letter in s:
    if test == '':
        test += letter
    elif letter >= test[-1]:
        test += letter
    else:
        if len(test) > len(best):
            best = test
        test = letter
if len(test) > len(best):
    best = test
print(best)
