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

def decryption(ciphertext,shiftkey):
    plaintext=""
    for char in ciphertext:          
        position=alphabet.index(char)
        newposition=(position-shiftkey)%26
        plaintext+=alphabet[newposition]
    print(f"The text after decryption is: {plaintext}")

end=False
while not end:
    option=input("Type 'e' for encryption and 'd' for decryption:\n")
    text=input("Type your message:")
    shift=int(input("Enter the shift key:\n"))
    if option=="e":
        encryption(plaintext=text,shiftkey=shift)
    elif option=="d":
        decryption(ciphertext=text,shiftkey=shift)
    choice=input("Enter 'yes'to continue or enter 'no'to stop:\n")
    if choice=='no':
        end=True
        print("Closing the terminal, Thank You!")