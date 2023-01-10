import re


class InvalidLogin(Exception):
    pass
class InvalidPassword(Exception):
    pass
class InvalidEmail(Exception):
    pass
class ValidationError(Exception):
    pass


class Validator:
    def __init__(self, login: str, password: str, email: str) -> bool:
        self.login = login
        self.password = password
        self.email = email


    def validate_login(self) -> bool:
        if re.match(r'^[A-Za-z][A-Za-z0-9_]{6,10}$', self.login):
            return True
        else:
            raise InvalidLogin

    def validate_email(self) -> bool:
        if re.match(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[by]', self.email):
            return True
        else:
            raise InvalidEmail

    def validate_password(self) -> bool:
        if re.match(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$', self.password):
            return True 
        else:
            raise InvalidPassword

    def validate(self):
        try:
            self.validate_login()
            self.validate_password()
            self.validate_email()
        except (InvalidLogin, InvalidPassword, InvalidEmail):
            raise ValidationError
        else:
            return True