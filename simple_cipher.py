#create the pre_cipher string
pre_cipher_string = 'What is the password now?'
print("The pre-cipher string is: " + pre_cipher_string)

#print the default shift
default_shift = -25
print("The default shift is: " + str(default_shift))
print('\n')

#create a function to run the cipher on a string, takes
#the numbers of characters to shift as a secondary argument
def simple_cipher(cipher_string, character_shift):

    #split string into a list
    cipher_list = list(cipher_string)
    print("The pre-cipher list is:") 
    print(cipher_list)
    print('\n')
 

    #create a placeholder list for the final result
    transform_list = []

    #start a loop
    for i in cipher_list:
        
        #convert the character into decimal unicode equivalent, 
        #make sure the unicode equivalent exists
        ord_tmp = ord(i)
        
        #shift the unicode character up 3 characters from where it is
        shifted = ord_tmp + character_shift
        
        if (shifted > 0):
            #add the shifted items into a final list
            transform_list.append(chr(shifted));
        else:
            return print("The character shift value is too low, please choose a higher value")

    #print the post cipher list
    print("The post-cipher list is:") 
    print(transform_list)
    print('\n')
    
    #returns the cipher output as a string
    final_cipher = ''.join(transform_list)
    return print("The cipher string is: " + final_cipher)

#Call the function to join the list items together again and print
simple_cipher(pre_cipher_string, default_shift)

