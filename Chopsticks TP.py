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
    if (computerLeft == computerRight):
        return False
    if (((computerLeft + computerRight) == 2)
        or ((computerLeft + computerRight) == 3)
        or ((computerLeft + computerRight) == 4)
        or ((computerLeft + computerRight) == 5)
        or ((computerLeft + computerRight) == 6)):
        return True
    else:
        return False

def computerSplit(computerLeft, computerRight):
    if (computerLeft + computerRight) == 2:
        computerLeft = 1
        computerRight = 1
    elif (computerLeft + computerRight) == 3:
        computerLeft = random.choice([1,2])
        computerRight = 3 - computerLeft
    elif (computerLeft + computerRight) == 4:
        computerleft = 2
        computerRight = 2
    elif (computerLeft + computerRight) == 5:
        computerLeft = random.choice([2,3])
        computerRight = 5 - computerLeft
    elif (computerLeft + computerRight) == 6:
        computerLeft = 3
        computerRight = 3
    return [computerLeft, computerRight]

#==============================allow PLAYER to split============================

def askUserSplit(userLeft, userRight):
    if 1<(userLeft + userRight)<9:
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
    while True:
        print('How would you like to split?')
        leftChoice = int(input('What number would your left hand have? --- > '))
        rightChoice = int(input('What number would your right hand have? ---> '))
        #print(userLeft, userRight, leftChoice, rightChoice)
        if (leftChoice + rightChoice) == (userLeft + userRight):
            return  [leftChoice, rightChoice]
        else:
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
    print('================CP LEFT====CP RIGHT==================')
    print('================UR LEFT====UR RIGHT==================')
    print('Computer Hand:', '[    ' + str(computerLeft)+'    ,    '+str(computerRight) + '    ]')
    print('Your Hand:', '    [    ' + str(userLeft)+'    ,    '+str(userRight) + '    ]')
    print('=====================================================')
    while ((computerLeft + computerRight)>0 or (userRight + userLeft)>0):
        if (currentPlayer == 'C'):
            # computer's turn
            if askComputerSplit(computerLeft, computerRight) == True:
                #SMART computer will split if conditions are met.
                splitComputerMove = computerSplit(computerLeft, computerRight)
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
