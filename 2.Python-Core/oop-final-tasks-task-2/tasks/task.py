import string

class Cipher:
    @staticmethod
    def __encrypt(key) -> string:
        encrypted_alphabet = key
        for letter in string.ascii_lowercase:
            if letter not in key.lower():
                encrypted_alphabet += letter
        return encrypted_alphabet

    def __shift(self, char) -> int:
        #shift of the letter in the alphabet, positive to the right, negative to the left
        return ord(self.__encrypted_alphabet[ord(char.lower()) - ord('a')])

    def __init__(self, key):
        self.alphabet = string.ascii_lowercase
        self.__encrypted_alphabet = self.__encrypt(key)

    def encode(self, data):
        result = ""
        for char in data:
            if char not in string.ascii_letters:
                result += char
            else:
                result += chr(ord(char) + self.__shift(char) - ord(char.lower()))
        return result
    
    def decode(self, data):
        result = ""
        for char in data:
            if char not in string.ascii_letters:
                result += char
            else:
                encrypted_letter = self.alphabet[self.__encrypted_alphabet.index(char.lower())]
                if char.islower():
                    result += encrypted_letter
                else:
                    result += encrypted_letter.upper()
        return result


if __name__ == '__main__':
    cipher = Cipher("crypto")
    assert cipher.encode("Hello world") == "Btggj vjmgp"
    assert cipher.decode("Fjedhc dn atidsn") == "Kojima is genius"