#!/usr/bin/env python3
class Person:
    g1 : Gender
    name :  str
    age : int
    def __init__(self,name,age):
        self.age = age
        self.name = name
    def getName(self) -> str :
        return self.name
    def setName(self,name):
        self.name = name
    def getAge(self) -> int:
        return self.age
    def setAge(self,age) -> int:
        self.age = age
    def getGender(self):
        return self.g1
    def setGender(self):
        self.g1 = Gender()
    def reducedFare():
        if age < 12 or age > 64:
            return True
        else:
            return False
class Gender(Person):
    gender : str
    def __init__(self,name,age):
        super(name,age)
    def __init__(self,name,age,gender):
        self(name,age)
        self.gender = Gender()
class Student(Person):
    college : str
    gpa     : float
    y1      : YearInSchool()
    def __init__(self,name,age,college,gpa):
        super().__init__(name,age)
        self.college =college
        self.gpa = gpa
        self.y1 =  YearInSchool()
    def getCollege() -> str :
        return college
    def setCollege() -> str :
        self.college = college
