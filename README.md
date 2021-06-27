# Caesar Cipher Encryption

## First program:

**This program takes in 2 inputs:**
1. the first is a text that is going to be encrypted
2. second is a integer which is the shift value
3. Stops running if second value is not in range:

```py
if shift > 25 or shift < 1:
    print("shift value in invalid")
```
## Second program:

**Also takes in 2 inputs:**
1. the first is a text that is going to be encrypted
2. second is a integer which is the shift value
3. Prompts the user to enter another value everytime the second value is not in specified range:

```py
while not shift:
    try:   
        shift = int(input("Enter cipher's shift in range(1 and 25): "))
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift = 0
    if not shift:
        print("Invalid value!")
```

> Difference from the previous program:
>> This does *not* stop running if second value is not in specified range

## Third program:

**Takes in 2 inputs:**
1. the first is a text that is going to be encrypted
2. second is a integer which is the shift value
3. has no range limit for the shift value

> Difference from the previous program:
>>removed the piece of code limiting the shift value:
```py
if shift > 25 or shift < 1:
    print("shift value in invalid")
```


### *Sidenote*
_This program does **NOT** encrypt numbers and special characters_