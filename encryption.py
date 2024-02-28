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
        code = int(input("Please enter your password ")) #enter password
        text = list(str(input("Please enter the text you want to encrypt: ")))
        textlenght = len(text)
        for y in range(textlenght): #Dividing the text into two lists for better protection
            if y % 2:
                encrypteven.append(text[y])
            else:
                encryptodd.append(text[y])
                
        print(encryptodd)
        print(encrypteven)
            
        
        
        
        
        
        
        
        
        
        for i in range(code):
            disk1.append(disk1.pop(0))
        for j in range(code^2):
            disk2.append(disk2.pop(0))
        
        
        

    elif choice == "d":     #choice decryption
        code = int(input("Please enter your passwort "))
    
    else:   #choice closing program
        counter = counter + 1   #ending the loop
        print("Closing program ... ")