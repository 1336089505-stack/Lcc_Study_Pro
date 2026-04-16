from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    address: str

    def __repr__(self):
        return (f"<User id = {self.id},name = {self.name},"
                f"age = {self.age}, sex = {self.sex}>,"
                f"address = {self.address}")