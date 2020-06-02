import random, sys
    
    print('ROCK-PAPER-SCISSORS')
    win = 0
    loss = 0
    draws = 0


    while True: #the main code of the entire game
        
        while True: #Gets the required user output
            print('Please enter (r)ock, (p)aper, or (s)cissor or (q)uit to play')
            
            userInput = input()
            
            if userInput == 'q':
                sys.exit()
            elif userInput == 'r' or userInput == 'p' or userInput = 's':
                print('User entered ' + userInput + '...')
                break
        

        # getting the required random number
        randomInput = random.randint(1,3)
        
        if randomInput == 1:
            computerInput = 'r'
            print('Computer chose Rock')
        elif randomInput == 2:
           computerInput = 'p'
           print('Computer chose Paper')
        elif randomInput == 3:
           computerInput = 's'
           print('Computer chose Scissors')
        

        print('                            ')

        if computerInput == userInput:
            print('it is a tie')
            draws = draws + 1
        elif computerInput == 'r' and userInput == 'p':  
            print('Paper beats rock so User wins')
            win = win + 1            
        elif computerInput == 'p' and userInput == 'r':
            print('Paper beats rock so Computer wins')
            loss = loss + 1    
        elif computerInput == 'r' and userInput == 's':
            print('Rock beats Scissors so Computer wins')
            loss = loss + 1
        elif computerInput == 's' and userInput == 'r':
            print('Rock beats Scissors so User wins')
            win = win + 1
        elif computerInput == 's' and userInput == 'p':
            print('scissors beat paper so Computer wins')
            loss = loss + 1
        elif computerInput == 'p' and userInput == 's':
            print('scissors beat paper so User wins')
            win = win + 1
            
        

                

        print('                            ')
        print('                            ')
        print('                            ')
        print('                            ')
        print('                            ')
                
        
        
    print('The game has ended')
    
    if win > loss:
        print('You won')
    elif loss > win:
        print('You lost')
    else:
        print('You drew')    
    
    print('You had %s wins, %s losses, %s draws' % (win, loss, draws))
    
    
    
    
    











