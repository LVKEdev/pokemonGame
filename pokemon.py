import os
import random

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Pokemon:
    def __init__(self, name):
        self.name = name
        if name == "pikachu":
            self.type = "electric"
            self.hp = 35
            self.attack = 55
            self.defence = 40
            self.spAttack = 50
            self.spDefence = 50
            self.speed = 90
            self.move1 = Move("thunderbolt")
            self.move2 = Move("quick attack")
            self.move3 = Move("tail whip")
            self.move4 = Move("nasty plot")
            self.display1 = " |\\__/| "
            self.display2 = " {+OO+} "
            self.display3 = "  /  \\  "
            self.reverse1 = " |\\__/| "
            self.reverse2 = " {+OO+} "
            self.reverse3 = "  /  \\  "
        elif name == "squirtle":
            self.type = "water"
            self.hp = 44
            self.attack = 48
            self.defence = 65
            self.spAttack = 50
            self.spDefence = 64
            self.speed = 43
            self.move1 = Move("water gun")
            self.move2 = Move("tail whip")
            self.move3 = Move("bite")
            self.move4 = Move("hydro pump")
            self.display1 = "   ___  "
            self.display2 = "/_|_\\('>"
            self.display3 = " \"   \"  "
            self.reverse1 = "   ____ "
            self.reverse2 = "<'(/_|_\\"
            self.reverse3 = "   \"  \" "
        elif name == "bulbasaur":
            self.type = "grass"
            self.hp = 45
            self.attack = 49
            self.defence = 49
            self.spAttack = 65
            self.spDefence = 65
            self.speed = 45
            self.move1 = Move("vine whip")
            self.move2 = Move("razor leaf")
            self.move3 = Move("tackle")
            self.move4 = Move("growl")
            self.display1 = "||\\\\    "
            self.display2 = "(++[O.O]"
            self.display3 = " \"  \"   "
            self.reverse1 = "    //||"
            self.reverse2 = "[0.0]++)"
            self.reverse3 = "   \"  \" "
        elif name == "charmander":
            self.type = "fire"
            self.hp = 39
            self.attack = 52
            self.defence = 43
            self.spAttack = 60
            self.spDefence = 50
            self.speed = 65
            self.move1 = Move("growl")
            self.move2 = Move("ember")
            self.move3 = Move("inferno")
            self.move4 = Move("slash")
            self.display1 = "('u') * "
            self.display2 = "(^ ^)// "
            self.display3 = " \" \"    "
            self.reverse1 = "('u') * "
            self.reverse2 = "(^ ^)// "
            self.reverse3 = " \" \"    "
        elif name == "espeon":
            self.type = "psychic"
            self.hp = 65
            self.attack = 65
            self.defence = 60
            self.spAttack = 130
            self.spDefence = 95
            self.speed = 110
            self.move1 = Move("bite")
            self.move2 = Move("tackle")
            self.move3 = Move("tail whip")
            self.move4 = Move("psybeam")
            self.display1 = "\\\\__/   "
            self.display2 = "('-') \/"
            self.display3 = "(^&^)_//"
            self.reverse1 = "\\\\__/   "
            self.reverse2 = "('-') \/"
            self.reverse3 = "(^&^)_//"
        self.hpFull = self.hp
        self.attackFull = self.attack
        self.defenceFull = self.defence
        self.spAttackFull = self.spAttack
        self.spDefenceFull = self.spDefence
        self.moves = (self.move1, self.move2, self.move3, self.move4)

