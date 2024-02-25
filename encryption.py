### Program for encryption and decryption
### Ask whether it should be encrypted or decrypted
### Program should be executed as a loop
### second file with vars _ check password if password is part of file2

### grober Entwurf (bisher noch fehlerhaft!!!)
choice = input("encryption (e) , decryption (d) , close program (q)")

if choice == "q":   # choice quit program
    print("Closing program ... ")

elif choice == "e":  #choice encryption 
    code = input("Please enter your password ") #enter password
    if password in passwords_ls:
        set code == True:   #checking password if part of file
        print("Welcome ")
    else:
        set code == False #Wrong password entered
        print("Wrong password, closing program ... ")
           
elif choice == "d":     #choice decryption
    code = input("Please enter your passwort")
    if password in password_ls:
        set code == True:
        print("Welcome ")
    
    else:
        set code == False:
        print("Wrong password, closing program ... ")    
        