# Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

size = int(input("Enter the size of the dictionary (26 for a-z): "))
ascii_dict = {}

if size == 26:
    alphabet = [chr(ord('a')+ i) for i in range(26)]
    ascii_values = [ord(char) for char in alphabet]
    for i in range(26):
        ascii_dict[alphabet[i]] = ascii_values[i]
    print("Generated Dictionary:")
    print(ascii_dict)
else:
    print("Invalid size. Please enter 26 for a-z,")
