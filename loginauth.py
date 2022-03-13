def register(): 
  import re
  print("\nWelcome to Registration")
  file1 = open("credential.txt","a")
  pat = "^[a-z0-9]+[@]\w+[.]\w{2,3}$"
  while True:
    email=input("Enter Email: ")
    if re.match(pat,email):
      break
    else:
      continue
  
  file3 = open("credential.txt", 'r')
  data_dict = {}
  for line in file3:
    e,p = line.strip().split(' ')
    data_dict[e.strip()] = p.strip()
  file3.close()
#  print(' text file to dictionary =\n ',data_dict)

  if email not in data_dict.keys(): 
   while True:  
       password = input("Enter your password: ")
       if (len(password)<5 or len(password)>16):
           print("Invalid..! Must be 6 to 16 Chars, RE-ENTER")
           continue
       elif not re.search("[a-z]",password):
           print("Invalid..! Must contain 1 of a-z, RE-ENTER ")
           continue
       elif not re.search("[0-9]",password):
           print("Invalid..! Must contain 1 of 0-9, RE-ENTER")
           continue
       elif not re.search("[A-Z]",password):
           print("Invalid..! Must contain 1 of A-Z, RE-ENTER")
           continue
       elif not re.search("['!#$%&()*+,-./:;<=>?@[\]^_`{|}~]",password):
           print("Invalid..! Must be one special char, RE-ENTER")
           continue
       elif re.search("\s",password):
           print("Invalid..! Must be string, RE-ENTER")
           continue
       else:
           break
   file1 = open("credential.txt","a")
   file1.write(email+" "+password+"\n")
   print("Registration Successful")
   file1.close()
  else:
   print("User exits already, try to use login page")
   login()


def login():
  print("\nWelcome to login screen")
  email=input ("Enter Email: ")
  file3 = open("credential.txt", 'r')
  data_dict = {}
  for line in file3:
    e,p = line.strip().split(' ')
    data_dict[e.strip()] = p.strip()
  file3.close()
  if email in data_dict.keys():
    email1 = email
    password = input("Enter your password: ")
    pass1 = data_dict.get(email1)
    if password == pass1:
        print("Login successful")
    else:
        print("Invalid Password, Use forgot option to retrive")
  else:
    print("Email ID not registered, please register now")
    register()


def forget():
  print("\nWelcome to Forget screen")
  email=input ("Enter Email: ")
  file3 = open("credential.txt", 'r')
  data_dict = {}
  for line in file3:
    e,p = line.strip().split(' ')
    data_dict[e.strip()] = p.strip()
  file3.close()
  if email in data_dict.keys():
    email1 = email
    pass1 = data_dict.get(email1)
    print("Password is", pass1 )
  else:
    print("Email ID not registered, please register now")  

print("Welcome User. Enter")
print("1 for Register \n2 for Login \n3 for Forget \n4 for END  ")

def main(): 
  n = int(input("\nEnter choice(1/2/3/4): "))
  if n in range(1,5):
    if n == 1:
      register()
      main()
    elif n == 2:
      login()
      main()
    elif n == 3:
      forget()
      main()
    elif n == 4:
      end()
  else:
    print("Invalid Entered, Accepted only 1,2,3,4")
    main()

def end():
  print("Ended Successfully")
  
main()
