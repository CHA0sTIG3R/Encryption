text = input("Enter a line of text to encrypt: ")
shift = int(input("Enter a shift value: "))
cipher = ""

for char in text:
    if not char.isalpha():
        cipher += char
        continue
    code = ord(char) - shift
    if char.isupper():
        code = (ord(char) + shift - 65) % 26 + 65
        cipher += chr(code)
    elif char.islower():
        code = (ord(char) + shift - 97) % 26 + 97
        cipher += chr(code)
print(cipher)