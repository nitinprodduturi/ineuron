'''

XOR algorithm of encryption and decryption converts the plain text in the format ASCII bytes and uses XOR procedure to convert it to a specified byte. It offers the following advantages to its users −

Fast computation
No difference marked in left and right side
Easy to understand and analyze
Code
'''

import random
import string
def Encrypt(filename):
    file=open(filename, 'rb')
    data=file.read()
    file.close()
    data=bytearray(data)
    tar_word="\\"
    res=f.rindex(tar_word)
    Folder_Location=f[0:res + 1]

    key_file = open(Folder_Location + "key.key", 'w')
    for i in range(5):
        key_file.write(random.choice(string.ascii_letters))
    key_file.close()
    print("\nGenerated your key in a file named 'key.key'.")
    print("Keep it safe to access the file.\n")

    with open(Folder_Location + 'key.key', 'r') as my_key:
        key_data = my_key.read()

    print("Encryption going on\nPlease wait.")
    key_data = [ord(key_val) for key_val in (key_data)]
    for key in key_data:
        for index, value in enumerate(data):
            data[index] = value ^ key

    filename = f[res + 1:]
    file = open(Folder_Location + "--Encrypted--" + filename, "wb")
    file.write(data)
    file.close()

    encrypted_file_name = "--Encrypted--" + filename
    print(f"Successfully encrypted the file with name '{encrypted_file_name}'")


def Decrypt():
    filename_with_location = input("Enter filename in quotes:\n")
    filename_with_location = filename_with_location[1: len(
        filename_with_location) - 1]
    file = open(filename_with_location, 'rb')
    data = file.read()
    file.close
    data = bytearray(data)
    Key_Location = input("Enter key of the file path in quotes:\n")
    Key_Location = Key_Location[1: len(Key_Location) - 1]
    with open(Key_Location, 'r') as my_key:
        key_data = my_key.read()

    key_data = [ord(key_val) for key_val in (key_data)]
    for key in key_data:
        for index, value in enumerate(data):
            data[index] = value ^ key
    tar_word = "\\"
    res = filename_with_location.rindex(tar_word)
    Folder_Location = filename_with_location[0:res + 1]
    filename = filename_with_location[res + 1:]

    file = open(Folder_Location + "--Decrypted--" + filename, "wb")
    file.write(data)
    file.close()

    print("\n")
    Decrypted_file_name = "--Decrypted--" + filename
    print(f"Successfully Decrypted the file with name as:  '{Decrypted_file_name}'")


print("Choice: ")
print("1.Encryptiion:")
print("2.Decryption:")
c = int(input())
if c==1:

    f=input("\nEnter filename in quotes:\n")
    f= f[1: len(f) - 1]
    Encrypt(f)
elif c==2:
    print("\n")
    Decrypt()
else:
    print("Invalid")