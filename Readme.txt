# TEA23_project 

#######################

Creators:             

Fabian Wulf
Nicklas Fischer
Raphael Boelts

#############################################################################################################################################

English

############

Program for encryption and decryption.


When running the program, the user is prompted to choose between "Encrypt", "Decrypt" and "Close program".

Following the selection just made, a shiftcode and an entry to be encrypted or decrypted are requested.  

The user's input is saved in a list (encrypted or decrypted text). There depending on the position of the letters / spaces 
(whether even or odd) is divided into two lists. List 1 (odd positions) is shiftet by the shiftfactor during encryption. 
List 2 (even positions) is shifted by the shiftfactor (squared + 7) during encryption.

If the user decides to exit the program directly, it closes automatically. (Pressing any key except of e or d )

When decrypting, the lists are reversed and shifted.

All letters in upper and lower case are permitted as input as well as numbers from 0-9 and . ! spaces and question marks. 

Not supported are (ä,ü,ö,symbols and commas). 

The result of the encryption or decryption is output at the end of the process.

#############################################################################################################################################

German

########

Programm zur Ver- und Entschlüsselung.


Bei der Ausführung des Programms wird der Nutzer aufgefordert zwischen "Verschlüsseln", "Entschlüsseln" und "Programm beenden" zu wählen.

Im Anschluss der gerade getroffenen Wahl, wird ein Shiftcode und eine zu ver- oder entschlüsselnde Eingabe verlangt. 

Die Eingabe des Nutzers wird in einer Liste (encrypted- oder decryptedtext) gespeichert. Dort wird abhängig von der Position der Buchstaben / Leerzeichen 
(ob gerade oder ungerade) in zwei Listen eingeteilt. Liste 1 (ungerade Positionen) wird dann beim Verschlüsseln um den Shiftfaktor verschoben. 
Liste 2 (gerade Positionen) wird beim Verschlüsseln um den Shiftfaktor zum Quadrat + 7 verschoben.

Sollte der Nutzer sich jedoch dazu entscheiden das Programm direkt zu beenden, so schließt dieses sich von selbst.

Beim Entschlüsseln werden die Listen gedreht und verschoben.

Als Eingabe sind alle Buchstaben in Groß- und Kleinschrift erlaubt, sowie Zahlen von 0-9 und . ! Leerzeichen Fragezeichen. 

Nicht unterstützt werden die Umlaute und das Komma. 

Das Ergebnis der Ver- oder Entschlüsselung wird im Anschluss des Prozesses ausgegeben.

##############################################################################################################################################

Quellen

########

Skript T3ELG10008.2 Informatik 1 Labor
Lehrbuch/Praxisbuch: Python 3 ISBN: 978-3-95845-791-1
        (Befehle wie reverse, .index,.join, break, try )
Pap-Designer (Grafischer Verlauf)