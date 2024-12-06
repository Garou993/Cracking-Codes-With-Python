from random import shuffle

isCode = ""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while isCode != "C" and isCode != "D" and isCode != "G":
    isCode = input("Do u want to (C)ode, (D)ecode or code with (G)enerated key your message: ")
    isCode = isCode.upper()

message = input("Insert your mesasge: ")
message = message.upper()

if isCode == "C":
    code = ""
    while len(code) != 26:
        code = input("Insert your code(Random alphabet order): ")

    answer = ""
    for letter in message:
        asciiLetter = ord(letter)
        if asciiLetter > 65 and asciiLetter < 90:
            answer += code[ALPHABET.index(letter)]
        else:
            answer += letter
    
    print(answer)

if isCode == "D":
    code = ""
    while len(code) != 26:
        code = input("Insert your code(Random alphabet order): ")

    answer = ""
    for letter in message:
        asciiLetter = ord(letter)
        if asciiLetter > 65 and asciiLetter < 90:
            answer += ALPHABET[code.index(letter)]
        else:
            answer += letter
    
    print(answer)

if isCode == "G":
    code = list(ALPHABET)
    shuffle(code)
    code = ''.join(code)

    answer = ""
    for letter in message:
        asciiLetter = ord(letter)
        if asciiLetter >= 65 and asciiLetter <= 90:
            answer += code[ALPHABET.index(letter)]
        else:
            answer += letter
    
    print(answer)
    print("Your code is:", code)