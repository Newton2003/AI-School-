"""
class exercise:

working with lists, set, dictionaries, and tuples

"""

#create a list of favorite food
fav = ["rice", "beans", "spag", "eba", "amala"]
#create a new list 
new = ["name", "jake"]
#merge the 2 lists
add = fav+new
print(add)
#add a new food item to favorite food at index 2
fav[2]= ("yam")
print(fav)


#create a car dictionary 
car= {
    "brand": "highlander",
    "model":"toyota",
    "year": 2003
}
#print out the model of the car
print(car["model"])


#create a tuple called numbers and print out 
num= {1,1,1,1,1,1,2,2,4,4,4,4,5,6}
print(num)

#create a color set
color = ("yellow", "blue","red")
print(color[2])


