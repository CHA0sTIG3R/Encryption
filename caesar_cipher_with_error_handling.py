# input text to encrypt
text = input("Enter message: ")

# enter valid shift value (repeat until it succeeds)
shift = 0

while not shift:
    # use try/except to handle the error when the value entered is not in range
    try:
        # input shift    
        shift = int(input("Enter cipher's shift in range(1 and 25): "))
        if shift not in range(1,26):
            # if true raises value error
            raise ValueError
    # if value error is raised then it will execute this exception
    except ValueError:
        shift = 0
    if not shift:
        print("Invalid value!")

cipher = ''

for char in text:
    # is it a letter?
    if char.isalpha():
        # shift its code
        code = ord(char) + shift
        # find the code of the first letter (upper- or lower-case)
        if char.isupper():
            # make correction
            code = (code - ord('A')) % 26 + ord('A')
            # append encoded character to message
            cipher += chr(code)
        elif char.islower():
            # make correction
            code = (code - ord('a')) % 26 + ord('a')
            # append encoded character to message
            cipher += chr(code)
    else:
        # append original character to message
        cipher += char

print(cipher)