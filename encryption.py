##############################################
### Program for encryption and decryption  ###
##############################################

counter = 0

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
                code = int(input("Please enter your shiftcode ")) #enter shiftcode/factor.
                if code >=0:     # Only full and positive numbers check.
                    break        # If full number = exiting loop.
                else:            # else ask give an error message and ask for an new input.
                    print("Invalid input. Do not use negative numbers ")
            except ValueError:   # No letters or floats.
                    print ("Invalid input. Do not use letters or floats. ")
code2 = code * code


while counter == 0: # Starting the loop
    
       
    d1indexmarker = [] # Marks index of disk 1 where disk 1 and index cross
    d2indexmarker = [] # Marks index of disk 2 where disk 2 and index cross
    evenelements = [] # Even signs from text input
    oddelements = [] # Odd signs from text input 
   

    choice = input("encryption (e), decryption (d), close program (any key): ")  # Choice between encryption, decryption or close programm 


###############################################
###           encryption                    ###
###############################################

    if choice == "e":  #choice encryption 
        
        
        encryptedtext = [] # disk where encrypted text goes      
        unencryptedtext = list(str(input("Please enter the text you want to encrypt: ")))
        textlength = len(unencryptedtext)
        textlength2 = int(float((textlength/2)+0.5))
        textlength3 = int(textlength/2)
                

        for y in range(textlength): #Dividing the text into two lists for better protection
            if y % 2:
                evenelements.append(unencryptedtext[y])
            else:
                oddelements.append(unencryptedtext[y])
                
        for x in range(textlength3):
            d1indexmarker.append(disk1.index(evenelements[x]))
                     
        for z in range(textlength2):    #Creating a list to keep track of the indexes
            d2indexmarker.append(disk2.index(oddelements[z]))
            
        for i in range(code):   #Shifting the disks to encrypt the text
            disk1.append(disk1.pop(0))
            
        for j in range(code2):
            disk2.append(disk2.pop(0))
            
        for h in range(textlength3):
            evenelements[h] = disk1[d1indexmarker[h]]
            
        for g in range(textlength2):
            oddelements[g] = disk2[d2indexmarker[g]]
            
        for f in range(textlength3):
            encryptedtext.append(oddelements[f])
            encryptedtext.append(evenelements[f])
            
        if len(oddelements)>len(evenelements):
            encryptedtext.append(oddelements[len(oddelements)-1])
        
        encryptedtextprint = "".join(encryptedtext)
         
        print(encryptedtextprint)
        
        
###############################################
###           decryption                    ###
###############################################


    elif choice == "d":     # Choice decryption
  
         
        encryptedtext = list(str(input("Please enter the text you want to decrypt: ")))
        unencryptedtext = [] # List where the decrypted text goes
        textlength = len(encryptedtext)
        textlength2 = int(float((textlength/2)+0.5))
        textlength3 = int(textlength/2)
        disk1.reverse()
        disk2.reverse()
                        

        for y in range(textlength): #Dividing the encryptedtext into two lists
            if y % 2:
                evenelements.append(encryptedtext[y])
            else:
                oddelements.append(encryptedtext[y])
                
        for x in range(textlength3):
            d1indexmarker.append(disk1.index(evenelements[x]))
                     
        for z in range(textlength2):    #Creating a list to keep track of the indexes
            d2indexmarker.append(disk2.index(oddelements[z]))
            
        for i in range(code):   #Shifting the disk-lists to decrypt the text
            disk1.append(disk1.pop(0))
            
        for j in range(code2):
            disk2.append(disk2.pop(0))
            
        for h in range(textlength3):    #Placing the shifted elements back into the even-/oddelements lists
            evenelements[h] = disk1[d1indexmarker[h]]
            
        for g in range(textlength2):
            oddelements[g] = disk2[d2indexmarker[g]]
            
        for f in range(textlength3):    #Putting the decrypted text together using the shifted even-/oddelements lists
            unencryptedtext.append(oddelements[f])
            unencryptedtext.append(evenelements[f])
            
        if len(oddelements)>len(evenelements):  #Adding the last element in case there are more odd than even elements
            unencryptedtext.append(oddelements[len(oddelements)-1])
        
        unencryptedtextprint = "".join(unencryptedtext)     #Making the unencryptedtext list printable
         
        print(unencryptedtextprint)
 
 
###############################################
###           close program                 ###
###############################################
    
    
    else:   # Choice closing program
        counter = counter + 1   # Ending the loop
        print("Closing program ... ") # Program closed
