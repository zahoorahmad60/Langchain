from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=4, default=2.5,description="A decimal point value that is representing the score of a particular student")

    #regex (you can parse the input in any regex format like phone number)

struct_dict = {'name': 'Zahoor', 'age': 23,'email':'abc@gmail.com','cgpa':3}


student1 = Student(**struct_dict)

print(f"This is simple python Dictionary: {student1}")
#dictionary format
student1_dict = dict(student1)
print(f"Here i'm converting the object into Dict and printing the students age: {student1.age}")


#json format
student1_json = student1.model_dump_json()
print(f"Here is the Json format of out object {student1_json}")