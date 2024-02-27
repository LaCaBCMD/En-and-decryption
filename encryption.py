### Program for encryption and decryption
### Ask whether it should be encrypted or decrypted
### Program should be executed as a loop
### General structure of the programm

counter = 0
disk1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
disk2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
while counter == 0:      #starting the loop
    
    choice = input("encryption (e), decryption (d), close program (any key): ")

    if choice == "e":  #choice encryption 
        code = input("Please enter your password ") #enter password
    
    elif choice == "d":     #choice decryption
        code = input("Please enter your passwort")
    
    else:   #choice closing program
        counter = counter + 1   #ending the loop
        print("Closing program ... ")