import random
import string

#s1=list(string.ascii_uppercase + string.ascii_lowercase +string.punctuation + string.digits)

upper = string.ascii_uppercase
lower = string.ascii_lowercase
symbol = string.punctuation
num = string.digits

all=list(upper+lower+symbol+num)

length=int(input("enter length : "))

password=[]

for i in range(length):
    password.append(random.choice(all))
    len(password)
    
if len(password)>=4:
    random.shuffle(password)
    print("".join(password))
else:
    print("only above 4 letter password is allowed")


#############################################################################


import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
symbol = string.punctuation
num = string.digits

l1= random.choice(lower)
u1= random.choice(upper)
n1= random.choice(num)
s1= random.choice(symbol)


all=list(l1+u1+n1+s1)


p=int(input("enter length : "))

password=[]

for i in range(p):
    password.append(random.choice(all))
    len(password)
    
if len(password)>=4:
    random.shuffle(password)
    print("".join(password))
else:
    print("only above 4 letter password is allowed")


































