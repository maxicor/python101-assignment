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
    "email":'shubhamkalanni21@gmail.com',
    'password':'shubham567',
    'balance':55540
    }
} 
def login_menu():
    print("press 1. for deposit")
    print("press 2. for withdrawl")
    print("press 3. for password change")
    print("press 4. for forget paaswrd")
    print("press 5. for exit")

def login():
    account_no=input()
    if account_no in database:
    	passw=input()
    	if passw == database[account_no]['password']:
    		print('welcome',database[account_no]['account_name'])
    		while true:
                login_menu()
                ch=int(input('enter the choice'))
                if(ch==1):
                     deposit=int(input())
                     database[account_no]['balance']+=deposit
                elif(ch==2): 
                	withdrawl=int(input())
                	database[account_no]['balance']-=withdrwal
                elif(ch==3):
                	update_pass = input()
                	database[account_no]['password'] = update_pass
                elif(ch==4):#forget passs
                    #verify your email addresss
                    verify_email = input()
                    if verfiy_email == database[account_no]['email']:
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
    while true:
        start_menu()
        choice=int(input())
        if(choice==1):
            login()
        elif(ch==2):
            account_no = input()
            account_name = input()
            age = int(input())
            email = input()
            passw = input()
            open_bal = int(input())
            database[account_no]={"account_name":account_name,"age":age,"email":email,"password":passw,"balance":open_bal}#crate a new dict in      
        elif(choice==3):
            break
        else:
            print('enter the valid key')
            login()
