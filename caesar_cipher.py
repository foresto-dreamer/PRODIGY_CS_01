#Caesar Cipher-Task1
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
          'n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plaintext,shiftkey):
    ciphertext=""
    for char in plaintext:          
        position=alphabet.index(char)
        newposition=(position+shiftkey)%26
        ciphertext+=alphabet[newposition]
    print(f"The text after encryption is: {ciphertext}")



    
option=input("Type 'e' for encryption and 'd' for decryption:\n")
text=input("Type your message:")
shift=int(input("Enter the shift key:\n"))
if option=="e":
    encryption(plaintext=text,shiftkey=shift)
#elif option=="d":
#  decryption(ciphertext=text,shiftkey=shift)