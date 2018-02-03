import urllib.request
import urllib.parse

def read_text():
    quotes = open("/Users/varunramarajudandu/Desktop/movie_quiotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    return ()

def check_profanity(text):
    data = urllib.parse.urlencode([('q',text)])
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+data)
    output = connection.read()
    #print(output)
    connection.close()
    if 'false' in str(output):
        print("No Profanity")
    else:
        print("Profanity found")


read_text()
