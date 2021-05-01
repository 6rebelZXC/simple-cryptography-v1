from cryptography.fernet import Fernet
from tabulate import tabulate
from colorama import Fore, Back, Style, init

init()

method = "SCV1"
copyrights = Style.BRIGHT + "Made by https://github.com/xsolisortusx"


def encode(s: str = "None"):
    cipher_key = Fernet.generate_key()
    cipher = Fernet(cipher_key)
    encrypted = cipher.encrypt(s.encode())
    return {"status": 200, "encoded": True, "key": cipher_key.decode(), "text": encrypted.decode()}


def decode(s: str = "None", key: str = "None"):
    cipher = Fernet(key.encode())
    decrypted_text = cipher.decrypt(s.encode())
    return {"status": 200, "decoded": True, "text": decrypted_text.decode()}


def starter():
    # Variables
    #########################################################################
    cipher_key = Fernet.generate_key()                                      #
    cipher = Fernet(cipher_key)                                             #
    print("Enter your secret message")                                      #
    text = input("> ").encode() or b"Nothing"                               #
    encrypted_text = cipher.encrypt(text)                                   #
    decrypted_text = cipher.decrypt(encrypted_text)                         #
    data = [[f"{Back.LIGHTWHITE_EX}{Fore.BLACK}{method}{Style.RESET_ALL}",  #
             f"{Fore.GREEN}{cipher_key.decode()}{Style.RESET_ALL}",         #
             f"{Fore.GREEN}{encrypted_text.decode()}{Style.RESET_ALL}",     #
             f"{Fore.GREEN}{decrypted_text.decode()}{Style.RESET_ALL}"]]    #
    #########################################################################

    print(tabulate(data, headers=["METHOD", "KEY", "ENCRYPTED", "DECRYPTED"], tablefmt="grid"))
    print(f"\n\n{copyrights}")


if __name__ == '__main__':
    starter()

# TODO:  Adding .EXE extension support [IN PROCESS]
# Any updates for this application are acceptable in pull requests
# DISCORD: 𝙋𝘼𝙄𝙉𝙇𝙀𝙎𝙎#0090.