class Move:
    def __init__(self,name):
        self.name = name
        self.accuracy = 1
        self.power = 1
        if name == "thunderbolt":
            self.category = "sp"
            self.type = "electric"
            self.power = 0.9
        elif name == "quick attack":
            self.category = "ph"
            self.type = "normal"
            self.power = 0.4
        elif name == "tail whip":
            self.category = "st"
            self.type = "normal"
        elif name == "nasty plot":
            self.category = "st"
            self.type = "dark"
        elif name == "water gun":
            self.category = "sp"
            self.type = "water"
            self.power = 0.4
        elif name == "bite":
            self.category = "ph"
            self.type = "dark"
            self.power = 0.6
        elif name == "hydro pump":
            self.category = "sp"
            self.type = "water"
            self.accuracy = 0.8
            self.power = 1.1
        elif name == "vine whip":
            self.type = "grass"
            self.category = "ph"
            self.power = 0.45
        elif name == "razor leaf":
            self.type = "grass"
            self.category = "sp"
            self.power = 0.55
            self.accuracy = 0.9
        elif name == "tackle":
            self.type = "normal"
            self.category = "ph"
            self.power = 0.4
        elif name == "growl":
            self.type = "normal"
            self.category = "st"
        elif name == "ember":
            self.type = "fire"
            self.category = "sp"
            self.power = 0.4
        elif name == "inferno":
            self.type = "fire"
            self.category = "sp"
            self.accuracy = 0.5
        elif name == "slash":
            self.type = "normal"
            self.category = "ph"
            self.power = 0.4
        elif name == "psybeam":
            self.type = "psychic"
            self.category = "sp"
            self.power = 0.65

