#Chopsticks TP for 15-110 
#Phil Huang. Jerry Li
#ID:xiangheh, jerryl
#Commends: we choose not to use a 2d-list representation so this code might be
#cancerous to code trace. Have Fun!
#-------------------------------------------------------------------------------
#=====================================change player=============================
import random
def getStartingPlayer():
    #very first function
    while True:
        player = input('Who starts, [U]ser or [C]omputer? ---> ')
        if ((player == 'U') or (player == 'C')):
            return player
        else:
            print('That is not a legal response. Please enter a single uppercase letter.')
            print('---------------------------------------------------------------------')

def getOtherPlayer(player):
    #switch player
    if (player == 'C'):
        return 'U'
    else:
        return 'C'
        
def setComputerDifficulty():
    #sets computer difficulty
    while True:
        difficulty = input('What difficulty do you wish to set? [H]ard or [N]ormal? ---> ')
        if ((difficulty == 'H') or (difficulty == 'N')):
            return difficulty
        else:
            print('That is not a legal response. Please enter a single uppercase letter.')
            print('---------------------------------------------------------------------')

#===============================get COMPUTER's moves and results================

def getComputerMove(computerLeft, computerRight):
    if(computerLeft==0):
        addingHand='R'
    elif(computerRight==0):
        addingHand='L'
    else:
        addingHand=random.choice(['L', 'R']) #add from a random hand
    targetHand=random.choice(['L', 'R']) # add TO the PLAYER'S random hand
    print('---------------------------------------------------------------------')
    return [addingHand, targetHand]
    
def getResultsOfComputerMove(addingHand, targetHand, computerLeft, computerRight, userLeft, userRight):
    #add from C's hand to P's target hand
    if(addingHand=='L' and targetHand=='L'):
        userLeft += computerLeft
        addedInteger=computerLeft
    elif(addingHand=='L' and targetHand=='R'):
        userRight += computerLeft
        addedInteger=computerLeft
    elif(addingHand=='R' and targetHand=='L'):
        userLeft += computerRight
        addedInteger=computerRight
    elif(addingHand=='R' and targetHand=='R'):
        userRight += computerRight
        addedInteger=computerRight
    return [addedInteger, userLeft, userRight]#addedInt is the C's hand

#===============================get PLAYER's moves and results================
    
def getUserAddingHand():
    #input P's hand that P is gonna add to the C's hand
    while True:
        addingHand=input('Which of your hand will you add from, [L]eft or [R]ight? ---> ')
        if (addingHand=='L' or addingHand=='R'):
            return addingHand
        else:
            print('That is not a legal response. Please enter [L] or [R]')
            print('--------------------------------------------------')

def getUserTargetHand():
    #input C's hand that P wants to add to
    while True:
        targetHand=input('Which of Computer hand will you add to, [L]eft or [R]ight? --- >')
        if (targetHand=='L' or targetHand=='R'):
            return targetHand
        else:
            print('That is not a legal response. Please enter [L] or [R]')
            print('--------------------------------------------------')
        
def getResultsOfUserMove(addingHand, targetHand, computerLeft, computerRight, userLeft, userRight):
    #add P's hand number to the C's hand the P wants to add to
    if(addingHand=='L' and targetHand=='L'):
        computerLeft += userLeft
        addedInteger=userLeft
    elif(addingHand=='L' and targetHand=='R'):
        computerRight += userLeft
        addedInteger=userLeft
    elif(addingHand=='R' and targetHand=='L'):
        computerLeft += userRight
        addedInteger=userRight
    elif(addingHand=='R' and targetHand=='R'):
        computerRight += userRight
        addedInteger=userRight
    return [addedInteger, computerLeft, computerRight]

#=================check Zero-out================================================
        
def checkZerosOut(userRight, userLeft, computerRight, computerLeft):
    #if one hand reaches 5 or above, make it 0
    if (userRight>=5):
        userRight=0
    elif (userLeft>=5):
        userLeft=0
    elif (computerRight>=5):
        computerRight=0
    elif (computerLeft>=5):
        computerLeft=0
    return [userRight, userLeft, computerRight, computerLeft]

#==============================allow COMPUTER to split==========================

def askComputerSplit(computerLeft, computerRight):
    computerCount=computerLeft+computerRight
    if (computerCount<2 or computerCount>6):
        return False
    else:
        return True

def computerSplit(computerLeft, computerRight, userLeft, userRight):
    computerCount=computerLeft+computerRight
    #for sticks in range (initialCount+1):
    if(computerCount<4):
        if(computerLeft==computerCount or computerRight==computerCount):
            #if all sticks on one hand, split
            computerLeft=1
            computerRight=computerCount-computerLeft
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
        else:
            computerLeft=computerCount
            computerRight=0
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
    elif(computerCount==4):
        if(computerLeft==computerCount or computerRight==computerCount):
            #if all sticks on one hand, split
            computerLeft=1
            computerRight=computerCount-computerLeft
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
            computerLeft=2
            computerRight=computerCount-computerLeft
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
        elif(computerLeft==1 or computerLeft==3):
            computerLeft=computerCount
            computerRight=0
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
            computerLeft=2
            computerRight=computerCount-computerLeft
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
        else:
            computerLeft=computerCount
            computerRight=0
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
            computerLeft=1
            computerRight=computerCount-computerLeft
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
    else:
        if(computerLeft==3 or computerRight==3):
            computerLeft=4
            computerRight=computerCount-computerLeft
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
        else:
            computerLeft=3
            computerRight=computerCount-computerLeft
            if(computerLeft+userLeft<5 and computerRight+userLeft<5 and computerLeft+userRight<5 and computerRight+userRight<5):
                #checks so that the user cannot eliminate any of the computer's hands
                return [computerLeft, computerRight]
    return False

