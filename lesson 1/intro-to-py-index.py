##print('Hello World!')##

##Hey console, i need you to say something for me

##ok what do u need me to say? put it in these ('')

##print('FUCK YOU')##

# v = input() #

# v is the variable, in this case the variable is a string i.e user input and or a constant in the code

# the method input() is how we grab the users input in the terminal

# in this case we are setting the variable string v to whatever the user types and hits enter on in the terminal

# once the user hits enter on the required user input() it will then set the v variable string to whatever the user typed

##if v == 'fuck you':
    #print('Fuck you too then..')
##else:
    #print('What was that?') 

# the if else statement will check if the string is a certain keyphrase and if it is, it will pass to the print statement "Fuck you too then"
# anything that isnt the keyphrase will pass to the else print statement

##Start() - this will not work up here because it hasnt been defined "yet"

def Option2():
    z = input()
    if z == 'leave':
        print('you leave the fucking town')
    elif z == 'go home':
        print('you went home')
    else:
        print("I didn't catch that")
        Option2()

def Start():
    # Start the program with a prompt, in this case a question to the user.
    print('What do you do?')
    v = input()
    if v == 'select key':
        print('You selected the key of hearts')
        print('')
        print('What will you do now')
        Option2()
            
        # calling the method inside of itself will cause it to loop, this case we want it to happen so we can contiously grab user input data
        Start()
    else:
        print('What was that?')
        Start()

# think of this like reading, you read top to bottom, so does the computer when programming in python
# when defining a function/code block/method you have to define it first before placing the function as seen above

Start()
