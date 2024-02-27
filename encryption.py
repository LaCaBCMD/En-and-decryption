### Program for encryption and decryption
### Ask whether it should be encrypted or decrypted
### Program should be executed as a loop
### General structure of the programm

i = 0
while i == 0:      #starting the loop
    
    choice = input("encryption (e), decryption (d), close program (any key): ")

    if choice == "e":  #choice encryption 
        code = input("Please enter your password ") #enter password
    
    elif choice == "d":     #choice decryption
        code = input("Please enter your passwort")
    
    else:   #choice closing program
        i = i + 1   #ending the loop
        print("Closing program ... ")