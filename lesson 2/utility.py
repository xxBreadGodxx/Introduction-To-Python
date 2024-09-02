
# The '#region <description of the snippet>' is a neat parler trick for organizing your code in snippets.
# Once you have decided where the region of the code will end you can put '#endregion', you will then be able to close
## an entire cod block instead of just minimizing methods by themselves.

#region Custom Methods (Beautify)

# We define the method as usual but instead we assign an empty variable in the method parameters
# Doing this will let us put any value we want in the method paramater in this case we're using a string
def WriteLine(string):
    # Doing an empty print will allow us to have space between print lines so it isnt cluttered together in console.
    print('')
    # We use the regular print method and combine it with the string we want to use when called in other methods.
    # It will essentially look like this in the console [Debug]-> Hello!
    # We call this in other method like this so we can can save ourselves some time writing what is debug and what isnt.
    # WriteLine('Hello!') ## We are assiging the empty variable, "string", to 'Hello!'.
    print('[Debug]-> '+string)
#endregion

#region Main Operations
def Addition():
    # Here's where the fun begins....
    # The 'try except' statement in a method allows us to catch any potential errors like an 'if else' statement would.
    # We can get more precise error catching/handling with the 'try except' statement in this case "ValueError".
    # ValueError will allow us to catch if the user, in this case, inputs a non whole number, i.e: 2.5.
    # In short we 'try' to do something and if it doesnt work we throw it to 'except'.
    # All whole numbers will pass through properly and all decimal non whole numbers will be caught as an error.
    try:
        print('')
        # num1 will be our variable 
        # Instead of just allowing the user to type on the next line we are allowing the user to type on the same line the question
        ## was asked on
        # In this case we want to capture an integer or rather a numerical value (a number), so we encapsulate the question with int()
        # This allows it to only capture the string as an int so we do math with the user input.
        # So if you only want the user to input a number you would say 'int(input('Enter a number: '))' if you want the user to only input a string
        ## you'd put 'input('Enter Your Name: ')', if you would like the user to only input decimal values you'd put 'float(input(Enter A Decimal: ))'.
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        # Doing any type of calculation you will need to use a basic print() method to do so. Since we didn't define extra
        ## variables in the WriteLine() method except a string, it wont work.
        # Putting variables in a print line is easy, just write what you want in quotes and add a comma to make it display a variable
        # In this case we want to do addition to both of the variables and have the console print it so we will take num1 and num2 and put
        ## a plus symbol between them, i.e: print('The Sum Is: ', num1+num2)
        print('The answer is: ', num1+num2)
    except ValueError:
        print('Please only use whole numbers.')
        Addition()


def Subtraction():
    try:
        print('')
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        print('The answer is: ', num1-num2)
    except ValueError:
        print('Please only use whole numbers.')
        Addition()

def Multiplication():
    try:
        print('')
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        print('The answer is: ', num1*num2)
    except ValueError:
        print('Please only use whole numbers.')
        Addition()

def Division():
    try:
        print('')
        num1 = int(input('Enter the first number: '))
        num2 = int(input('Enter the second number: '))
        print('The answer is: ', num1/num2)
    except ValueError:
        print('Please only use whole numbers.')
        Addition()
#endregion

#region Options
def Options():
    print('')
    print('[1]: Addition [2]: Subtraction [3]: Multiplication [4]: Division')
    optionPick = input('Please Choose An Operation: ')

    if optionPick == '1':
        Addition()
        Options()
    # 'elif' statement allows us to further continue the if statement, just think of it as another 'if' value.
    # We can use the 'elif' value as much as we want but it is very unoptimized if unchecked, so try and keep it short and sweet if possible.
    elif optionPick == '2':
        Subtraction()
        Options()
    elif optionPick == '3':
        Multiplication()
        Options()
    elif optionPick == '4':
        Division()
        Options()
    # The 'elif' value will not count as an 'else' value. You need to end the 'if' always with an 'else' or it will not work.
    else:
        WriteLine('That is not a valid option, please try again.')
        Options()
#endregion

#region User Login
def Password():
    passString = input('Enter Password: ')
    if passString == 'password':
        # As said earlier this is how we call/use our custom print statement when we want to send a "debug" message to the console.
        # The word "debug" does not represent anything, in this case it's just what I'm using the custom print statement for.
        # You can make as many or use as many custom print statements as you like, they can either have purpose or no purpose at all.
        WriteLine('Logged In Successfully')

def Login():
    print('')
    userString = input('Enter Username: ')
    if userString == 'admin':
        print('')
        Password()
        WriteLine('Welcome Back '+userString+'!')
        Options()
        
    else:
        WriteLine('No user was found with the user: "'+userString+'" Try again.')
        Login()
#endregion

# Program Startup
Login()