class def_init_:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.age = age
        self.cgpa = cgpa

class student:
    def __init__(self, name, age, cgpa):
        self.name = name
        self.cgpa = cgpa
        self.age = age
 
def display_info(name, age, cgpa):
    print(name)
    print(age)
    print(cgpa)
    
    
st1 = student("Newton", 12, 3.5)
st2 = student("ola", 23, 4.6)

print(st1.name)

    
    
        