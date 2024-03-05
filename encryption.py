##############################################
### Program for encryption and decryption  ###
##############################################

counter1 = 0
counter2 = 0

disk1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", 
         "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", 
         "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
         "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", 
         "4", "5", "6", "7", "8", "9", "0", ".", "!", "?", " "] # Disk 1

disk2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", 
         "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
         "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", 
         "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", 
         "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", 
         "4", "5", "6", "7", "8", "9", "0", ".", "!", "?", " "] # Disk 2

while True:
            try:
                code = int(input("Please enter your shiftcode ")) # Enter shiftcode/factor.
                if code >=0:     # Only full and positive numbers check.
                    break        # If full number = exiting loop.
                else:            # Else ask give an error message and ask for an new input.
                    print("Invalid input. Do not use negative numbers ")
            except ValueError:   # No letters, floats or symbols.
                    print ("Invalid input. Do not use letters, floats or symbols. ")
                    
code2 = (code * code) + 7

while counter1 == 0: # Starting the loop
    
       
    d1indexmarker = [] # Marks index of disk 1 where disk 1 and index cross
    d2indexmarker = [] # Marks index of disk 2 where disk 2 and index cross
    evenelements = []  # Even signs from text input
    oddelements = []   # Odd signs from text input 
   

    choice = input("encryption (e), decryption (d), close program (any key): ")  # Choice between encryption, decryption or close programm 


###############################################
###           encryption                    ###
###############################################

    if choice == "e":   # Choice encryption 
  
        
        while counter2 == 0:
            unencryptedtext = list(str(input("Please enter the text you want to encrypt: ")))   # Enter text
            comp = len(list(set(unencryptedtext) - set(disk1))) # Creating a variable that indicates how many different characters are not suppurtet
            if comp == 0:
                counter2 = counter2 + 1 # Exiting Loop
            elif comp > 1:  # If there are multiple different characters, the user will get that information 
                print("Your text contains", comp, "unsupportet characters, please adjust your text!")
            else:   # If there is only one different character, the user will get that information
                print("Your text contains one unsupportet character, please adjust your text!")
        counter2 = 0    # Setting the counter back to reingage the loop
        
        
        encryptedtext = [] # Disk where encrypted text goes
        textlength = len(unencryptedtext)
        textlength2 = int(float((textlength/2)+0.5))
        textlength3 = int(textlength/2)
                

        for i in range(textlength): # Dividing the text into two lists for better protection
            if i % 2:
                evenelements.append(unencryptedtext[i])
            else:
                oddelements.append(unencryptedtext[i])
                
        for j in range(textlength3):
            d1indexmarker.append(disk1.index(evenelements[j]))
                     
        for k in range(textlength2):    # Creating a list to keep track of the indexes
            d2indexmarker.append(disk2.index(oddelements[k]))
            
        for l in range(code):   # Shifting the disks to encrypt the text
            disk1.append(disk1.pop(0))
            
        for m in range(code2):
            disk2.append(disk2.pop(0))
            
        for n in range(textlength3):
            evenelements[n] = disk1[d1indexmarker[n]]
            
        for o in range(textlength2):
            oddelements[o] = disk2[d2indexmarker[o]]
            
        for p in range(textlength3):
            encryptedtext.append(oddelements[p])
            encryptedtext.append(evenelements[p])
            
        if len(oddelements)>len(evenelements):
            encryptedtext.append(oddelements[len(oddelements)-1])
        
        encryptedtextprint = "".join(encryptedtext)
         
        print(encryptedtextprint)
        
        
###############################################
###           decryption                    ###
###############################################

    elif choice == "d":     # Choice decryption
         
        
        while counter2 == 0:
            encryptedtext = list(str(input("Please enter the text you want to encrypt: "))) # Enter text
            comp = len(list(set(encryptedtext) - set(disk1)))   # Creating a variable that indicates how many different characters are not suppurtet
            if comp == 0:
                counter2 = counter2 + 1 # Exiting loop
            elif comp > 1:  # If there are multiple different characters, the user will get that information 
                print("Your text contains", comp, "unsupportet characters, meaning this programm probably didnt encrypt it!")
            else:   # If there is only one different character, the user will get that information
                print("Your text contains one unsupportet character, meaning this programm probably didnt encrypt it!")
        counter2 = 0    # Setting the counter back to reingage the loop
        
         
        unencryptedtext = [] # List where the decrypted text goes
        textlength = len(encryptedtext)
        textlength2 = int(float((textlength/2)+0.5))
        textlength3 = int(textlength/2)
        disk1.reverse() 
        disk2.reverse()
                        

        for i in range(textlength):     # Dividing the encryptedtext into two lists
            if i % 2:
                evenelements.append(encryptedtext[i])
            else:
                oddelements.append(encryptedtext[i])
                
        for j in range(textlength3):
            d1indexmarker.append(disk1.index(evenelements[j]))
                     
        for k in range(textlength2):    # Creating a list to keep track of the indexes
            d2indexmarker.append(disk2.index(oddelements[k]))
            
        for l in range(code):       # Shifting the disk-lists to decrypt the text
            disk1.append(disk1.pop(0))
            
        for m in range(code2):
            disk2.append(disk2.pop(0))
            
        for n in range(textlength3):    # Placing the shifted elements back into the even-/oddelements lists
            evenelements[n] = disk1[d1indexmarker[n]]
            
        for o in range(textlength2):
            oddelements[o] = disk2[d2indexmarker[o]]
            
        for p in range(textlength3):    # Putting the decrypted text together using the shifted even-/oddelements lists
            unencryptedtext.append(oddelements[p])
            unencryptedtext.append(evenelements[p])
            
        if len(oddelements)>len(evenelements):  # Adding the last element in case there are more odd than even elements
            unencryptedtext.append(oddelements[len(oddelements)-1])
        
        unencryptedtextprint = "".join(unencryptedtext)     # Making the unencryptedtext list printable
         
        print(unencryptedtextprint)
 
 
###############################################
###           close program                 ###
###############################################
        
    else:                             # Choice closing program
        counter1 = counter1 + 1         # Ending the loop
        print("Closing program ... ") # Program closed