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
        elif name == "mudkip":
            self.type = "water"
            self.hp = 50
            self.attack = 70
            self.defence = 50
            self.spAttack = 50
            self.spDefence = 50
            self.speed = 40
            self.display1 = "  _||_  "
            self.display2 = ">(o..o)<"
            self.display3 = "   \" \"  "
            self.reverse1 = "  _||_  "
            self.reverse2 = ">(o..o)<"
            self.reverse3 = "   \" \"  "
            self.move1 = Move("water gun")
            self.move2 = Move("growl")
            self.move3 = Move("tackle")
            self.move4 = Move("endeavor")
        elif name == "pidgey":
            self.type = "flying"
            self.hp = 40
            self.attack = 45
            self.defence = 40
            self.spAttack = 35
            self.spDefence = 35
            self.speed = 56
            self.reverse1 = "<(\")    "
            self.reverse2 = "  (@@)> "
            self.reverse3 = "   ' '  "
            self.display1 = "    (\")>"
            self.display2 = "  <(@@) "
            self.display3 = "   ' '  "
            self.move1 = Move("quick attack")
            self.move2 = Move("gust")
            self.move3 = Move("agility")
            self.move4 = Move("wing attack")
        elif name == "bunnelby":
            self.type = "normal"
            self.hp = 38
            self.attack = 36
            self.defence = 38
            self.spAttack = 32
            self.spDefence = 36
            self.speed = 57
            self.display1 = "  (\_/) "
            self.display2 = "  (o.o) "
            self.display3 = "  (^ ^) "
            self.reverse1 = " (\_/)  "
            self.reverse2 = " (o.o)  "
            self.reverse3 = " (^ ^)  "
            self.move1 = Move("quick attack")
            self.move2 = Move("bounce")
            self.move3 = Move("take down")
            self.move4 = Move("flail")
        elif name == "meowth":
            self.type = "normal"
            self.hp = 40
            self.attack = 45
            self.defence = 35
            self.spAttack = 40
            self.spDefence = 40
            self.speed = 90
            self.display1 = "  /\_/\ "
            self.display2 = " ( o.o )"
            self.display3 = "  > ^ < "
            self.reverse1 = " /\_/\  "
            self.reverse2 = "( o.o ) "
            self.reverse3 = " > ^ <  "
            self.move1 = Move("growl")
            self.move2 = Move("scratch")
            self.move3 = Move("bite")
            self.move4 = Move("slash")
        self.originalSpeed = self.speed
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
        elif name == "scratch":
            self.category = "ph"
            self.type = "normal"
            self.power = 40
        elif name == "bounce":
            self.category = "ph"
            self.type = "flying"
            self.power = 0.85
            self.accuracy = 0.85
        elif name == "take down":
            self.category = "ph"
            self.type = "normal"
            self.power = 0.9
            self.accuracy = 0.85
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
        elif name == "endeavor":
            # This is a physical attack but is coded as a status attack
            self.type = "normal"
            self.category = "st"
        elif name == "gust":
            self.category = "sp"
            self.type = "flying"
            self.power = 0.4
        elif name == "agility":
            self.type = "psychic"
            self.category = "st"
        elif name == "wing attack":
            self.type = "flying"
            self.category = "sp"
            self.power = 0.6
        elif name == "flail":
            self.type = "normal"
            self.category = "ph"
        

