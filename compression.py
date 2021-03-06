from struct import *
import os
def compress():
    input_file=input("Enter text file path in quotes(ex: c://abc.txt):  ")
    maximum_table_size = pow(2, int(os.path.getsize(input_file)))
    n=os.path.getsize(input_file)
    file = open(input_file)
    data = file.read()
    dictionary_size = 256
    dictionary = {chr(i): i for i in range(dictionary_size)}
    string = ""
    compressed_data = []

    for symbol in data:
        string_plus_symbol = string + symbol  # get input symbol.
        if string_plus_symbol in dictionary:
            string = string_plus_symbol
        else:
            compressed_data.append(dictionary[string])
            if (len(dictionary) <= maximum_table_size):
                dictionary[string_plus_symbol] = dictionary_size
                dictionary_size += 1
            string = symbol

    if string in dictionary:
        compressed_data.append(dictionary[string])
    out = input_file.split(".")[0]
    output_file = open(out + ".lzw", "wb")
    for data in compressed_data:
        output_file.write(pack('>H', int(data)))

    output_file.close()
    file.close()

def decompress():
    input_file = input("Enter text file path in quotes(ex: c://abc.txt):  ")
    maximum_table_size = pow(2, int(os.path.getsize(input_file)))
    n = os.path.getsize(input_file)
    file = open(input_file, "rb")
    compressed_data = []
    next_code = 256
    decompressed_data = ""
    string = ""
    while True:
        rec = file.read(2)
        if len(rec) != 2:
            break
        (data,) = unpack('>H', rec)
        compressed_data.append(data)
    dictionary_size = 256
    dictionary = dict([(x, chr(x)) for x in range(dictionary_size)])
    for code in compressed_data:
        if not (code in dictionary):
            dictionary[code] = string + (string[0])
        decompressed_data += dictionary[code]
        if not (len(string) == 0):
            dictionary[next_code] = string + (dictionary[code][0])
            next_code += 1
        string = dictionary[code]
    out = input_file.split(".")[0]
    output_file = open(out + "_decoded.txt", "w")
    for data in decompressed_data:
        output_file.write(data)

    output_file.close()
    file.close()

print("Choice: ")
print("1.Compress:")
print("2.Decompress:")
c = int(input())
if c==1:
    compress()
elif c==2:
    decompress()
else:
    print("Invalid")