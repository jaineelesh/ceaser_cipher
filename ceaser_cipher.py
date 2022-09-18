import string

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)


def cipher():
    cipher_type = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    message = input("type your message: ")
    shift_number = int(input("What is the shift number: "))

    if cipher_type == "encode":
        print("Here is the encoded message")
    elif cipher_type == "decode":
        print("Here is the decoded message")
        shift_number *= -1

    letters = string.ascii_letters

    result = ""
    for i in message:
        if i == " ":
            result += " "
            continue
        index = letters.index(i)
        new_index = index + shift_number
        if new_index > 51:
            new_index %= 52
        result += letters[new_index]

    return result


status = 'y'
while status == 'y':
    print(cipher())
    status = input("type 'y' to continue and 'n' to exit: ")
