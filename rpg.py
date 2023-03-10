# Text Colors ----------------------------------------------------------------------------------------------------------

class ANSI():
    def background(code):
        return "\33[{code}m".format(code=code)

    def style_text(code):
        return "\33[{code}m".format(code=code)

    def color_text(code):
        return "\33[{code}m".format(code=code)




# Game Preparation -----------------------------------------------------------------------------------------------------

class Player:

    def __init__(self, pseudo, health, damage):
        
        self.pseudo_fix()
        
        self.pseudo = pseudo
        self.health = health
        self.damage = damage

        print("")
        print("")
        print(ANSI.color_text(93), self.pseudo, "joined.")
        print(ANSI.color_text(93), "health : ", self.health)
        print(ANSI.color_text(93), "strength : ", self.damage)
        
        
        
    def pseudo_fix():
        while pseudo.lower == "bot":
            print("Error : your name can't be 'bot' ! Please try again : ")
            pseudo = input("-> ")

    def get_pseudo(self):
        return self.pseudo

    def get_health(self):
        return self.health

def attack(p1, p2):
    import random
    dmg = int(p2.damage + random.randint(-7, 7))
    p1.health -= dmg
    print("")
    print(ANSI.color_text(91),  "Ouch ! ", ANSI.color_text(91), p2.pseudo, " attacked ", p1.pseudo, " who lost ", dmg, "hp")
    if p1.health > 0:
        print(ANSI.color_text(91), p1.pseudo, " has ", p1.get_health(), "hp left.")
    else:
        p1.health = 0
        print(ANSI.color_text(91), p1.pseudo, " has ", p1.get_health(), "hp left, he is dead.")


def bandage(p):
    import random
    p.health += random.randint(5, 20)
    if p.health > 100:
        p.health = 100
    print(ANSI.color_text(92), p.pseudo, " treated himself, he has ", p.get_health(), "hp now.")


def pturn():
    print("")
    print(ANSI.color_text(39), ANSI.style_text(1), player1.pseudo, "'s turn :")
    print(ANSI.color_text(39), ANSI.style_text(1), "What do you want to do : attack / bandage / stats : ")

    whattodo = input("-")
    if whattodo == "attack" or whattodo == "bandage" or whattodo == "stats":
        if whattodo == "attack":
            attack(ennemy, player1)

        if whattodo == "bandage":
            if player1.health < 100:
                bandage(player1)
            else:
                print(ANSI.color_text(91), ANSI.style_text(1),"Error : your health is already maxed out, retry")
                pturn()
        if whattodo == "stats":
            print(ANSI.color_text(93), "--------------------stats--------------------")
            print(ANSI.color_text(93), "--------", player1.pseudo, " :")
            print(ANSI.color_text(93), "Health : ", player1.health)
            print(ANSI.color_text(93), "--------", ennemy.pseudo, " :")
            print(ANSI.color_text(93), "Health : ", ennemy.health)
            pturn()

        print("------------------------------------")


    else:
        print(ANSI.color_text(91), ANSI.style_text(1), "Error : You didn't answer correctly, please retry")
        pturn()

def botturn():
    print("")
    print(ANSI.color_text(39), ANSI.style_text(1), ennemy.pseudo, "'s turn :")
    import random
    bot_choice = random.randint(1, 2)
    if bot_choice == 1:
        print("")
        attack(player1, ennemy)
        print("------------------------------------")
    if bot_choice == 2:
        print("")
        if ennemy.health < 100 and ennemy.health > 0:
            bandage(ennemy)
        else:
            attack(player1, ennemy)
            
        print("------------------------------------")    




# Game Start -----------------------------------------------------------------------------------------------------------

player1 = Player(input("Choose a pseudo :\n ->"), 100, 10)
ennemy = Player("Bot", 100, 10)
a = 1
while player1.health > 0 and ennemy.health > 0:
    pturn()
    botturn()



if player1.health < 1:
    pwin = ennemy.pseudo
else:
    pwin = player1.pseudo


print("")
print(ANSI.style_text(2), pwin, " won,")
print(ANSI.style_text(2), "End of the game.")
