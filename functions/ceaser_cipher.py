alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type a shift number to encode:\n"))
shifted_alphabet_one=alphabet[:shift]
shifted_alphabet_two=alphabet[shift:]
shifted_alphabet=shifted_alphabet_two + shifted_alphabet_one

def ceaser(plain_text,shift_amount,choice):
    cipher_text=""
    decoded_text=""
    if choice == 'encode':
        if shift_amount > 26 :
          shift_amount = shift_amount % 26
        for letter in plain_text:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=position+shift_amount
                cipher_text+=alphabet[new_position]
            else:
                cipher_text+=letter   

        print(f"The encoded text is {cipher_text}")  
        shift_amount = int(input("Type the shift number to decode:\n"))
        shift_amount = shift_amount % 26
        for letter in cipher_text:
            if letter in alphabet:
                position=alphabet.index(letter)
                new_position=position-shift_amount
                decoded_text+=alphabet[new_position]
            else:
                decoded_text+=letter     
        print(f"The decoded text is {decoded_text}")            
    
ceaser(plain_text=text,shift_amount=shift,choice=direction) 

should_continue=True
while should_continue:
    result = input("Type yes to continue and no to end:\n").lower() 
    if result == "yes":  
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type a shift number to encode:\n"))
        ceaser(plain_text=text,shift_amount=shift,choice=direction) 
    else:      
        should_continue=False
        print("Goodbye...")        

 
               
        
        

# def encode(msg,number):
#     encoded_text=""
#     for x in text:
#         for y in range(25):
#             if alphabet[y]== x:
#                 encoded_text=encoded_text+shifted_alphabet[y]


#     print(f"The Encoded Text is {encoded_text}") 

        


# def decode(cipher_text,shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position=position-shift_amount
#         plain_text+=alphabet[new_position]
#     print(f"The decoded text is {plain_text}") 

# if direction == 'encode':
#     encode(msg=text,number=shift)   
# else:    
#     decode(cipher_text=text,shift_amount=shift)       

#Todo-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #Todo-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#Todo-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 