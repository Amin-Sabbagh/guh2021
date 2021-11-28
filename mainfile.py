#global vars:
#level:0
#number of lives:1
hearts = 1
#gameover = false

#imported libraries:
import time
#pygame?? or tkinter if need be
#
# Why u so clever?

def gameover():
    x = input("")
    if input == input:
        exit()

def gameovergood():
    print("")
    print("")
    print("You became a zombie!")
    time.sleep(0.5)
    print("You and Tom the zombie got married")
    time.sleep(0.5)
    print("You and Tom got a house on a fixed interest mortgage rate!")
    time.sleep(0.5)
    print("You've had a child! how is that possible!?")
    time.sleep(0.5)
    print("Both you and tom have lived happily ever after")
    time.sleep(0.5)
    print("while the world decayed into ruins,")
    time.sleep(0.5)
    print("you two are still going strong")
    time.sleep(0.5)
    print("well done!")
    time.sleep(0.5)
    print("humanity lost but you two sure won!")
    time.sleep(0.5)
    print("the end")
    time.sleep(0.5)
    gameover()

def gameoverbad1():
    #play song - really really american one - name??
    print("")
    print("")
    print("wow you killed a zombie... his name was Tom")
    time.sleep(0.5)
    print("He was a father! Child Zombie runs in the scene")
    time.sleep(0.5)
    print("Daddy! Daddy wake up!")
    time.sleep(0.5)
    print(":O")
    time.sleep(0.5)
    print("why did you kill my dad mister?!")
    time.sleep(0.5)
    print('You are a murderer!')
    time.sleep(0.5)
    print("game over")
    gameover()

def gameoverbad2():
    print("")
    print("")
    print("you've been cancelled on twitter")
    time.sleep(0.5)
    print("A large karen voice looms for the rest of your life")
    time.sleep(0.5)
    print("Game Over")
    gameover()

def gameoverbad3():
    print("")
    print("")
    time.sleep(0.5)
    print("Cow just killed you. Made you into a human burger")
    time.sleep(0.5)
    print("Game Over")
    gameover()

def gameoverbad4():
    print("")
    print("")
    print("You were eaten alive!!")
    time.sleep(0.5)
    print("At least you were tasty?")
    gameover()

def level3():
    print("")
    print("")
    print("(You say to yourself) Oh maybe love cures zombie?")
    time.sleep(0.5)
    print("You get closer to the zombie")
    time.sleep(0.6)
    print("Bite!!")
    time.sleep(0.5)
    print("Oh never mind, the zombie bit you..")
    time.sleep(1)
    global hearts
    if hearts <2:
        gameoverbad4()
    else:
        gameovergood()
    return hearts

def level2():
    global hearts
    print("")
    print("")
    print("Level 2")
    time.sleep(0.5)
    print("*The Second Date*")
    time.sleep(0.5)
    print("You and Zombie is going to cemetery")
    time.sleep(0.5)
    print("Look!! a cow in a coat. It's holding a gun!!")
    time.sleep(0.5)
    print("It seems like you have a gun with you. What will you do?")
    time.sleep(0.5)
    print("a: shoot the cow")
    time.sleep(0.5)
    print("b: run away")
    time.sleep(0.5)
    print("c: don't shoot. It could be friendly")
    time.sleep(0.5)
    c = input("action choice:")
    if c == "a":
        hearts += 1
        print("You and the zombie is having some burgers for dinner")
        time.sleep(0.5)
    elif c =="b":
        hearts -= 1
        print("You are shot! But still got away from the nasty cow.")
        time.sleep(0.5)
    elif c == "c":
        print("The cow attacks you!")
        time.sleep(0.5)
        gameoverbad3()
    else:
        print("You did nothing")
        time.sleep(0.5)
    return hearts

def level1():

    global hearts
    print("")
    print("")
    print("Level 1")
    time.sleep(0.5)
    print("*The First Date*") #make this text big
    time.sleep(0.5)
    print("awwwww") #make this text small
    time.sleep(0.5)
    print("choose a movie")
    time.sleep(0.5)
    print("a: twilight")
    time.sleep(0.5)
    print("b: world war z")
    time.sleep(0.5)
    print("c: garfield 3 the movie")
    time.sleep(0.5)
    c = input("movie choice: ")
    time.sleep(0.5)
    if c == "a":
        print("Zombie loves this movie!")
        time.sleep(0.5)
        print("shares some of their brainy popcorn")
        time.sleep(0.5)
        print("zombie and you had a great movie date")
        time.sleep(0.5)
        hearts = hearts + 1
    elif c == "c":
        print("zombie thinks you are immature")
        time.sleep(0.5)
        print("zombie want to go over relationship boundaries")
        time.sleep(0.5)
        print("zombie and you had an meh movie date")
        time.sleep(0.5)
        hearts -= 1
    elif c == "b":
        print("zombie thinks youre insensitive (yikes)")
        time.sleep(0.5)
        print("Oh No! zombie took out their phone and tweeted!")
        time.sleep(0.5)
        print("Zombie storms out of theatre")
        time.sleep(0.5)
        print("Oh no your boss is on the phone! You've been cancelled!")
        time.sleep(0.5)
        hearts -= 1
        gameoverbad2()
    else:
        print('get error checking - note')
    return hearts

