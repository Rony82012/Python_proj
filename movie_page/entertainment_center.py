import movies1
import webbrowser
import fresh_tomatoes


toystory = movies1.Movie("Toy Story",
                         "A Story of a boy and his toys that come to life",
                         "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = movies1.Movie("Avatar",
                       "Humans become aliens on another planet(Pandora)",
                       "https://upload.wikimedia.org/wikipedia/sco/b/b0/Avatar-Teaser-Poster.jpg",
                       "https://www.youtube.com/watch?v=5PSNL1qE6VY")
interstellar = movies1.Movie("InterSterllar",
                             "Earth is on the brink of inhabitability, Humans quest for a safe home through interstellar travel",
                             "http://t1.gstatic.com/images?q=tbn:ANd9GcRf61mker2o4KH3CbVE7Zw5B1-VogMH8LfZHEaq3UdCMLxARZAB",
                             "https://www.youtube.com/watch?v=0vxOhd4qlnA")

movies = [toystory, avatar, interstellar]

avatar.storyline = "Marines on another planet"
avatar.new = "yikes"
#fresh_tomatoes.open_movies_page(movies)
#print("beggining of the program\n\n")

print(movies1.Movie.__doc__)
#print (toystory.title)
#print(toystory.storyline)
print (avatar.storyline)
#print (interstellar.storyline)

#avatar.show_trailer()
#interstellar.show_trailer()
#webbrowser.open_new_tab(toystory.youtube_trailer)