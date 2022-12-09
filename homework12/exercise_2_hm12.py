""" 2) Создайте класс Validator который позволяет проводить проверку данных пользователя при регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — не менее 6 символов
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Валидация каждого элемента в кортеже производится отдельным методом для каждого элемента (validate_email, validate_login, validate_password)
в которых в случае непрохождения валидации вызывается ошибка (InvalidPassword, InvalidLogin, InvalidEmail), при соответствии — возвращается значение True.
 В методе validate необходимо предусмотреть обработку этих ошибок и в случае их наличия — вызвать ошибку ValidationError. """


import string

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
        if len(self.login) >= 6:
            return True
        else:
            raise InvalidLogin

    def validate_email(self) -> bool:
        if '@' in self.email and self.email[-3] == '.' and self.email[-3:].isalpha():
            return True
        else:
            raise InvalidEmail

    def validate_password(self) -> bool:
        if (len(self.password)>=8 and 
            len ([x for x in self.password if x in string.ascii_uppercase]) > 0 and
            len ([x for x in self.password if x in string.ascii_lowercase]) > 0 and
            len ([x for x in self.password if x in string.punctuation]) > 0):
            return True 
        else:
            raise InvalidPassword
    
    def validate(self):
        try:
            self.validate_login()
            self.validate_password()
            self.validate_email()
        except InvalidLogin:
            raise ValidationError
        except InvalidPassword:
            raise ValidationError
        except InvalidEmail:
            raise ValidationError
        else:
            return True

v = Validator('Maxred92', 'Stayot199*&d4', 'maksimvolkau@gmail.by')
