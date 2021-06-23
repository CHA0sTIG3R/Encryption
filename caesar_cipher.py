text = input("Enter a line of text to encrypt: ")
shift = int(input("Enter a shift value in range of 1 and 25: "))
cipher = ""
if shift > 25 or shift < 1:
    print("shift value in invalid")
else:
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