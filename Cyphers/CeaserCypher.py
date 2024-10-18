isCode = ""

while isCode != "C" and isCode != "D":
    isCode = input("Do u want to (C)ode or (D)ecode your message: ")
    isCode = isCode.upper()

message = input("Insert your mesasge: ")
message = message.upper()

def transformLetter(letter, code): 
    asciiLetter = ord(letter)
    if asciiLetter < 65 or asciiLetter > 90:
        return letter
    elif asciiLetter + code <= 90:
        return chr(asciiLetter + code)
    else:
        return chr(code - 26 + asciiLetter)

if isCode == "C":
    code = ""
    while not code.isdigit():
        code = input("Insert your code(1 to inf): ")

    code = int(code)
    if code > 25:
        code %= 26

    answer = ""
    for letter in message:
        answer += transformLetter(letter, code)
    
    print(answer)

elif isCode == "D":
    print("Smth of this is your answer:")
    for code in range(1, 26):
        answer = ""
        for letter in message:
            answer += transformLetter(letter, code)            
        
        print(code, ". ", answer)