def play():
    q = None
    while(q != "q"):
        clearScreen ()
        choice = None
        firstAttempt = True
        while (choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6" and choice != "7" and choice != "8" and choice != "9"):
            if (not firstAttempt):
                print("Invalid choice! Please select a number between 1 and 9!")
            firstAttempt = False
            print("Select a pokemon: \n1: Pikachu\n2: Squirtle\n3: Bulbasaur\n4: Charmander\n5: Espeon\n6: Mudkip\n7: Pidgey\n8: Bunnelby\n9: Meowth")
            choice = input()
            clearScreen()
        choice = int(choice)
        pkmList = (Pokemon("pikachu"), Pokemon("squirtle"), Pokemon("bulbasaur"), Pokemon("charmander"), Pokemon("espeon"), Pokemon("mudkip"), Pokemon("pidgey"), Pokemon("bunnelby"), Pokemon("meowth"))
        userPkm = pkmList[choice-1]
        rivalPkm = pkmList[random.randint(0,8)]
        if userPkm==rivalPkm:
            rivalPkm=Pokemon(rivalPkm.name)
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
        print("Press 'q' to quit or hit enter to play again.")
        q = input()
    clearScreen()

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
        if(move.name == "flail"):
            move.power = 2-1.75*(rival.hp/rival.hpFull)
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
            message += "But it failed!"
        else:
            message += user.name.capitalize()+"'s defence fell!"
        user.defence = round(current*user.defenceFull)
    elif(move.name == "nasty plot"):
        current = round(rival.spAttack/rival.spAttackFull, 2)
        current = round(current*2, 2)
        if(current >= 4):
            current = 4
            message += "But it failed!"
        else:
            message += rival.name.capitalize()+"'s special attack rose!"
        rival.spAttack = round(current * user.spAttackFull)
    elif(move.name == "growl"):
        current = round(user.attack/user.attackFull, 2)
        current = round(current/2, 2)
        if(current <= 0.1):
            current = 0.1
            message += "But it failed!"
        else:
            message += user.name.capitalize()+"'s attack fell!"
    elif(move.name == "endeavor"):
        if(rival.hp < user.hp):
            damage = user.hp-rival.hp
            user.hp = rival.hp
            message += "It did "+str(damage)+" HP of damage!"
        else:
            message += "But it failed!"
    elif(move.name == "agility"):
        current = round(rival.speed/rival.originalSpeed, 2)
        current = round(current*2, 2)
        if(current >= 4):
            current = 4
            message += "But it failed!"
        else:
            message += rival.name.capitalize()+"'s speed rose!"
        rival.speed = round(current * user.speed)
    print(message)

def attack(move, user, rival):
    message = user.name.capitalize()+" used "+move.name.capitalize()+"! "
    if(move.type=="electric" and (rival.type=="electric" or rival.type=="grass")) or (move.type=="water" and (rival.type=="water" or rival.type=="grass")) or (move.type=="grass" and (rival.type=="grass" or rival.type=="fire")) or (move.type=="fire" and (rival.type=="water" or rival.type=="fire")) or (move.type=="psychic" and rival.type=="psychic") or (move.type=="flying" and rival.type=="electric") or (move.type=="grass" and rival.type=="flying"):
        multiplier = 0.5
    elif(move.type=="electric" and rival.type=="water") or (move.type=="water" and rival.type=="fire") or (move.type=="grass" and rival.type=="water") or (move.type=="fire" and rival.type=="grass") or (move.type=="dark" and rival.type=="psychic") or (move.type=="flying" and rival.type=="grass") or (move.type == "electric" and rival.type == "flying"):
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
        if(move.name == "flail"):
            move.power = 2-1.75*(use.hp/user.hpFull)
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
            message += "But it failed!"
        else:
            message += rival.name.capitalize()+"'s defence fell!"
        rival.defence = round(current*rival.defenceFull)
    elif(move.name == "nasty plot"):
        current = round(user.spAttack/user.spAttackFull, 2)
        current = round(current*2, 2)
        if(current >= 4):
            current = 4
            message += "But it failed!"
        else:
            message += user.name.capitalize()+"'s special attack rose!"
        user.spAttack = round(current * user.spAttackFull)
    elif(move.name == "growl"):
        current = round(rival.attack/rival.attackFull, 2)
        current = round(current/2, 2)
        if(current <= 0.1):
            current = 0.1
            message += "But it failed!"
        else:
            message += rival.name.capitalize()+"'s attack fell!"
    elif(move.name == "endeavor"):
        if(user.hp < rival.hp):
            damage = rival.hp-user.hp
            rival.hp = user.hp
            message += "It did "+str(damage)+" HP of damage!"
        else:
            message += "But it failed!"
    elif(move.name == "agility"):
        current = round(user.speed/user.originalSpeed, 2)
        current = round(current*2, 2)
        if(current >= 4):
            current = 4
            message += "But it failed!"
        else:
            message += user.name.capitalize()+"'s speed rose!"
        user.speed = round(current * user.speed)
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
