#Caesar Cipher-Task1
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plaintext,shiftkey):#hello
    ciphertext=""
    for char in plaintext:          #to get the index
        position=alphabet.index(char)
        newposition=position+shiftkey
        ciphertext+=alphabet[newposition]
    print(f"The text after encryption is {ciphertext}")


    


option=input("Type 'e' for encryption and 'd' for decryption:\n")
text=input("Type your message")
shift=input("Enter the shift key:\n")
if option=="e":
    encryption(plainttext=text,shiftkey=shift)
#elif option=="d":
 #   decryption(ciphertext=text,shiftkey=shift)