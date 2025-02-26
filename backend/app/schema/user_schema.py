from pydantic import BaseModel
from app.variable import *

class User(BaseModel):
    user_id: str

class SigninForm(User):
    password: str
    name: str
class LoginForm(User):
    password: str
    
class LeaderForm(User):
    is_leader: bool = False 
