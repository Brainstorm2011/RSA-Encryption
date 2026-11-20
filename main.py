import sys
from random import choice, randint
from math import *
from time import sleep

sys.set_int_max_str_digits(100000) # Increases string limit to allow for more data

def calculate_RSA(): # Calculates the e, d, n and phi n values for rsa
    global p, q, e, d, n, phin
    isprime = False
    
    f = open("pns.txt", 'r')
    primes = f.read().splitlines()
    f.close()
    
    while isprime == False:
        p = int(input("Enter a prime number(Greater than 11) ")) # Asks for first prime - p
        if str(p) in primes and p > 11: # Makes sure the prime number is a prime number
            isprime = True
        else:
            print("Not a prime/Under 11")
    
    isprime = False
           
    while isprime == False:
        q = int(input("Enter another prime number(Greater than 13) ")) # Asks for second prime - q
        if q != p and str(q) in primes and q > 13: # Makes sure the rpime number is a prime number
            isprime = True
        else:
            print("Not prime/Under 13/Isn't a different prime")
    
    n = p * q # Calculates n
    sleep(0.5)
    print("'n' Calculated")
    phin = (p - 1) * (q - 1) # Calculates phi n
    
    calculate_e() # Calls the function to calculate e
    sleep(0.5)
    print("'e' Calculated")
    calculate_d() # Calls the function to calculate d
    sleep(0.5)
    print("'d' Calculated")
    
    sleep(1)
    print("RSA values calculated") # Gives the user the e, d and n values
    print(f"Your n value is {n}")
    print(f"Your e value is {e}")
    print(f"Your d value is {d}")
    print("Please keep these values saved")
    print("You can share your e and n value")
    print("Don't share your d value")

def calculate_e(): # Calculates the e value
    global p, q, e, d, n, phin
    coprimes = []
    
    for i in range(phin - 2): # Loops through every value greater than 1 but less than phi n
        if gcd((i + 2), phin) == 1: # Checks if the value is coprime with phi n and n
            if gcd((i + 2), n) == 1:
                coprimes.append(i + 2) # Adds the value to the list
    e = choice(coprimes) # Chooses a random value from the list and sets e to it
    
def calculate_d(): # Calculate the d value
    global p, q, e, d, n, phin
    
    for i in range(phin * 9): # Loops through numbers that ehn multiplied by e and modded by phi n gives 1
        if (i * e) % phin == 1 and i != e:
            if randint(1, 100) > 50:
                d = i  # Sets the value of d
                break

def encrypt_RSA(): # Encrypts using RSA
    e = int(input("Please enter your e value ")) # Asks for the e value
    n = int(input("Please enter your n value ")) # Asks for the n value
    
    message = input("Please enter the message you would like to encrypt ")
    print("ASCII message in progress...")
    sleep(0.5)
    encrypted = numify(message) # Converts the message into ASCII
    print("ASCII message complete")
    sleep(0.5)
    print("Encrypting in progress...")
    sleep(0.5)
    for i in range(len(encrypted)):
        encrypted[i] = (encrypted[i] ** e) % n # Raises each character of the message to e and modulo n 
    print("Encrypting Complete")
    sleep(0.5)
    print(*encrypted)
    print("Please copy the encrypted numbers, without modifying them")
 
def decrypt_RSA(): # Decrypts using RSA
    d = int(input("Please enter your d value ")) # Asks for the d value
    n = int(input("Please enter your n value ")) # Asks for the n value
    
    message = input("Please enter the list of numbers you would like to decrypt ")
    nums = message.split(" ")
    print("Decryption in progress...")
    sleep(0.5)
    for i in range(len(nums)):
        nums[i] = (int(nums[i]) ** d) % n # Raises each character of the message to d and modulo n
        
    print("Decrypted message complete")
    sleep(0.5)
    print("Charactered message in progress...")
    decrypted = charify(nums) # Converts ASCII back into characters
    print("Charactered message complete")
    sleep(0.5)
    print(decrypted) 
   
def numify(message):
    num = []
    for i in range(len(message)):
        num.append(ord(message[i])) # Converts the character into ASCII
    
    return num

def charify(num):
    char = ''
    for i in range(len(num)):
        char += chr(num[i]) # Converts ASCII back into characters
        
    return char

def convertList(m): # Converts the string into a list
    l = []
    for i in range(len(m)):
        l.append(m[i])
        
    return l
    
def convertString(l):
    string = ''
    for i in range(len(l)):
        string += l[i]
    
    return string