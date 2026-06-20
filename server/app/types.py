from pydantic import BaseModel

class Cookies(BaseModel):
    session_cookie: str

class Player(BaseModel):
    id: int
    name: str = "Anon"
