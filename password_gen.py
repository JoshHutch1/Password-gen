import random 

#selections of charaters
chars = "abcdefghijklmnopqrstuvwxyxABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!£$%^&*()."


while 1:
    password_len = int(input("How long would you like your password to be : "))
    password_count = int(input("How many passwords would you like : "))

    #getting the amount of password that the user wants
    for x in range(0,password_count):
        password = ""
        #adding more charater to the password
        for x in range(0,password_len):
            password_char = random.choice(chars) # selecting random charater form char
            password = password + password_char
        print("here is your paswsword :", password)
