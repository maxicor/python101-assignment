database = {
"siddharth":{
    "account_name": 'siddharth shevde',
    "age":20,
    "email":'siddharthshevde22@gmail.com',
    'password':'sid123',
    'balance':2342
},
"sohil":
    {
    "account_name": 'sohil jain',
    "age":21,
    "email":'sohiljain69@gmail.com',
    'password':'sohil69',
    'balance':6969
    },
    "sonika":{
    "account_name": 'sonika mallick',
    "age":20,
    "email":'sonikamallick1998@gmail.com',
    'password':'sonika09',
    'balance':10000
},
"shubham":
    {
    "account_name": 'shubham kalani',
    "age":21,
    "email":'shubhamkalani21@gmail.com',
    'password':'shubham567',
    'balance':55540
    }
} 
def login_menu():
    print("press 0. balance check")
    print("press 1. for deposit")
    print("press 2. for withdrawl")
    print("press 3. for password change")
    print("press 4. for forget paaswrd")
    print("press 5. for exit")

def login():
    account_no=input('Enter account number ')
    if account_no in database:
        passw=input("Enter password ")
        if passw == database[account_no]['password']:
            print('welcome',database[account_no]['account_name'])
            while True:
                login_menu()
                ch=int(input('enter the choice'))
                if (ch == 0):
                    print(database[account_no]['balance'])
                elif(ch==1):
                    deposit=int(input("Enter deposit ammount"))
                    database[account_no]['balance']+=deposit
                elif(ch==2): 
                    withdrawl=int(input("Enter withdrawl ammount"))
                    database[account_no]['balance']-=withdrawl
                elif(ch==3):
                    update_pass = input("Enter new password")
                    database[account_no]['password'] = update_pass
                elif(ch==4):
                    verify_email = input("Enter verifying email")
                    if verify_email == database[account_no]['email']:
                        forget_pass = input('new pass')
                        database[account_no]['password'] = forget_pass
                elif(ch==5):
                        break
                else:
                    print("enter the valid key")
                    login_menu()
            
    else:
        print('not valid')

def start_menu():
    print('1. for login')
    print('2. sign up')
    print('3. exit')

def menu():
    while True:
        start_menu()
        choice=int(input())
        if(choice==1):
            login()
        elif(choice==2):
            account_no = input("Enter Account number")
            account_name = input("Enter Account name")
            age = int(input("Enter Age"))
            email = input("Enter email")
            passw = input("Enter password")
            open_bal = int(input("Enter opening balance"))
            database[account_no]={"account_name":account_name,"age":age,"email":email,"password":passw,"balance":open_bal}  
        elif(choice==3):
            return 
        else:
            print('enter the valid key')
    


menu()
