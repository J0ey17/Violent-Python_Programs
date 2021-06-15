#!/bin/python3
import crypt
import sys

try:
    fileName=sys.argv[2]
    passHash=sys.argv[1]

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
