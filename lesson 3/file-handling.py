# Importing allows us to use certain libraries or packages we have installed with python
# We can install custom stuff to do certain things but in this case we import os (operating system)
## so that we can have our program access directories on our local machine.

# The 'os' import is used with alotttttttttttttttttttttt of my bullshit that I do in python; so might as well do this
## for your next lesson.
import os

# With this method we are going to be looking for the folder path and creating a file in that folder path.
# Later on we will use these set method variables to allow the user to set a custom path and give a custom name.

# Also from now on, I will be calling them method variables in the lessons. For example 'def Method(variable1, variable2)' the variables in the
## parentheses will be called method variables in the lessons from here on out.

# The content variable will be what the user wants to store inside of the file
def createFile(folder_path, file_name, content):
    print('')
    # We will first see if the user has given us a usables folder path/making sure it exists.
    # The 'if not' statement will help us check for a false value instead of a true value like a default 'if' statement does.
    # 'os.path' essentially mean 'operating_system directory_path'
    # First we call the 'os' package then we add a dot allowing us to call methods inside of that package.
    # The 'path' method is only accessible inside of the 'os' package.
    # We then call a definition inside of the 'path' method to check to see if the directoy exists, funny enough this definition is called 'exists';
    ## the '.exists' is going to be your bestfriend so you can save yourself from a fuckton of errors when it comes to directory checking/making.

    # Finally we give the user designated folder path to check to see if it exists or not as seen below.
    if not os.path.exists(folder_path):
        # If the path that the user gave us does not exist we will make it for them.
        os.makedirs(folder_path)

    # Next we will, in a way, construct/make the full directory including the file name
    # This means that it will lead all the way to, in this case, a txt file, instead of just the directory.
    # If that's too weird to comprehend, think of it like this 'C:\Users\eldri\OneDrive\Desktop\Coding Shit\test.txt'
    # We combine the folder path with the file name we are making if not already made then we are finding it.

    # The 'os.path.join(directory, file_name)' essentially just makes it look like this C:\Users\eldri\OneDrive\Desktop\Coding Shit\test.txt
    ## instead of this 'C:\Users\eldri\OneDrive\Desktop\Coding Shit,   test.txt'
    # So the join method is exactly as it sounds, it joins two variables to make a whole one.
    file_path = os.path.join(folder_path, file_name)

    # This will open the file in that joint file path name and it will open it in 'write mode' also the 'w' you see in the statement.
    # There are many different variables you could use to open a file with you can also only read a file and not write to it, that would be 'r' instead of 'w'.
    with open(file_path, 'w') as file:
        # We will write whatever the user input for the content variable inside of the file using the method 'file.write', the method 'file' comes from the
        ## import os as well as the definition inside of it called 'write'. The 'file' method has a few definitions inside of it. 
        ### We can write, read, delete as far as my knowledge, feel free to experiment with it.
        file.write(content)
    # You maybe asking "Why the fuck is there a random 'f' in the print statment?" Well that f there allows us to put our variables inside of the print statement,
    ## instead of outside of it like this print('Hello! ', username).
    # You'll also need to add those squiggle brackets in quotes in order to make the variable called inside of the print along with the f at the beggining outside
    ## of the print string.
    print(f"File '{file_name}' created in the folder path: '{folder_path}'" )

def deleteFile(file_path):
    print('')
    if os.path.exists(file_path):
        # Using the 'os.remove(file path)' will delete any file that is in the specified directory
        # In this case we are allowing the user to delete the file they created if they desired. They would just need to input the directory path to the file
        ## like this 'C:\Users\eldri\OneDrive\Desktop\Coding Shit\test.txt'
        os.remove(file_path)
        print('File ', file_path,' has been deleted.')
    else:
        print('The designated file path does not exist.')

def Start():
    print('')
    print('[1]: Create A File [2]: Delete A File')
    optionPick = input('Please Choose An Operation: ')
    if optionPick == '1':
        folder_path = input('Please Input The Folder Path: ')
        # 'With Extension' means we're asking the user what type of file are we making, in this case the provided code will only work with a '.txt' extension
        file_name = input('Please Input The File Name With Extension: ')
        content = input('Please input what you would like the contain: ')
        # We make three new method variables so that we can then store them into the createFile defintion as mentioned above earlier.
        createFile(folder_path, file_name, content)
        # Might as well have it loop so we can just keep it open instead of re running the debug launcher each time we want to make a file
        # Or make it to where the user is able to make multiple text files so we loop it.
        Start()
    elif optionPick == '2':
        print('')
        file_path = input('Please Input The File Path: ')
        deleteFile(file_path)
        Start()
    else:
        print('')
        print('Not a valit operation')
        Start()


# Program Start
Start()