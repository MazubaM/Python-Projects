import random
from secrets import choice
import string

#character set for random password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def gen_random_pass():
    #ask user to enter length
    length = int(input("Enter password length: "))
    
    #shuffle characters
    random.shuffle(characters)
    
    randompass = []
    for i in range(length): 
        randompass.append(random.choice(characters))
    
    #shuffle the created password
    random.shuffle(randompass)
    
    #convert the password from list to string 
    print("".join(randompass))
    
#call the function gen_random_pass
gen_random_pass()
    