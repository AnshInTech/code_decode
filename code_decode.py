alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("""           
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
""")


def cipher(direction_c,text_c,shift_c):
    answer = ""
    if direction_c== "encode":
        for char in text_c:
            j = alphabet.index(char)
            new_postion = j + shift_c
            if new_postion>25:
                new_new = new_postion%26
                k = alphabet[new_new]
                answer+=k
            else:
             k = alphabet[new_postion]
             answer+=k
    elif direction_c=="decode":
       for char in text_c:
            j = alphabet.index(char)
            new_postion = j -shift_c
            if new_postion<0:
                n = -int((new_postion/26))
                new_new = new_postion +26*(n+1)
                k = alphabet[new_new]
                answer+=k
            else:
                k = alphabet[new_postion]
                answer+=k
    print(f"the {direction}d message is {answer}")
game_contuine = True
while  game_contuine :
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt,type 'stop'to stop):\n")
        text_old = input("Type your message:\n")
        shift = int(input("Type the shift number:\n"))
        text = ''.join([i for i in text_old if not i.isdigit()]).lower()

        cipher(direction_c=direction,text_c=text,shift_c=shift)
         
        result = input("do you want to run the code again. \n1.yes \n2.no \n")
        if result == 2:
            game_contuine= False
            print("thanks")

       
           
     
