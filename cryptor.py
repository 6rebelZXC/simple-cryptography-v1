from cryptography.fernet import Fernet
  # text
  print("| Simple Cryptography V1 |")
  print("| By https://github.com/xsolisortusx |")
  print("| Key |")
  # Creating Key
cipher_key = Fernet.generate_key()
  print(cipher_key) # Doing Key for encryption
  print('|     |')
  # Encrypting text
cipher = Fernet(cipher_key)
text = input("Input: ").encode()
encrypted_text = cipher.encrypt(text)
  print('|     Encrypted text     |')
print(encrypted_text) # Printing encrypted variant of text. 
  print("|                        |")
  #
  # Decrypting text [EXAMPLE OF DECRYPTION CODE]
print("|      Decryption...     |")
decrypted_text = cipher.decrypt(encrypted_text)
print(decrypted_text) # Printing decrypted variant of text that you put in.
print("|       Decrypted        |")
# TODO:  Adding .EXE interface for using like SoftWare On Windows 10
# If you want to send me updated version(By you) of my code you can easily do it 
# My discord: 𝙋𝘼𝙄𝙉𝙇𝙀𝙎𝙎#0090.
