""" 3. Создайте класс Validator который позволяет проводить проверку данных пользователя при
регистрации передаваемых в виде кортежа (login, password, email)
В данном классе реализовать метод validate(user_data), который позволяет проверить передаваемый кортеж по правилам:
login — от 6 до 10 символов английского алфавит и цифр 0-9 в любой последовательности
password — не менее 8 символов, буквы в верхнем и нижнем регистре, не менее одного специального символа (+-/*! и т.д)
email — присутствует символ @, оканчивается . и 2 символами (.by)
Проверку на соответствие правилам выполнить регулярными выражениями. 
По результатам работы метода validate пользователь получит True если все 3 элемента прошли проверку, в противном случае - False
 """

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

v = Validator('Maxred92', 'Stayot199*&d4', 'maksimvolkau@gmail.by')
v.validate()