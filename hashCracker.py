"""
The script below follows an approach close to the one described above;
Asks for the location of a wordlist
Asks for the hash to be cracked
Reads values from the wordlist (one per line)
Converts cleartext values to SHA256 hash values
Compares the generated SHA256 hash value with the value entered by the user
"""

"""
As you probably know, hash values can not be cracked as they do not contain the cleartext value. Unlike encrypted values that can be "reversed" (e.g. decrypted), cleartext values for hashes can only be found starting with a list of potential cleartext values. A simplified process can be seen below;

You retrieve the hash value "eccbc87e4b5ce2fe28308fd9f2a7baf3" from a database, which you suspect is the hash for a number between 1 and 5.
You create a file with possible cleartext values (numbers from 1 to 5)
You generate a list of hashes for values in the cleartext list (Hash values for numbers between 1 and 5)
You compare the generated hash with the hash value at hand (Matches hash value of the number 3)
"""

#Imports
import hashlib
import pyfiglet

#ASCII Banner
ascii_banner = pyfiglet.figlet_format("HASH CRACKER for SHA256", font='doom')
print(ascii_banner)

#User Input
word_list = str(input("Can you please enter the wordlist location: "))
input_hash = str(input('Enter the hash value to be cracked: '))

#Reading the Wordlist and Hashing
with open(word_list, 'r') as file:
    for line in file.readlines():
        hash_ob = hashlib.sha256(line.strip().encode())
        hashed_pass = hash_ob.hexdigest() #Computes the hexadecimal representation of the SHA-256 hash.
        if hashed_pass == input_hash: #Compares the computed hash with the input hash.
            print("Found the cleartext password! " + line.strip())
            exit(0)


