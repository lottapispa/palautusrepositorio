from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import string
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user
    
    def check_for_password_form(self, password):
        letters = 0
        numbers = 0
        symbols = 0
        for letter in password:
            if letter.isalpha():
                letters += 1
            elif letter in ["0","1","2","3","4","5","6","7","8","9"]:
                numbers += 1
            else:
                symbols += 1
        return [numbers, symbols]
            

    def validate(self, username, password, password_confirmation):
        if not username or not password:
            raise UserInputError("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
        if len(username) < 3:
            raise UserInputError("Invalid username")

        for letter in username:
            if letter not in string.ascii_lowercase:
                raise UserInputError("Invalid username")

        if len(password) < 8 or len(password) > 20:
            raise UserInputError("Invalid password")
        
        elif self.check_for_password_form(password)[0] < 1 and self.check_for_password_form(password)[1] < 1:
            raise UserInputError("Invalid password")
        
        elif password != password_confirmation:
            raise UserInputError("Passwords don't match")

user_service = UserService()
