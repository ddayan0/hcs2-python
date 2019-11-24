#Dennis Dayan
#DataStructuresProject.py
print('''

 .----------------. .----------------. .----------------. .----------------. .----------------. .-----------------.
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| | _____  _____ | | |      __      | | |  _________   | | |    _______   | | |     ____     | | | ____  _____  | |
| ||_   _||_   _|| | |     /  \     | | | |  _   _  |  | | |   /  ___  |  | | |   .'    `.   | | ||_   \|_   _| | |
| |  | | /\ | |  | | |    / /\ \    | | | |_/ | | \_|  | | |  |  (__ \_|  | | |  /  .--.  \  | | |  |   \ | |   | |
| |  | |/  \| |  | | |   / ____ \   | | |     | |      | | |   '.___`-.   | | |  | |    | |  | | |  | |\ \| |   | |
| |  |   /\   |  | | | _/ /    \ \_ | | |    _| |_     | | |  |`\____) |  | | |  \  `--'  /  | | | _| |_\   |_  | |
| |  |__/  \__|  | | ||____|  |____|| | |   |_____|    | | |  |_______.'  | | |   `.____.'   | | ||_____|\____| | |
| |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 .----------------. .----------------. .-----------------..----------------. .-----------------..----------------. .----------------. .----------------. .----------------. .----------------.
| .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. | .--------------. |
| |  _________   | | |     _____    | | | ____  _____  | | |      __      | | | ____  _____  | | |     ______   | | |     _____    | | |      __      | | |   _____      | | |    _______   | |
| | |_   ___  |  | | |    |_   _|   | | ||_   \|_   _| | | |     /  \     | | ||_   \|_   _| | | |   .' ___  |  | | |    |_   _|   | | |     /  \     | | |  |_   _|     | | |   /  ___  |  | |
| |   | |_  \_|  | | |      | |     | | |  |   \ | |   | | |    / /\ \    | | |  |   \ | |   | | |  / .'   \_|  | | |      | |     | | |    / /\ \    | | |    | |       | | |  |  (__ \_|  | |
| |   |  _|      | | |      | |     | | |  | |\ \| |   | | |   / ____ \   | | |  | |\ \| |   | | |  | |         | | |      | |     | | |   / ____ \   | | |    | |   _   | | |   '.___`-.   | |
| |  _| |_       | | |     _| |_    | | | _| |_\   |_  | | | _/ /    \ \_ | | | _| |_\   |_  | | |  \ `.___.'\  | | |     _| |_    | | | _/ /    \ \_ | | |   _| |__/ |  | | |  |`\____) |  | |
| | |_____|      | | |    |_____|   | | ||_____|\____| | | ||____|  |____|| | ||_____|\____| | | |   `._____.'  | | |    |_____|   | | ||____|  |____|| | |  |________|  | | |  |_______.'  | |
| |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | | |              | |
| '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' | '--------------' |
 '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------' '----------------'




''')

loggedIn = False #no idea what this does but it works i guess
curentUser="" #Current user is for multi-user functionality


users = { #Dictionary for valid users of the program
    1: {
        'userName': 'Dennis Dayan',
        'pin': 211246,
        'balance': 100
    },
    2: {
        'userName': 'Arielle Madeam',
        'pin': 211284,
        'balance': 100

    },
     3: {
        'userName': 'Brianna Sumner',
        'pin': 211200,
        'balance': 100

    },
    4: {
        'userName': 'Luke Chrampanis',
        'pin': 1234,
        'balance': 100

    },
    5: {
        'userName': 'Kanye West',
        'pin': 92618,
        'balance': 100

    },
    6: {
        'userName': 'Bread Junior',
        'pin': 2468,
        'balance': 100

    }
}
def logout(): #Logout function
    global curentUser #Calls current user
    print('Thank you for banking with Watson Financials  {}.'.format(curentUser['userName'])) #Prints message
    curentUser=""
    login() #Ah, the ol switcharoo. Logout calls Login. It works.

def withDraw(): #Withdraw function
    global curentUser #Calls current user
    amt = int(input('Enter the amount you are withdrawing: ')) #Sets user input to variable "amt"
    if (amt < curentUser['balance']): #Checking variable against current users balance
        curentUser['balance'] -= amt #Actually withdraws
        print('Your balance is now {} USD'.format(curentUser['balance'])) #Prints greeting and current balance after withdrawing
    else:
        print('Invalid amount selected')





def checkBal(): #Lets user check balance
    global curentUser #Calls current user logged in
    print("Your current balance is {} USD".format(curentUser['balance'])) #Prints users balance using .format

def deposit(): #Deposit functiom
    amt = int(input('Amount you are depositing: ')) #Sets user input to varible "amt"
    if (amt > 0 and amt < 1000): #Checks if amt is less than 0 and over 1000
        curentUser['balance'] += amt #Adds valid amt value
        print('Amount Deposited') #Alerts user
        print("You balance is now {} USD".format(curentUser['balance'])) #Prints current balance using .format
    else:
        print('INVALID DEPOSIT AMOUNT') #See amt check abovem will print if user input is invalid


def bankMenu(): #T H E   A B S O L U T E   U N I T. Main user interface component
    running = True
    while running:#While loop
        global curentUser #Calls currentUser into the function
        print('Welcome to Watson Financials, Please select an option.') #Prints L O V E L Y greeting
        print(''''
         1: Deposit
         2: Withdraw
         3: Check balance
         4: Exit
         5: Logout
         ''''')    #User options
        usinput = int(input('Enter your selection : '))
        if usinput == 1: #Chose deposit
            deposit()
        if usinput == 3: #Chose check balance
            checkBal()
        if usinput == 4: #Chose exit
            print('Thank you for choosing Watson Financials, Goodbye.')
            import sys  #imports sytem
            sys.exit(0) #pretty damn simple, exits with exit code 0.
        if usinput == 2: #Chose withdraw
            withDraw()
        if usinput < 1: #Checks for a valid input
            print('INVALID OPTION SELECTED')
        if usinput > 5: #^^^^^^^^^^^^^^^^^^^^^^
            print('INVALID OPTION SELECTED')
        if usinput == 5: #Chose logout
            logout()
            break



def login(): #Login function, lets user login
    pinnum = int(input('Enter your password : ')) #Sets user input to var "pinnum"
    global curentUser #Calls current user
    for i in users: #for...in... loop
        if users[i]['pin'] == pinnum: #Iterates and checks pinnum against user passwords in dictionary
            print('Welcome {}!'.format(users[i]['userName'])) #Welcomes user with .format
            curentUser = users[i] #Sets currentUser to logged in user
            bankMenu()#Starts the bank menu. This is where my program goes into a state of mind known as "sicko mode"
            break #Breaks out of the loop
        else:
            curentUser = users[i] #Checks password
            print('Checking.......') #Prints what the program is doing to the user for security and peace of mind for the user
            print('Program Will Exit If Invalid password Is Entered')#Notifies User
            if pinnum == str: #this is supposed to check if pinnum is a string, BUT IT DOESNT WORK!!!!!!!!!!!!
                print('Enter your password NUMBER!') #OHHHH MY GODDDD ITS 12:49 WHYYYYY




login() #Login function defined above

