# jonathan de la cruz Review system

print ("Hello, welcome to Jon's review system")
mediatype = input("Please enter your media type: ")
genre = input("Now enter genre: ")
title = input("Enter title of media: ")
descrip = input("give a brief description: ")
year = input("year of its release: ")
rating = input("What is your rating for this out of 10?: ")
float(rating)

new_list = []
new_list = [mediatype,genre,title,descrip,year,rating]

if mediatype == "movie":
    print movie.append(new_list)
    
if mediatype == "books":
    print books.append(new_list)

if mediatype == "videogames":
    print videogames.append(new_list)

if mediatype == "music":
    print music.append(new_list)

print new_list 
print ("thank you")
