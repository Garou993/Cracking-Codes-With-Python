isCode = ""

while isCode != "C" and isCode != "D":
    isCode = input("Do u want to (C)ode or (D)ecode your message: ")
    isCode = isCode.upper()

message = input("Insert your mesasge: ")

if isCode == "C":
    code = ""
    while not code.isdigit():
        code = input("Insert your code(1 to inf): ")

    code = int(code)
    answer = ""

    for i in range(0, code):
        for j in range(i, len(message), code):
            answer += message[j]
    
    print(answer)

elif isCode == "D":
    pass