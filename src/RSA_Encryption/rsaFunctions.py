import sys
from random import choice, randint
from math import *

sys.set_int_max_str_digits(100000) # Increases string limit to allow for more data

def calculate_RSA(p, q): # Calculates the e, d, n and phi n values for rsa
    n = p * q # Calculates n
    phin = (p - 1) * (q - 1) # Calculates phi n
    
    e = calculate_e(n, phin) # Calls the function to calculate e
    d = calculate_d(phin, e) # Calls the function to calculate d
    
    return {"e" : e, "d" : d, "n" : n}

def calculate_e(n, phin): # Calculates the e value
    coprimes = []
    
    for i in range(phin - 2): # Loops through every value greater than 1 but less than phi n
        if gcd((i + 2), phin) == 1: # Checks if the value is coprime with phi n and n
            if gcd((i + 2), n) == 1:
                coprimes.append(i + 2) # Adds the value to the list
    e = choice(coprimes) # Chooses a random value from the list and sets e to it
    return e
    
def calculate_d(phin, e): # Calculate the d value
    for i in range(phin * 9): # Loops through numbers that ehn multiplied by e and modded by phi n gives 1
        if (i * e) % phin == 1 and i != e:
            if randint(1, 100) > 50:
                d = i  # Sets the value of d
                break
    return d

def encrypt_RSA(message, e, n): # Encrypts using RSA
    encrypted = numify(message) # Converts the message into ASCII
    for i in range(len(encrypted)):
        encrypted[i] = (encrypted[i] ** e) % n # Raises each character of the message to e and modulo n 
    
    return encrypted
 
def decrypt_RSA(message, d, n): # Decrypts using RSA
    for i in range(len(message)):
        message[i] = (int(message[i]) ** d) % n # Raises each character of the message to d and modulo n
        
    decrypted = charify(message) # Converts ASCII back into characters
    
    return decrypted
   
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
