listo = {'monday':[],
        'tuesday':[],
        'wednesday':[],
        'thursday':[],
        'friday':[],
        'saturday':[],
        'sunday':[]}
repeat = True

def helpList ():
    print('\nTotal list of commands:')
    print('get - retrieves to-do list for one day')
    print('add - add an entry to a day')
    print('quit - quit the program')
    print('!help - get a list of all commands')

def getList ():
    print('\nWhat day?')
    day = input('> ').lower()
    if day in listo:
        print(listo[day])
    else:
        print('\nInvalid Day.')
        getList()

def addList():
    print('\nWhat day?')
    day = input('> ').lower()
    if day in listo:
        print('\nWhat would you like to add?')
        entry = input('> ')
        listo[day].append(entry)
    else:
        print('\nInvalid Day.')
        addList()

def quitList():
    global repeat
    repeat = False
    print('\nQuitting program...')
    print('Thank you for using To-Do.py™ for all your to-do needs!')
    
def toDo ():
    global repeat
    while repeat != False:
        try:
            print("\nPrompt: What would you like to do?")
            userAct = input("> ").lower()
            
            if userAct == '!help':
                helpList()
            
            elif userAct == 'get':
                getList()
                    
            elif userAct == 'add':
                addList()
            
            elif userAct == 'quit':
                quitList()
            
            else:
                print('\nInvalid Entry. Please enter !help for a list of all valid commands.')
        
        except:
            print('SMTH went wrong. IDK what...')
toDo()