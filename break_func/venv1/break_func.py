import time
import webbrowser


def breaks(s, n):
    i = 0
    print ("Start Time: "+time.ctime())
    while(i < n):
        time.sleep(s)
        webbrowser.open("https://www.youtube.com/feed/trending") #youtube trending videos, so you may check put on your break
        i = i + 1
        print("Break number: ", i)
        print ("Current Time: " + time.ctime())

    return 0

n = int(input("Total no of breaks needed: "))

s = int(input("Time duration b/w breaks in seconds: "))

breaks(s, n)