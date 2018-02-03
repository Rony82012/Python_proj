def summ_list (p):
    sum = 0
    i = 0
    while(i < len(p)):
        sum = sum + p[i]
        i = i + 1
    return sum


print summ_list([2,3])