#==============================allow PLAYER to split============================

def askUserSplit(userLeft, userRight):
    if 1<(userLeft + userRight)<7:
        while True:
            userChoice = input("Do you want to split? [Y]es or [N]o ---> ")
            if userChoice == 'Y':
                return True
            elif userChoice == 'N':
                return False
            else:
                print('That is not a legal response. Please enter a single uppercase letter.')
                print('---------------------------------------------------------------------')
    else:
        return False
    
def userSplit(userLeft, userRight):
    userCount=userLeft+userRight
    while True:
        print('How would you like to split?')
        try:
            leftChoice = int(input('What number would your left hand have? --- > '))
            rightChoice = userCount-leftChoice
            if(leftChoice==userLeft or leftChoice==userRight):
                print('You trickster! You must make a viable change to the count on either hand!')
                print('----------------------------------------------------------')
            elif(leftChoice>4 or rightChoice>4):
                print('You know you cannot have 5 or more fingers on either hand!')
                print('----------------------------------------------------------')
            elif(leftChoice<0 or rightChoice<0):
                print('You cannot have less than 0 fingers on either hand!')
                print('----------------------------------------------------------')
            elif (leftChoice + rightChoice) == userCount:
                return  [leftChoice, rightChoice]
            else:
                print('You must make sure both hands add up to the same initial amount!')
                print('----------------------------------------------------------')
        except:
            print('That is not a legal response. Please enter a single digit.')
            print('----------------------------------------------------------')

#==============================THE GAME=========================================

def playChopsticks():
    print('* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * ')
    print('Time to get choppy bois!')
    currentPlayer=getStartingPlayer()
    computerLeft=1
    computerRight=1
    userLeft=1
    userRight=1
    userSplitTimes = 0
    computerDifficulty=setComputerDifficulty()
    print('================CP LEFT====CP RIGHT==================')
    print('================UR LEFT====UR RIGHT==================')
    print('Computer Hand:', '[    ' + str(computerLeft)+'    ,    '+str(computerRight) + '    ]')
    print('Your Hand:', '    [    ' + str(userLeft)+'    ,    '+str(userRight) + '    ]')
    print('=====================================================')
    while ((computerLeft + computerRight)>0 and (userRight + userLeft)>0):
        if (currentPlayer == 'C'):
            # computer's turn
            if (computerDifficulty=='H'):
                if (askComputerSplit(computerLeft, computerRight) == True and computerSplit(computerLeft, computerRight, userLeft, userRight)!=False):
                    #SMART computer will split if conditions are met.
                    splitComputerMove = computerSplit(computerLeft, computerRight, userLeft, userRight)
                    computerLeft = splitComputerMove[0]
                    computerRight = splitComputerMove[1]
                    print('Computer splitted!')
                else:
                    currentMove = getComputerMove(computerLeft, computerRight)
                    addingHand=currentMove[0]
                    targetHand=currentMove[1]
                    resultsOfMove = getResultsOfComputerMove(addingHand, targetHand, computerLeft, computerRight, userLeft, userRight)
                    userLeft=resultsOfMove[1]
                    userRight=resultsOfMove[2]
                    print('Computer added', resultsOfMove[0], 'to User', targetHand)
            else:
                currentMove = getComputerMove(computerLeft, computerRight)
                addingHand=currentMove[0]
                targetHand=currentMove[1]
                resultsOfMove = getResultsOfComputerMove(addingHand, targetHand, computerLeft, computerRight, userLeft, userRight)
                userLeft=resultsOfMove[1]
                userRight=resultsOfMove[2]
                print('Computer added', resultsOfMove[0], 'to User', targetHand)
        else:
            # user's turn
            if askUserSplit(userLeft, userRight) == True:
                #ask if PLAYER wants to split. If not, go to add.
                splitUserMove = userSplit(userLeft, userRight)
                userLeft = splitUserMove[0]
                userRight = splitUserMove[1]
                print('User splitted!')
                userSplitTimes += 1
            else:
                addingHand = getUserAddingHand()
                targetHand = getUserTargetHand()
                resultsOfMove=getResultsOfUserMove(addingHand, targetHand, computerLeft, computerRight, userLeft, userRight)
                computerLeft=resultsOfMove[1]
                computerRight=resultsOfMove[2]
                print('User added', resultsOfMove[0], 'to Computer', targetHand)
        #check if split too many times
        if userSplitTimes > 7:
            print('User has splitted too many times! GAME OVER!')
            return
        #next step is to check zero-out
        userLeft=checkZerosOut(userRight, userLeft, computerRight, computerLeft)[1]
        userRight=checkZerosOut(userRight, userLeft, computerRight, computerLeft)[0]
        computerLeft=checkZerosOut(userRight, userLeft, computerRight, computerLeft)[3]
        computerRight=checkZerosOut(userRight, userLeft, computerRight, computerLeft)[2]
        #give the calculated result
        print('================CP LEFT====CP RIGHT==================')
        print('================UR LEFT====UR RIGHT==================')
        print('Computer Hand:', '[    ' + str(computerLeft)+'    ,    '+str(computerRight) + '    ]')
        print('Your Hand:', '    [    ' + str(userLeft)+'    ,    '+str(userRight) + '    ]')
        print('=====================================================')
        currentPlayer = getOtherPlayer(currentPlayer)
        #Next code determines winner
        if(computerLeft + computerRight == 0):
            print('User wins!')
            return
        elif(userLeft + userRight == 0):
            print('Computer wins!')
            return
    
playChopsticks()