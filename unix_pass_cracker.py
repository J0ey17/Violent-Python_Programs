#This is a simple Unix password Cracker, uses Crypt module of python.
#Takes 2 command line arguments. The hash we want to crack, and the wordlist.
#USAGE:
#python3 unix_pass_cracker.py HX9LLTdc/jiDE wordlist.txt

#!/bin/python3
import crypt
import sys

try:
    fileName=sys.argv[2]    #wordlist file
    passHash=sys.argv[1]    #Hash 4 Crack

    salt=passHash[0:2]
    print("Salt: "+salt)
    
    f=open(fileName,'r')
    
    for line in f.readlines():
        line=line.strip('\n')
        newHash=crypt.crypt(line,salt)
        print ("Trying: " +line+ "||  corresponding hash: "+newHash+ "||  Loaded Hash: "+passHash)

        if newHash==passHash:
            print ("Match found, password is : "+line)
            break
        else:
            continue
    f.close()

except Exception as e:
    print ("Error: "+str(e))