def level0():
    global hearts
    print("")
    print("")
    print("There are weapons on the ground! quick choose!")
    time.sleep(0.5)
    print('a: bat')
    time.sleep(0.5)
    print("b: gun")
    time.sleep(0.5)
    print("c: crossbow")
    time.sleep(0.5)
    print("d: bare! hands!")
    time.sleep(0.5)
    weapon = ''
    while weapon == "" or weapon == 'a' or weapon == 'c':
        weapon = input("what do you choose? ")
        time.sleep(0.5)
        if weapon == "a":
            print("You chose bat!")
            time.sleep(0.5)
            print("You hit the zombie!")
            time.sleep(0.5)
            print("boink!") #zombie is hit
            time.sleep(0.5)
            print("Didn't work... zombie is mildly annoyed")
        elif weapon == "b":
            print("You chose a gun")
            time.sleep(0.5)
            print("You shoot the zombie!")
            time.sleep(0.5)
            print("Blood is splattered!")
            time.sleep(0.5)
            print("Zombie lifeless body falls to the floor")
            hearts = 0
        elif weapon == "c":
            print("You chose a crossbow")
            time.sleep(0.5)
            print("You are inexperienced!")
            time.sleep(0.5)
            print("You shot yourself in the foot")
            time.sleep(0.5)
            print("zombie smells your blood, looks hungry")
        elif weapon == "d":
            print("you're going into this empty handed??")
            time.sleep(0.5)
            print("The zombie looks at you awkwardy and gives you a hug")
            time.sleep(0.5)
            print("Wow... there's a connection")
            hearts += 1
        else:
            print("sorry try again, that wasnt one of the options?")
            time.sleep(0.2)

def decison():
    global hearts
    print("")
    print("")
    time.sleep(0.5)
    print("[boo!]")#actual jump scare noise
    time.sleep(0.5)
    print('*DANGER*')
    time.sleep(0.5)
    print('a zombie is approaching you')
    time.sleep(0.5)
    print('What do you do?')
    print("a: Fight")
    print("b: Wait")
    print("c: Run")
    time.sleep(0.5)
    dec1=""
    while(dec1!="a" or dec1!="b" or dec1!="c"):
        dec1 = input("What's your decision?:")
        if dec1 =="a":
            level0()
            return hearts
        elif dec1 =="c":
            time.sleep(0.5)
            print("you were too slow, because you smoked too much before the fallout")
            time.sleep(0.5)
            print("Game Over")
            gameover()
        elif dec1 =="b":
            print("Zombie was waiting for love too..")
            time.sleep(0.5)
            time.sleep(0.5)
            hearts += 1
            print("DATING SIM <3")
            level1()
            break
        else:
            dec1=""

def start():
    global hearts
    print("")
    print("")
    print("Manchester 2077: Zombie Survival Fallout Game")
    print("Press a, b, c for each option choice")
    inp = input("Press enter key to start game ")
    if inp == "":
        print("The year.... is 2077 in Manchester....")
        time.sleep(0.5)
        print("Global Warming has irreversably altered the enviroment....")
        time.sleep(0.5)
        print("as we know it...")
        time.sleep(0.5)
        print("Leading to food supplies issues, nuclear war, general HAVOC")
        time.sleep(0.5)
        print("A new variant of Covid has apeared...")
        time.sleep(0.5)
        print("The Omicron variant produced new zombies")
        time.sleep(0.5)
        print("The objective is to SURVIVE")
        time.sleep(0.5)
        print('--------------------------------------------')
        time.sleep(0.5)
        print("")
        decison()
        if hearts == 0:
            gameoverbad1()
        elif hearts == 3:
            level2()
            level3()
        elif hearts==2:
            level1()
            level2()
            level3()
        else:
            print("???")
    else:
        print('wow')
        time.sleep(0.5)
        print("coward")
        exit()

start()
gameover()
