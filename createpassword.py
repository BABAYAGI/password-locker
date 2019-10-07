import random 
s = "QWERTYUIOPLKJHGFDSAZXCVBNM,.;'[]=-qwertyuioplkjhgfdsazxcvbnm,.;']*-1234567890!@##$%^&*()_+"
len_password = int(input("enter number of characters in password :")
)
password = "".join(random.sample(s ,len_password))
print(password)

answer = input("would you like to keep this password :")
if("yes" in answer):
    account_name = input("enter account name:")
    
  else:
    print
