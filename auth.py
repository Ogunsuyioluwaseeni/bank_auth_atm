# register
#--first name,last name,password, email
#--generation user id

#login
#- account number and password

#bank operations

#initializing the system

import random


database={} #dictionary

def init():
    
    print("Welcome to RSE Bank")
    
    haveAccount =int(input("Do you have account with us: 1(Yes) 2(No)\n"))
        
    if(haveAccount==1):
        login()
            
    elif(haveAccount==2):
           
        print(register())   
             
    else:
        print("You have seleceted invalid 0ptions")
        init()

def login():
    print ("*******Login*******")
    accountNumberFromUser=int(input("What is your account number?\n"))
    password=input("What is your Password\n")
        
    for accountNumber,userDetails in database.items():
        if (accountNumber==accountNumberFromUser):
            if(userDetails[3]==password):
                bankOperation(userDetails)
                    
    print('Invalid account or password')
    login()
    
    
def register():
    print("******Register******")
    
    email=input("What is your Email Address?:\n")
    first_name= input("What is your First Name?:\n ")
    last_name= input("What is your Last Name?:\n")
    password= input("Create a password for yourself\n")
    
    accountnumber= generateAccountNumber()
    
    database[accountnumber]=[ first_name, last_name, email, password]
    
    print("Your Account has been created")
    print("======= ===== ==== ==== === ===")
    print("Your account Number is: %d" % accountnumber)
    print("Make sure you keep it safe")
    print("====== ===== ==== ===== ====== =")
    
    login()
    
    
def bankOperation(user):
    print("Welcome %s %s" %(user[0], user[1]))
    
    
    selectedOption = int(input("What do you like to do? (1) for deposit (2) for withdrawal (3) for Logout  (4) for exit\n"))
    
    if(selectedOption == 1):
        
        depositOperation()
    elif(selectedOption == 2):
        
        withdrawalOperation() 
    elif(selectedOption == 3):
    
        logout()  
    elif(selectedOption == 4):
        
        exit()     
    else:
        
        print("invalid Option selected") 
        bankOperation(user)
        
def withdrawalOperation():
        print("Withdrawal")
        
        
def depositOperation():
        print("Deposit Operation")
        
        
def generateAccountNumber():
   return random.randrange(1111111111,9999999999)

def logout():
    login()


##### Actual Banking System

init()
