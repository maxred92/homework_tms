""" 4* Реализовать кодирование и декодирование ключевых слов для латинского алфавита согласно указанному соответствию (маппингу). 
Шифр (используйте данное соответствие букв при решении задания)
* A B C D E F G H I  J  K L M N O P Q R S T U V W X Y Z
* C R Y P T O A B D E F G H  I  J  K L M N Q S U V W X Z
Пример:
cipher = Cipher()
cipher.encode("Hello world")
"Btggj vjmgp"

cipher.decode("Fjedhc dn atidsn")
"Kojima is genius" """

from string import ascii_lowercase
""" string.ascii_lowercase:
Строчные буквы 'abcdefghijklmnopqrstuvwxyz'. Это значение не зависит от локали и не изменится. """

class Cipher:


    def __init__(self, keyword):
        
        self.alphabet_keyword = self.crypted_alphabet(keyword)

    def encode(self, word):

        encod_dict = dict(zip(ascii_lowercase, self.alphabet_keyword))
        return self.crypt(encod_dict, word)

    def decode(self, word):

        decod_dict = dict(zip(self.alphabet_keyword, ascii_lowercase))
        return self.crypt(decod_dict, word)

    def crypt(self, dictonary, words):

        result_words = ""
        for i in words:
            key = dictonary.get(i.lower(), i)
            result_words += key
        return result_words




cipher = Cipher("CRYPTOABDEFGHIJKLMNQSUVWXZ")
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc, dn atidsn"))
