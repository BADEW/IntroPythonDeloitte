class Animal(object):
    def __init__(self, startname, age):
        self.name = startname #= attribute
        self.name =age # = attribute
    def description(self): # description here is a method
        print("this is "+ self.name)
        print("he/she is " + str(self.age)+ "years old")


