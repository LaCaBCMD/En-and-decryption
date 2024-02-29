### Program for encryption and decryption of Texts
### Ask whether it should be encrypted or decrypted
### Program should be executed as a loop
### General structure of the programm

counter = 0

disk1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
         "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "!", "?", " "]

disk2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", 
         "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "!", "?", " "]

while counter == 0:      #starting the loop
    
    choice = input("encryption (e), decryption (d), close program (any key): ")  

    if choice == "e":  #choice encryption 
        
        encrypteven = []
        encryptodd = []
        d1indexmarker = []
        d2indexmarker = []
        encryptedtext = []
        
        code = int(input("Please enter your password ")) #enter password. 
        code2 = code + code     
        text = list(str(input("Please enter the text you want to encrypt: ")))
        textlength = len(text)
        textlength2 = int(float((textlength/2)+0.5))
        textlength3 = int(textlength/2)
        
        for y in range(len(text)): #Dividing the text into two lists for better protection
            if y % 2:
                encrypteven.append(text[y])
            else:
                encryptodd.append(text[y])
        for x in range(textlength3):
            d1indexmarker.append(disk1.index(encrypteven[x]))         
        for z in range(textlength2):    #Creating a list to keep track of the indexes
            d2indexmarker.append(disk2.index(encryptodd[z]))
        for i in range(code):   #Shifting the disks to encrypt the text
            disk1.append(disk1.pop(0))
        for j in range(code2):
            disk2.append(disk2.pop(0))
        for h in range(textlength3):
            encrypteven[h] = disk1[d1indexmarker[h]]
        for g in range(textlength2):
            encryptodd[g] = disk2[d2indexmarker[g]]
        for f in range(textlength3):
            encryptedtext.append(encryptodd[f])
            encryptedtext.append(encrypteven[f])
        if len(encryptodd)>len(encrypteven):
            encryptedtext.append(encryptodd[len(encryptodd)-1])
        
        encryptedtextprint = "".join(encryptedtext)
         
        print(encryptedtextprint)
        
        

        
        
        

    elif choice == "d":     #choice decryption
        code = int(input("Please enter your passwort "))
    
    else:   #choice closing program
        counter = counter + 1   #ending the loop
        print("Closing program ... ")
