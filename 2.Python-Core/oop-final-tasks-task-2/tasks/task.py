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
        return ord(self.encrypted_alphabet[ord(char.lower()) - ord('a')]) - ord(char.lower())


    def __init__(self, key):
        self.__key = key
        self.alphabet = string.ascii_lowercase
        self.encrypted_alphabet = self.__encrypt(key)
        # TODO: change encrypted alphabet to private

    def encode(self, data):
        result = ""
        for char in data:
            if char not in string.ascii_letters:
                result += char
            else:
                result += chr(ord(char) + self.__shift(char))
        return result
    
    def decode(self, data):
        result = ""
        for char in data:
            if char not in string.ascii_letters:
                result += char
            else:
                if char.islower():
                    result += self.alphabet[self.encrypted_alphabet.index(char.lower())]
                else:
                    result += self.alphabet[self.encrypted_alphabet.index(char.lower())].upper()
        return result


if __name__ == '__main__':
    # print(string.ascii_letters)
    # print(ord('a'),ord('A'))
    cipher = Cipher("crypto")
    print(cipher.encrypted_alphabet)
    print(cipher.encode("Hello world"))
    print(cipher.decode("Fjedhc dn atidsn"))