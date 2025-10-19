"""
class exercise: 

basics of list, dictionaries, tuples and sets

"""

Name = "olamide"
age = 29
gpa = 4.5

print("my name is ", Name, "and i am ", age, "years old and my gpa is ",gpa)

print(type(Name))
print(type(age))
print(type(gpa))


#Lists

fruit = ["orange", "apple", "grape"]
print(fruit)

fruit.append("bannana")
print(fruit)



#dictionary

Student = {
"Name": "jhon",
"Age": 13,
"grade": 'A'
}

print(Student["Age"])
print(Student["Name"])
print(Student["grade"])



#set

num = {1,2,2,3,4,5}
print(num)


#Tuple

coordinate = (10.5, 3.0)
print(coordinate[0])