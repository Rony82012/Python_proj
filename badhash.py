import urllib2
words = urllib2.urlopen("http://www.gutenberg.org/cache/epub/1661/pg1661.txt").split()

print (len(words))
