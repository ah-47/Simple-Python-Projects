import random
import zxcvbn

mylist = list('1Aa!2Bb@3Cc#4Dd$5Ee?6Gg^7Hh&8Ii*9Jj0Kk11Ll2Mm3Nn4Oo5Pp6Qq7Rr18Ss9Tt9Uu8Vv7Ww6Xx5Yy4Zz')

def password_generator(num):
            
    rp = random.sample(mylist, num)

    random_password = "".join(rp) # The join() method is a very efficient way to convert a list of strings back into a single string in Python.

    return random_password

def time_scale(years_to_crack):

    if years_to_crack >= 10**15:
        return "More than a quadrillion years (extremely secure)"
    
    elif years_to_crack >= 10**12:
        return "More than a trillion years (extremely secure)"
    
    elif years_to_crack >= 10**9:
        return "More than a billion years (very secure)"
    
    elif years_to_crack >= 10**6:
        return "More than a million years (quite secure)"
    
    else:
        return f"{years_to_crack:.2f} years"

def password():

        while True:
            
            choice = int(input('Press 1 for usage and press any key to exit: '))

            if choice == 1:

                num = int(input("How many characters do you want to in your password: "))
                
                random_password = password_generator(num)

                print("Generated password is: ", random_password)

                result = zxcvbn.zxcvbn(random_password)

                # print(result)

                guesses = result['guesses']
                
                guesses_per_second = 1000000000 # 1 billion guesses  
                
                seconds_to_crack = guesses / guesses_per_second
                
                years_to_crack = seconds_to_crack / 60 / 60 / 24 / 365

                print("Time to crack the password: ")

                print(time_scale(years_to_crack))
            
            else:
                print('Thanks for using our services')
                
                break
password()