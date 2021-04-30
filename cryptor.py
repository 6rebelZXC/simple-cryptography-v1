from cryptography.fernet import Fernet
print("| Simple Cryptography V1 |")
print("| By https://github.com/xsolisortusx |")
print("| Key |")
cipher_key = Fernet.generate_key()
print(cipher_key) # APM1JDVgT8WDGOWBgQv6EIhvxl4vDYvUnVdg-Vjdt0o=
print('|     |')
cipher = Fernet(cipher_key)
text = input("Input: ").encode()
encrypted_text = cipher.encrypt(text)
print('|     Encrypted text     |')
print(encrypted_text)
print("|                        |")
# (b'gAAAAABXOnV86aeUGADA6mTe9xEL92y_m0_TlC9vcqaF6NzHqRKkjEqh4d21PInEP3C9HuiUkS9f'
# b'6bdHsSlRiCNWbSkPuRd_62zfEv3eaZjJvLAm3omnya8=')

print("|      Decryption...     |")
decrypted_text = cipher.decrypt(encrypted_text)
print(decrypted_text) # 'My super secret message'
print("|       Decrypted        |")
# TODO:  Adding .EXE interface for using like SoftWare On Windows 10
# If you want to send me updated version(By you) of my code you can easily do it 
# My discord: 𝙋𝘼𝙄𝙉𝙇𝙀𝙎𝙎#0090.