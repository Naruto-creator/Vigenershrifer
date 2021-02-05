import logic

def main():

    print("-------------------")
    print("| Vigenere Cipher |")
    print("-------------------\n")

    vc = logic.VigenereCipher()

    keyword = "orchestra"

    plaintext = "A day without laughter is a day wasted."
    print(f'Plaintext:  {plaintext}')

    enciphered = vc.encipher(plaintext, keyword)
    print(f'Enciphered: {enciphered}')

    deciphered = vc.decipher(enciphered, keyword)
    print(f'Deciphered: {deciphered}')


main()
