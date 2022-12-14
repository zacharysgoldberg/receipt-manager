from fastapi import Request
from typing import Optional
from pydantic import BaseModel


class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.username: Optional[str] = None
        self.pasword: Optional[str] = None

    async def create_oauth_form(self):
        form = await self.request.form()
        self.username = form.get('email')
        self.password = form.get('password')


class ResetPassword(BaseModel):
    email: str
    new_password: str
    confirm_password: str


class UserVerification(BaseModel):
    username: str
    password: str
    new_password: str