def play():
    clearScreen ()
    choice = None
    firstAttempt = True
    while (choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5"):
        if (not firstAttempt):
            print("Invalid choice! Please select a number between 1 and 5!")
        firstAttempt = False
        print("Select a pokemon: \n1: Pikachu\n2: Squirtle\n3: Bulbasaur\n4: Charmander\n5: Espeon")
        choice = input()
        clearScreen()
    choice = int(choice)
    pkmList = (Pokemon("pikachu"), Pokemon("squirtle"), Pokemon("bulbasaur"), Pokemon("charmander"), Pokemon("espeon"))
    userPkm = choice
    rivalPkm = choice
    while (rivalPkm == choice):
        rivalPkm = random.randint(1,5)
    userPkm = pkmList[choice-1]
    rivalPkm = pkmList[rivalPkm-1]
    clearScreen()
    print ("You chose..."+userPkm.name.capitalize()+"! Your rival is..."+rivalPkm.name.capitalize()+"!")
    while (True):
        generateDisplay (userPkm, rivalPkm)
        print ("Select a move!")
        move = input()
        while(move != "1" and move != "2" and move != "3" and move != "4"):
            clearScreen()
            print("Invalid move! Select a move from 1-4")
            generateDisplay(userPkm, rivalPkm)
            move = input()
        userMove = userPkm.moves[int(move) - 1]
        rivalMove = rivalPkm.moves[random.randint(0, 3)]
        if (rivalMove.name == "quick attack" and userMove.name != "quick attack") or (userMove.name == "quick attack" and rivalMove.name != "quick attack"):
            noQuickAttack = False
        else:
            noQuickAttack = True
        if (rivalPkm.speed > userPkm.speed and noQuickAttack) or (userMove.name != "quick attack" and rivalMove.name == "quick attack"):
            clearScreen()
            defend(rivalMove, userPkm, rivalPkm)
            generateDisplay(userPkm, rivalPkm)
            if(checkMatchOver(userPkm, rivalPkm)):
                break
            print("Press enter to continue")
            input()
            clearScreen()
            attack(userMove, userPkm, rivalPkm)
            if(checkMatchOver(userPkm, rivalPkm)):
                generateDisplay(userPkm, rivalPkm)
                break
        else:
            clearScreen()
            attack(userMove, userPkm, rivalPkm)
            generateDisplay(userPkm, rivalPkm)
            if (checkMatchOver(userPkm, rivalPkm)):
                break
            print("Press enter to continue")
            input()
            clearScreen ()
            defend (rivalMove, userPkm, rivalPkm)
            if (checkMatchOver(userPkm, rivalPkm)):
                generateDisplay(userPkm, rivalPkm)
                break
    if (userPkm.hp==0):
        print(userPkm.name.capitalize() + " fainted! " + rivalPkm.name.capitalize() + " is the winner!")
    else:
        print(rivalPkm.name.capitalize() + " fainted! " + userPkm.name.capitalize() + " is the winner!")

def checkMatchOver (user, rival):
    if(user.hp==0 or rival.hp==0):
        return True
    else:
        return False

def defend(move, user, rival):
    message = rival.name.capitalize() + " used " + move.name.capitalize() + "! "
    if(move.type=="electric" and (user.type=="electric" or user.type=="grass")) or (move.type=="water" and (user.type=="water" or user.type=="grass")) or (move.type=="grass" and (user.type=="grass" or user.type=="fire")) or (move.type=="fire" and (user.type=="water" or user.type=="fire")) or (move.type=="psychic" and user.type=="psychic"):
        multiplier = 0.5
    elif(move.type=="electric" and user.type=="water") or (move.type=="water" and user.type=="fire") or (move.type=="grass" and user.type=="water") or (move.type=="fire" and user.type=="grass") or (move.type=="dark" and user.type=="psychic"):
        multiplier = 2
    else:
        multiplier = 1
    if(move.type == rival.type):
        multiplier *= 1.5
    accuracy = random.uniform(0,1)
    if(move.category == "sp"):
        if(accuracy < move.accuracy):
            damage = round((move.power*10*(rival.spAttack/user.spDefence)+2)*multiplier)
            if(damage > user.hp):
                damage = user.hp
            user.hp -= damage
            message+="It did "+str(damage)+" HP of damage!"
        else:
            message+="But it missed!"
    elif(move.category == "ph"):
        if(accuracy < move.accuracy):
            damage = round((move.power*10*(rival.attack/user.defence)+2)*multiplier)
            if(damage > user.hp):
                damage = user.hp
            user.hp -= damage
            message+="It did "+str(damage)+" HP of damage!"
        else:
            message+="But it missed!"
    elif(move.name == "tail whip"):
        current = round(user.defence/user.defenceFull, 2)
        current = round(current/2, 2)
        if(current <= 0.1):
            current = 0.1
            message += "But "+user.name+"'s defence can't fall any lower!"
        else:
            message += user.name+"'s defence fell!"
        user.defence = round(current*user.defenceFull)
    elif(move.name == "nasty plot"):
        current = round(rival.spAttack/rival.spAttackFull, 2)
        current = round(current*2, 2)
        if(current >= 4):
            current = 4
            message += "But "+rival.name+"'s special attack is full!"
        else:
            message += rival.name+"'s special attack rose!"
        rival.spAttack = round(current * user.spAttackFull)
    elif(move.name == "growl"):
        current = round(user.attack/user.attackFull, 2)
        current = round(current/2, 2)
        if(current <= 0.1):
            current = 0.1
            message += "But "+user.name+"'s attack can't fall any lower!"
        else:
            message += user.name+"'s attack fell!"
    print(message)

def attack(move, user, rival):
    message = user.name.capitalize()+" used "+move.name+"! "
    if(move.type=="electric" and (rival.type=="electric" or rival.type=="grass")) or (move.type=="water" and (rival.type=="water" or rival.type=="grass")) or (move.type=="grass" and (rival.type=="grass" or rival.type=="fire")) or (move.type=="fire" and (rival.type=="water" or rival.type=="fire")) or (move.type=="psychic" and rival.type=="psychic"):
        multiplier = 0.5
    elif(move.type=="electric" and rival.type=="water") or (move.type=="water" and rival.type=="fire") or (move.type=="grass" and rival.type=="water") or (move.type=="fire" and rival.type=="grass") or (move.type=="dark" and rival.type=="psychic"):
        multiplier = 2
    else:
        multiplier = 1
    if(move.type==user.type):
        multiplier *= 1.5
    accuracy = random.uniform(0,1)
    if(move.category == "sp"):
        if(accuracy < move.accuracy):
            damage = round((move.power*10*(user.spAttack/rival.spDefence)+2)*multiplier)
            if(damage > rival.hp):
                damage = rival.hp
            rival.hp -= damage
            message+="It did "+str(damage)+" HP of damage!"
        else:
            message+="But it missed!"
    elif(move.category == "ph"):
        if(accuracy < move.accuracy):
            damage = round((move.power*10*(user.attack/rival.defence)+2)*multiplier)
            if (damage > rival.hp):
                damage = rival.hp
            rival.hp -= damage
            message+="It did "+str(damage)+" HP of damage!"
        else:
            message+="But it missed!"
    elif(move.name == "tail whip"):
        current = round(rival.defence/rival.defenceFull, 2)
        current = round(current/2, 2)
        if(current <= 0.1):
            current = 0.1
            message += "But "+rival.name+"'s defence can't fall any lower!"
        else:
            message += rival.name+"'s defence fell!"
        rival.defence = round(current*rival.defenceFull)
    elif(move.name == "nasty plot"):
        current = round(user.spAttack/user.spAttackFull, 2)
        current = round(current*2, 2)
        if(current >= 4):
            current = 4
            message += "But "+user.name+"'s special attack is full!"
        else:
            message += user.name+"'s special attack rose!"
        user.spAttack = round(current * user.spAttackFull)
    elif(move.name == "growl"):
        current = round(rival.attack/rival.attackFull, 2)
        current = round(current/2, 2)
        if(current <= 0.1):
            current = 0.1
            message += "But "+rival.name+"'s attack can't fall any lower!"
        else:
            message += rival.name+"'s attack fell!"
    print(message)

def generateDisplay(user, rival):
    rivalHealthbar = ""
    userHealthbar = ""    
    for section in range(9,0,-1):
        if rival.hp < section * rival.hpFull / 9:
            rivalHealthbar+="░"
        else:
            rivalHealthbar+="█"
    if rival.hp == 0:
        rivalHealthbar += "░"
    else:
        rivalHealthbar+="█"
    for section in range(0,9):
        if user.hp > section * user.hpFull / 9:
            userHealthbar+="█"
        else:
            userHealthbar+="░"
    if user.hp==user.hpFull:
        userHealthbar+="█"
    else:
        userHealthbar+="░"
    print("╔═══════════════════════════════════════╗")
    print("║                  "+rival.type.upper().rjust(9)+" "+rival.name.upper().rjust(10)+" ║")
    print("║                      "+str(rival.hp).rjust(2)+" HP "+rivalHealthbar+" ║")
    print("║                                       ║")
    print("║ "+user.display1+"                     "+rival.reverse1+" ║")
    print("║ "+user.display2+"                     "+rival.reverse2+" ║")
    print("║ "+user.display3+"                     "+rival.reverse3+" ║")
    print("║                                       ║")
    print("║ "+user.name.upper().ljust(10)+" "+user.type.upper().ljust(9)+"                  ║")
    print("║ "+userHealthbar+" "+str(user.hp).ljust(2)+" HP"+"                      ║")
    print("╠═══════════════════╦═══════════════════╣")
    print("║ 1. "+user.move1.name.upper().ljust(15)+"║ 2. "+user.move2.name.upper().ljust(15)+"║")
    print("╠═══════════════════╬═══════════════════╣")
    print("║ 3. "+user.move3.name.upper().ljust(15)+"║ 4. "+user.move4.name.upper().ljust(15)+"║")
    print("╚═══════════════════╩═══════════════════╝")

play()


# Pokemon to be added:

# MUDKIP
#   _||_
# >(o..o)<
#   "  "

# PIDGEY

# <(")
#   (@@)>
#    ' '

# BUNNELBY

# (\_/)
# (o.o)
# (^ ^)

# MEOWTH

#  /\_/\
# ( o.o )
#  > ^ <
