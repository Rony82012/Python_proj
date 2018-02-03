class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent construct called")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("child construct called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys




#billy = Parent("Cyrus","Blue")

miley = Child("Cyrus","Brown","17")

#print (billy.last_name)
print (miley.last_name)
print (miley.eye_color)
print (miley.number_of_toys)