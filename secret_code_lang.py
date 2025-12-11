'''
Write a python program to translate a message into a secret code language. Use the rules below to translate normal English into secret code language

Coding:
If the word contains atleast 3 chars, remove the first letter and append it at the end. Now append three random chars at the starting and the end
else simply reverse the string

Decoding:
If the word contains less than 3 characters, reverse it
else remove 3 random chars from start and end. Now remove the last letter abd append it to the beginning

Program should ask whether you wanna code or decode

'''

#Function to generate random 3 length string
import random;
def generate_random():
    st="abcdefghijklmnopqrstuvwxyz"
    random_string = ""
    for i in range(0,3):
        random_string+=random.choice(st)
    return random_string

# Function for Code
def code_func(i):
    val=str(i)
    li=val.split(" ")
    v=""


    print("You have selected to code the string in secret language")
    for j in li:
        if(len(j)<3):
            v= " "+v+" "+j[::-1]
        else:
            x=j.removesuffix(j[1:len(j)])
            pre=generate_random()
            suf=generate_random()
            final=pre+j[1:len(j)]+x+suf
            v = " "+v+" "+ final
    print("Your encoded string is: ",v)    


#Function for Decode
def decode_func(i):
    print("You have selected to decode the string")
    val=str(i)
    li=val.split(" ")
    v=""
    for j in li:
        if(len(j)<3):
            v= " "+v+" "+j[::-1]
        else:
            x=j[3:len(j)-3]
            z=x[-1]
            y=x.removesuffix(x[-1])
            final=z+y
            v = " "+v+" "+ final
    print("Your encoded string is: ",v)



code_decode=input("Do you wanna code(c) or decode(d)?")

if code_decode == "c":
    inp=input(f"Please enter a string or sentence to code: ")
    code_func(inp)
elif code_decode == "d":
    inp=input(f"Please enter a string or sentence to decode: ")
    decode_func(inp)
else:
    print("Please enter valid option c for code, d for decode")

