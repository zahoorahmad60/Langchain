from typing import TypedDict

class Person(TypedDict):
    name : str
    age : int


person1 :  Person = {'name':'Zahoor','age': 23}
person2 : Person = {'name':'Ali','age':'23'}


print(person1)
print(person2)  #that's the problem it is taking age as a string as well not showing any error