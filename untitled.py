lst = []
num = []
for i in range(0,27,1):
    if i == 0:
        num = ["1","3"]
        print num
    elif i==1:
        num
    elif i ==2:
        num = ["1","5"]
        print num
    elif i == 24:
        num = ["21","25"]
        print num
    elif i == 26:
        num = ["23","25"]
        print num
    elif i % 3 == 0 and i!= 0:
        lst = ["i - 3","i+1","i+3"]
        
        print num
    elif (i+2)%3 == 0:
        num = ["i-3","i-1","i+3"]
        print num
    else:
        num = ["i-3","i-1","i+1","i+3"]
        
       
