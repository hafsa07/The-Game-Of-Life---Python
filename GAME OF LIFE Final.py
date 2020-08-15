# Imports ##################################################################################################################################
import time
import random
import math
import os
import sys
# variables ################################################################################################################################
key1 = False
key2 = False
key3 = False
key4 = False
jigsaw = False
axe = False
r3 = False
w = 7
inv = []
t = 5
k = 5
s = 0
p = 2
# time
now = round(time.time())
t = now + 300
# Functions ################################################################################################################################
# HP level 2 ===============================================================================================================================
def hp():
    now = time.time()
    if now > t:
        print("Time Over")
        time.sleep(2)
        print("Game Over")
        time.sleep(2)
        os._exit()
    z = t - now
    z = round(z)
    print("                                                                                                       [HP : ", z,"]")
    return
# timefunction =============================================================================================================================
def tima():
    now = time.time()
    if now > t:
        print("Time Over")
        time.sleep(2)
        print("Game Over")
        time.sleep(2)
        os._os._exit()
    z = t - now
    z = round(z)
    print("                                                                                                  [Time : ",z, "sec]")
    return
# Space function ===========================================================================================================================
def space():
    print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    return
# LEVEL 1 ##################################################################################################################################
# Group Info ===============================================================================================================================
def groupinfo():
    space()
    print ("Game Name     : Game Of Life")
    time.sleep (2)
    print ("Movie Name    : SAW Series")
    time.sleep (2)
    print ("Group Members : Haroon Rashid     FA17-BCS-030\n                Hafsa Muhammad    FA17-BCS-024")
    time.sleep(3)
    return
# How To Play ==============================================================================================================================
def howtoplay():
    space()
    print("!!!   How To Play   !!!")
    time.sleep(1.5)
    print ("\n")
    time.sleep(1.5)
    print ("1. Listen to every word")
    time.sleep(1.5)
    print ("2. Choose correct options")
    time.sleep(1.5)
    print ("3. Use main words to answer")
    time.sleep(1.5)
    print ("\n")
    time.sleep(1.5)
    x = input("Press ENTER to continue the game ...")
    time.sleep(1)
    space()
    print("                                                 ##########     LEVEL : 01     ##########")
    time.sleep(0.5)
    o = 10
    while o > 0:
        print ("\n")
        time.sleep(0.5)
        o = o - 1
    x = input("Press ENTER to continue...")
    return
# Introduction =============================================================================================================================
def intro():
    tima()
    print ("What will you do ?\n1. Try to find a way out\n2. Find light switch")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print ("You can't see any thing\nTry again")
        intro()
    elif a == 2:
        space()
        tima()
        print ("Switch board found. Switch board have three buttons.")
        switch()
    else:
        space()
        tima()
        intro()
    return
# Switch ===================================================================================================================================
def switch():
    tima()
    print ("Which swich you want to try ?\n1. First\n2. Second\n3. Third")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print ("Switch not working\nTry again")
        switch()
    elif a == 2:
        space()
        tima()
        print ("Lights on\nScene :\nYou are in a bathroom chained up. There is a body lying with a scar in his head and blood all over him. There is also a boy chained up at the other side of bathroom.")
        afterswitch()
    elif a == 3:
        space()
        tima()
        print ("Switch not working\nTry again")
        switch()
    else:
        space()
        tima()
        space()
        switch()
    return
# After Switch =============================================================================================================================
def afterswitch():
    tima()
    print ("What will you do now ?\n1. Wake up the boy\n2. Examine the body\n3. Unchain yourself")
    a = int(input(":"))
    if a == 2:
        space()
        tima()
        print ("You can't reach the body. You are chained.\nTry again")
        afterswitch()
    elif a == 3:
        space()
        tima()
        print ("Nothing happened\nTry again")
        afterswitch()
    elif a == 1:
        space()
        tima()
        print ("Boy wakes up")
        boywakesup()
    else:
        space()
        tima()
        space()
        afterswitch()
    return
# Boy wakes up =============================================================================================================================
def boywakesup():
    tima()
    print ("Boy : Where am I ?\n1. You know where is he\n2. You dont know")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print ("You don't know\nAgain")
        boywakesup()
    elif a == 2:
        space()
        tima()
        print ("Boy : Who are you ? What is your name ?")
    else:
        space()
        tima()
        space()
        boywakesup()
    return
# Whats Happening ==========================================================================================================================
def whatshappening():
    tima()
    print("Adam : Do you know what is happening ?\n1. You know\n2. You don't know")
    a = int(input(":"))
    if a == 1:
        tima()
        space()
        print("How could you know. Try again")
        whatshappening()
    elif a == 2:
        tima()
        space()
        print("Adam : (Looked at the body and vomit) What happened to him ? Whose body is this ?\n1. You know\n2. You don't know")
        b = int(input(":"))
        if b == 1:
            tima()
            space()
            print("How could you know. Try again")
        elif b == 2:
            tima()
            space()
        else:
            tima()
            space()
    else:
        tima()
        space()
        whatshappening()
    return
# Scars on body ============================================================================================================================
def scarsonbody():
    tima()
    print("Adam : Do you see any scars on my body?\n1. Yes\n2. No")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("(Sound of truck...)\nAdam shouts for help")
        aftershout()
    elif a == 2:
        space()
        tima()
        print("(Sound of truck...)\nAdam shouts for help")
        aftershout()
    else:
        tima()
        scarsonbody()
        print("Try again")
    return
# After shout ==============================================================================================================================
def aftershout():
    tima()
    print("What will you do now ?\n1. Examine the room\n2. Shout for help")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("Bathroom...")
        time.sleep(2)
        print("""You are at the bottom right of the bathroom. Adam is at the top left of the bathroom.
There is a toilet at your left and a toilet at adam's right and a bathtub on adam's left.
There is a door at the left wall of Adam and another door in the middle of right wall.
There is a brand new clock hanging opposite to the door on wall.""")
        time.sleep(2)
        print("Adam found an envelope")
        adamenvelope()
    elif a == 2:
        space()
        tima()
        print("Nothing happened\nTry again")
        aftershout()
    else:
        tima()
        aftershout()
    return
# Adams envelope ===========================================================================================================================
def adamenvelope():
    tima()
    print("Ask him\n1. Where did you find it\n2. Open it")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("Adam : It was in my pocket")
        time.sleep(2)
        loop1()
    elif a == 2:
        space()
        tima()
        print("Opening ...")
        time.sleep(2)
        print("Adam : There is a tape in my pocket. It says 'Play me'")
        time.sleep(2)
        loop1()
    else:
        space()
        tima()
        adamenvelope()
    return
# Loop1 ====================================================================================================================================
def loop1():
    tima()
    print("What to do now ?\n1. Ask Adam to play tape\n2. Search for your's")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("Adam tape playing ...")
        time.sleep(2)
        print("Rise and shine Adam. You might be wondering where you are. You are probably in a room where you will die.\nThis is game of death and life.")
        x = input("Press ENTER to continue...")
        afteradamtape()
    elif a == 2:
        space()
        tima()
        searchforyours()
    else:
        tima()
        time.sleep(1)
        space()
        tima()
        loop1()
    return
# After adam tape ==========================================================================================================================
def afteradamtape():
    space()
    tima()
    print("Search for yours ?\n1. Yes\n2. No")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("Which pocket?\n1. Right\n2. Left")
        b = int(input(":"))
        if b == 1:
            space()
            tima()
            print("Nothing found\nTry again")
            afteradamtape()
        elif b == 2:
            space()
            tima()
            print("Playing tape ...")
            time.sleep(2)
            print("""Many times you became the cause of someones life. Today you might become the cause of someone's death.
You have to kill Adam in 5 miniutes and your time had already started.If you don't kill Adam in time your dad will die.
There is a connection between your dad and Adams heart.That connection is bomb.There is a timebomb where you dad is and
to swich off the timer you have to kill Adam or you should escape this room.There are clues hidden in room.
Just remember that X marks the spot for treasure in dark.Just follow your heart.Now you can use 2 things in this room.
Ohhh i forgot (Laughing...) You can also use toilet but there is no water and tissues ;D.""")
            c = input("Press ENTER to continue ...")
            cluesession()
    elif a == 2:
        space()
        tima()
        cluesession()
    else:
        space()
        tima()
        time.sleep(2)
        print("Try again")
        afteradamtape()
    return
# Search for yours =========================================================================================================================
def searchforyours():
    tima()
    print("Which pocket ?")
    a = input(":")
    if 'right' in a:
        space()
        tima()
        print("Nothing Found")
        time.sleep(2)
        print("Try again")
        searchforyours()
    elif 'left' in a:
        space()
        tima()
        print("Envelope found\nOpening envelope...")
        time.sleep(2)
        print("Key Tape and Letter is found")
        gowith()
    elif 'front' in a:
        space()
        tima()
        print ("Which pocket from front side ?\n")
        time.sleep(1)
        searchforyours()
    elif 'back' in a:
        space()
        tima()
        print ("Don't have any pocket at the back side of pant.")
        time.sleep(1)
        searchforyours()
    else:
        time.sleep(1)
        space()
        tima()
        print("Try again")
        searchforyours()
    return
# Go with ==================================================================================================================================
def gowith():
    tima()
    space()
    print("key tape or bullet")
    a = input(":")
    a = a.lower()
    if 'key' in a:
        space()
        tima()
        print("Unlock chains using key ?")
        b = input(":")
        b = b.lower()
        if 'yes' in b or 'y' in b:
            space()
            tima()
            print("No use")
            time.sleep(1)
            gowith()
        elif 'no' in b or 'n' in b:
            space()
            tima()
            gowith()
        else:
            space()
            tima()
            gowith()
    elif 'tape' in a:
        space()
        tima()
    elif 'bullet' in a:
        space()
        tima()
        print("Can't use bullet without a gun")
        print("Try somrthing else")
        gowith()
    else:
        space()
        tima()
        gowith()
    return
# Your tape ================================================================================================================================
def haveyoulistenedtoadamtape():
    space()
    tima()
    print("Listen to Adam's tape\n1. Yes\n2. No")
    a = int(input(":"))
    if a == 2:
        space()
        tima()
        cluesession()
    elif a == 1:
        space()
        tima()
        print("""Rise and shine Adam. You might be wondering where you are. You are probably in a room where you will die.
This is game of death and life.""")
        b = input("press ENTER to continue ...")
        cluesession()
    else:
        space()
        tima()
        haveyoulistenedtoadamtape()
    return
# Clue Session =============================================================================================================================
def cluesession():
    space()
    tima()
    print("Lets move onto clue session")
    time.sleep(1)
    print("Now you need to recall the tapes and choose a clue from the tapes to escape.")
    a = input("press ENTER to continue...")
    clue()
    return
# Clue
def clue():
    tima()
    print("Which clue you want to choose?\n(Just enter clue name)")
    a = input(":")
    if a == ("x" or "X" or "x mark" or "X mark" or "xmark" or "Xmark"):
        space()
        tima()
        print("How to find X mark?")
        print("press ENTER to continue ...")
        space()
        xmark()
    elif a == ("heart" or "Heart" or "HEART"):
        space()
        tima()
        print("A heart is drawn on bathtub\nChain saw is found\nAdam is trying to cut the chains ...")
        time.sleep(2)
        print("Nothing happened ...")
        x = input("Press ENTER to continue ...")
        space()
        heart()
    elif a == ("toilet" or "Toilet" or "TOILET"):
        space()
        tima()
        toilet()
    else:
        space()
        tima()
        print("Think think time is running out ...")
        print("Do you want to listen the tapes again?\n1. Yes\n2. No")
        b = int(input(":"))
        if b == 2:
            space()
            tima()
            time.sleep(1)
            print("Then think hard . Time is slipping away\nTry again")
            clue()
        elif b == 1:
            space()
            tima()
            loop2()
    return
# loop2 ====================================================================================================================================
def loop2():
    tima()
    print("Which tape you want to play?\n1. Adam\n2. Your's")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        loop2a()
    elif a == 2:
        space()
        tima()
        loop2b()
    else:
        tima()
        loop2()
    return
# loop2a ===================================================================================================================================
def loop2a():
    if now > t:
        tima()
    print("Playing...")
    print("Adam tape playing...")
    time.sleep(2)
    print("""Rise and shine Adam. You might be wondering where you are. You are probably in a room where you will die.
This is game of death and life.""")
    x = input("press ENTER to continue when finished reading...")
    space()
    print("Do you want to listen to yours?\n1. Yes\n2. No")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        loop2b()
    elif a == 2:
        space()
        tima()
        print("Then try using another clue...")
        clue()
    else:
        space()
        tima()
        loop2a()
    return
# loop2b ===================================================================================================================================
def loop2b():
    tima()
    print("Playing...")
    time.sleep(2)
    print("Many times you became the cause of someones life. Today you might become the cause of someone's death.\nYou have to kill Adam in 5 miniutes and your time had already started.If you don't kill Adam in time your dad will die.\nThere is a connection between your dad and Adams heart.That connection is bomb.There is a timebomb where you dad is and\nto swich off the timer you have to kill Adam or you should escape this room.There are clues hidden in room.\nJust remember that X marks the spot for treasure in dark.Just follow your heart.Now you can use 2 things in this room.\nOhhh i forgot (Laughing...) You can also use toilet but there is no water and tissues ;D.")
    x = input("press ENTER to continue when finished reading")
    space()
    print("Do you want to listen Adam's tape?\n1. Yes\n2. No")
    if a == 1:
        space()
        tima()
        loop2a()
    elif a == 2:
        space()
        tima()
        print("Then try using another clue...")
        clue()
    else:
        space()
        tima()
        loop2b()
    return
# X mark ===================================================================================================================================
def xmark():
    tima()
    print("Where is X? (Give answer using lowercase and no spaces and using main words)")
    a = input(":")
    if a == ("lights off") or ("lights") or ("light") or ("LIGHTS OFF") or ("lightsoff") or ("lightsoff") or ("turnlightsoff") or ("turnofthelights") or ("turnthelightsoff"):
        space()
        tima()
        print("X mark found on wall near you.\nBreaking the wall\nBox is found.Box is locked")
        unlock()
    else:
        space()
        tima()
        print("You are wrong")
        b = int(input("What now?\n1. Choose another clue\n2. Try again"))
        if b == 1:
            space()
            tima()
            clue()
        elif b == 2:
            space()
            tima()
            print("Try again..")
            xmark()
    return
# Unlock ===================================================================================================================================
def unlock():
    tima()
    print("Unlock from whats ?")
    a = input(":")
    if a == ("key") or ("KEY") or ("Key"):
        space()
        tima()
        print("Cigarette , Letter and Pistol are found")
        loop3()
    else:
        space()
        tima()
        print("Can't unlock")
        b = int(input("Now\n1. Choose another clue\n2. Try again"))
        if b == 1:
            space()
            tima()
            clue()
        elif b == 2:
            space()
            tima()
            unlock()
    return
# loop3 ====================================================================================================================================
def loop3():
    tima()
    print("Go with\n1. Letter\n2. Cigarettes\n3. Pistol\n4. Another clue")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        letter()
    elif a == 2:
        space()
        tima()
        cigarettes()
    elif a == 3:
        space()
        tima()
        pistol()
    elif a == 4:
        space()
        tima()
        clue()
    else:
        space()
        tima()
        loop3()
    return
# Letter ===================================================================================================================================
def letter():
    tima()
    print("Reading letter...")
    time.sleep(1)
    print("Adam can be killed by dipping the cigarettes in blood")
    print("Kill Adam using cigarettes?\n1. Yes\n2. No")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("You saved your dad's life but you will rot in the room")
        time.sleep(2)
        print("GAME OVER")
        gameover()
    if a == 2:
        space()
        tima()
        print("Now choose/n1. Another thing\n2. Another clue")
        b = int(input(":"))
        if b == 1:
            space()
            tima()
            loop3()
        elif b == 2:
            tima()
            space()
            clue()
        else:
            space()
            tima()
            loop3()
    else:
        space()
        tima()
        loop3()
    return
#cigarettes ================================================================================================================================
def cigarettes():
    tima()
    print("Smoking ...")
    time.sleep(1)
    print("Puffing...")
    time.sleep(1)
    print("Now what?\n1. Choose another thing\n2. Choose another clue")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        loop3()
    elif a == 2:
        space()
        tima()
        clue()
    else:
        space()
        tima()
        cigarettes()
    return
#pistol ====================================================================================================================================
def pistol():
    tima()
    print("What to do ?\n1. Nothoing\n2. Kill Adam\n3. Kill yourself\n4. Shoot the chain lock")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        loop3()
    elif a == 2:
        space()
        tima()
        print("You saved your dad but you will die")
        gameover()
    elif a == 3:
        space()
        tima()
        gameover()
    elif a == 4:
        space()
        tima()
        print("Nothing happened")
        loop3()
    else:
        space()
        tima()
        loop3()
    return
# Heart ====================================================================================================================================
def heart():
    tima()
    print("Ask him to give you\n1. Yes\n2. No")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("Trying on yours ...")
        time.sleep(1)
        print("Nothing happened")
        heart1()
    elif a == 2:
        space()
        tima()
        print("Then choose another clue")
        clue()
    else:
        space()
        tima()
        heart()
    return
# Heart1 ===================================================================================================================================
def heart1():
    tima()
    print("Try it on somewhere else")
    a = input(":")
    if a == ("leg") or ("Leg") or ("LEG"):
        space()
        tima()
        free()
    else:
        space()
        tima()
        print("Nothing happened/n1. Choose another clue\n2. Try again")
        b = int(input(":"))
        if b == 1:
            space()
            tima()
            clue()
        elif b == 2:
            space()
            tima()
            heart1()
        else:
            space()
            tima()
            print("Try again")
            heart1()
    return
# Toilet ===================================================================================================================================
def toilet():
    tima()
    print("Examine which one?\n1. One close to Adam\n2. One close to You")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("Nothing happened\nNow\n1. Choose another clue\n2. Try toilet close to you")
        b = int(input(":"))
        if b == 1:
            space()
            tima()
            clue()
        elif b == 2:
            space()
            tima()
            toiletu()
        else:
            space()
            tima()
            print("Choose correct options...Try again...\n which toilet you want to Examine")
            toilet()
    elif a == 2:
        space()
        tima()
        toiletu()
    else:
        space()
        tima()
        print("Choose correct options...Try again...\n which toilet you want to Examine")
        toilet()
    return
# toilet u =================================================================================================================================
def toiletu():
    tima()
    time.sleep(2)
    print("A key is found\nTrying on your chainlock")
    print("Trying ...")
    time.sleep(2)
    print("You are free now")
    time.sleep(2)
    print("try it on adams chain lock\n1. Yes\n2. No")
    a = int(input(":"))
    if a == 1:
        space()
        tima()
        print("Adam is free...")
        time.sleep(4)
        print("BooooooooOoOoOOoOOoOOOOOM...")
        time.sleep(2)
        print("A blast that killed Adam")
        time.sleep(2)
        print("Now you are the lone survivor")
        return
    elif a == 2:
        space()
        print("BooOOOOOOoooooOOOoOOooOOMMMMmmMMM....")
        time.sleep(2)
        print("A blast that killes Adam")
        time.sleep(2)
        print("Now you are the lone survivor")
        return
    else:
        space()
        tima()
        toiletu()
    return
# LEVEL 2 ##################################################################################################################################
# lv2 ======================================================================================================================================
def lv2():
    space()
    hp()
    print("You are not free now but you escaped the bathroom and saved your dad's life.")
    time.sleep(2)
    print("This is the second level of the game.")
    time.sleep(3)
    print("                                         ===============LEVEL 2===============              ")
    a = input("press ENTER to continue ...")
    space()
    hp()
    print("You enter a room after escaping the bathroom.There is a locker in the middle of the room")
    time.sleep(2)
    print("There are 6 people sleeping at different cornors.There is also a tape on the locker.")
    a = input("press ENTER to continue...")
    whattodo()
    return
# What to do lv2 ===========================================================================================================================
def whattodo():
    space()
    hp()
    print("You can play tape or you can wake people\nSo what to do?")
    a = input(":")
    a = a.lower()
    if ("wakepeople") in a or ("wake people") in a:
        space()
        hp()
        wakepeople()
    elif ('play tape') in a or ('playtape') in a:
        space()
        hp()
        playtape()
    else:
        space()
        hp()
        print("Try again")
        whattodo()
    return
# play tape lv2 ============================================================================================================================
def playtape():
    space()
    hp()
    print("Hello",name,"We are not done yet. This is your second challenge. You are in a\nroom which is filled with toxic gas, so be quick and yes hints from previous room will help you alot.\n")
    time.sleep(3)
    a = input("press enter to continue...")
    wakepeople()
    return
# wake people lv2 ==========================================================================================================================
def wakepeople():
    space()
    hp()
    print("First Person\nDress Color : Yellow")
    time.sleep(1)
    print("\nHe wakes up")
    a = input("Where am I?\n:")
    space()
    hp()
    a = input("By the way what is your name?\n:")
    space()
    hp()
    print("By the way my name is Eric Methews\n")
    a = input("press Enter to continue...")
    space()
    hp()
    print("You go to second person and wake him up")
    print("Second Person\nDress Color : Green")
    time.sleep(1)
    print("\nHe wakes up")
    a = input("Where am I?\n:")
    space()
    hp()
    a = input("By the way what is your name?\n:")
    space()
    hp()
    print("By the way my name is Xavier\n")
    a = input("press Enter to continue...")
    space()
    hp()
    print("You go to third person and wake her up")
    print("Third Person\nDress Color : Indigo")
    time.sleep(1)
    print("\nHe wakes up")
    a = input("Where am I?\n:")
    space()
    hp()
    a = input("By the way what is your name?\n:")
    space()
    hp()
    print("By the way my name is Amanda Youngs\n")
    a = input("press Enter to continue...")
    space()
    hp()
    print("You go to forth person and wake him up")
    print("Forth Person\nDress Color : Red")
    time.sleep(1)
    print("\nHe wakes up")
    a = input("Where am I?\n:")
    space()
    hp()
    a = input("By the way what is your name?\n:")
    space()
    hp()
    print("By the way my name is Peter\n")
    a = input("press Enter to continue...")
    space()
    hp()
    print("You go to fifth person and wake him up")
    print("Fifth Person\nDress Color : Blue")
    time.sleep(1)
    print("\nHe wakes up")
    a = input("Where am I?\n:")
    space()
    hp()
    a = input("By the way what is your name?\n:")
    space()
    hp()
    print("By the way my name is Harry\n")
    a = input("press Enter to continue...")
    space()
    hp()
    print("You go to sixth person and wake him up")
    print("Sixth Person\nDress Color : Violet")
    time.sleep(1)
    print("\nHe wakes up")
    a = input("Where am I?\n:")
    space()
    hp()
    a = input("By the way what is your name?\n:")
    space()
    hp()
    print("By the way my name is Mark Hoffman\n")
    a = input("press Enter to continue...")
    space()
    hp()
    a = input("press ENTER to continue...")
    space()
    hp()
    print("Now there is a locker in the room and a door and there is a tape on the locker.")
    gowith1()
    return
# go with 1 lv2 ============================================================================================================================
def gowith1():
    a = input("What do you want to go with?")
    a = a.lower()
    if ('door') in a:
        space()
        hp()
        print("Door is locked.Choose another thing.")
        gowith1()
    elif ('locker') in a:
        space()
        hp()
        print("Can't open the locker you don't know the combination.\nTry again")
        gowith1()
    elif ('tape') in a:
        space()
        hp()
        print("Hello",name,"We are not done yet. This is your second challenge. You are in a\nroom which is filled with toxic gas, so be quick and yes hints from previous room will help you alot.\n")
        b = input("press ENTER to continue ...")
        tryclue()
    else:
        space()
        hp()
        gowith1()
    return
# Try Clue lv2 =============================================================================================================================
def tryclue():
    a = input("Enter the clue\n:")
    a = a.lower()
    if ('heart') in a:
        space()
        hp()
        print("A heart is on the wall.You can break the wall")
        breakthewall()
    else:
        space()
        hp()
        print("Try Again")
        tryclue()
    return
# Break the wall lv2 =======================================================================================================================
def breakthewall():
    a = int(input("1. Break the wall\n2. Don't break the wall\n:"))
    if a == 2:
        space()
        hp()
        print("You can't go further without breaking the wall")
        breakthewall()
    elif a == 1:
        space()
        hp()
        print("Letter and key are found")
        gowith2()
    return
# Go with 2 lv2 ============================================================================================================================
def gowith2():
    a = input("Choose one thing from key and letter\n:")
    a = a.lower()
    if ('key') in a:
        space()
        hp()
        key()
    elif ('letter') in a:
        space()
        hp()
        letter1()
    return
# Key lv2 ==================================================================================================================================
def key():
    print("Apply key on this door\n1. By Yourself\n2. Ask someonelse")
    a = int(input(":"))
    if a == 1:
        space()
        hp()
        shotbygun()
    elif a == 2:
        space()
        hp()
        print("Eric Methews is shot by the gun.He is dead.Door didn't opened.")
        try0()
    else:
        space()
        hp()
        print("Try again")
        key()
    return
# try 0 lv2 ================================================================================================================================
def try0():
    print("Try again to open door or read letter")
    a = input(":")
    a = a.lower()
    if ('letter') in a:
        space()
        hp()
        letter1()
    elif ('tryagain') in a:
        space()
        hp()
        by0()
    else:
        space()
        hp()
        try0()
    return
# By 0 lv2 =================================================================================================================================
def by0():
    print("Apply key on this door\n1. By Yourself\n2. Ask someonelse")
    a = int(input(":"))
    if a == 1:
        space()
        hp()
        shotbygun()
    elif a == 2:
        space()
        hp()
        print("Xavier is shot by the gun.He is dead.Door didn't opened.")
        try1()
    else:
        space()
        hp()
        print("Try again")
        by0()
    return
# try 1 lv2 ================================================================================================================================
def try1():
    print("Try again to open door or read letter")
    a = input(":")
    a = a.lower()
    if ('letter') in a:
        space()
        hp()
        letter1()
    elif ('tryagain') in a:
        space()
        hp()
        by1()
    else:
        space()
        hp()
        try1()
    return
# by 1 lv2 =================================================================================================================================
def by1():
    print("Apply key on this door\n1. By Yourself\n2. Ask someonelse")
    a = int(input(":"))
    if a == 1:
        space()
        hp()
        shotbygun()
    elif a == 2:
        space()
        hp()
        print("Amanda YOungs is shot by the gun.He is dead.Door didn't opened.")
        try2()
    else:
        space()
        hp()
        print("Try again")
        by1()
    return
# Shot by gun lv2 ==========================================================================================================================
def shotbygun():
    print("                                                                                                       [HP : 0]")
    print("You are dead. Game Over")
    return
# try2 lv2 =================================================================================================================================
def try2():
    print("Try again to open door or read letter")
    a = input(":")
    a = a.lower()
    if ('letter') in a:
        space()
        hp()
        letter1()
    elif ('tryagain') in a or ('try again') in a:
        space()
        hp()
        by2()
    else:
        space()
        hp()
        try2()
    return
# by2 lv2 ==================================================================================================================================
def by2():
    print("Apply key on this door\n1. By Yourself\n2. Ask someonelse")
    a = int(input(":"))
    if a == 1:
        space()
        hp()
        shotbygun()
    elif a == 2:
        space()
        hp()
        print("Peter is shot by the gun.He is dead.Door didn't opened.")
        try3()
    else:
        space()
        hp()
        print("Try again")
        by2()
    return
# try3 lv2 =================================================================================================================================
def try3():
    print("Try again to open door or read letter")
    a = input(":")
    a = a.lower()
    if ('letter') in a:
        space()
        hp()
        letter1()
    elif ('tryagain') in a or ('try again') in a:
        space()
        hp()
        by3()
    else:
        space()
        hp()
        try3()
    return
# by3 lv2 ==================================================================================================================================
def by3():
    print("Apply key on this door\n1. By Yourself\n2. Ask someonelse")
    a = int(input(":"))
    if a == 1:
        space()
        hp()
        shotbygun()
    elif a == 2:
        space()
        hp()
        print("Harry is shot by the gun.He is dead.Door didn't opened.")
        try4()
    else:
        space()
        hp()
        print("Try again")
        by3()
    return
# try4 lv2 =================================================================================================================================
def try4():
    print("Try again to open door or read letter")
    a = input(":")
    a = a.lower()
    if ('letter') in a:
        space()
        hp()
        letter1()
    elif ('tryagain') in a or ('try again') in a:
        space()
        hp()
        by4()
    else:
        space()
        hp()
        try4()
    return
# by4 lv2 ==================================================================================================================================
def by4():
    print("Apply key on this door\n1. By Yourself\n2. Ask someonelse")
    a = int(input(":"))
    if a == 1:
        space()
        hp()
        shotbygun()
    elif a == 2:
        space()
        hp()
        print("Mark Hoffman is shot by the gun.He is dead.Door didn't opened.")
        try5()
    else:
        space()
        hp()
        print("Try again")
        by4()
    return
# try 5 lv2 ================================================================================================================================
def try5():
    print("Now you are the only person left in this room.Try again by yourself to open the door or read letter")
    a = input(":")
    a = a.lower()
    if ('letter') in a:
        space()
        hp()
        letter1()
    elif ('tryagain') in a or ('try again') in a:
        space()
        hp()
        time.sleep(2)
        print("Hurraaaaayyyyyy ... ")
        time.sleep(1)
        print("The door opens.You are not shoted because the revolver is emptied")
        lv3()
    return
# letter1 lv2 ==============================================================================================================================
def letter1():
    space()
    hp()
    print("This is the key of the door that is infront of you but don't you dare to use this death key.\nAnd one more thing the combination of locker is rainbow")
    a = input("press ENTER to continue...")
    try6()
    return
# try6 lv2==================================================================================================================================
def try6():
    print("Now you can use the key on the door or use the clue in the letter")
    a = input("What do you want to do?\n:")
    a = a.lower()
    if ('key') in a:
        space()
        hp()
        key()
    elif ('clue') in a:
        space()
        hp()
        clue1()
    else:
        space()
        print("invalid input. try again")
        try6()
    return
# clue 1 lv2 ===============================================================================================================================
def clue1():
    a = input("What is the clue in the letter?\n:")
    a = a.lower()
    if ('rainbow') in a:
        space()
        hp()
        rainbow()
    elif ('push') in a or ('pull') in a:
        space()
        hp()
        print("There is a tunnel under the locker.\nDo you want to go there?")
        b = input(":")
        b = b.lower()
        if ('yes') in b or ('y') in b:
            space()
            hp()
            print("You escaped the the room")
            lv3()
        elif ('no') in b or ('n') in b:
            space()
            hp()
            print("Then choose a clue")
            clue1()
    else:
        space()
        hp()
        clue1()
    return
# rainbow lv2 ==============================================================================================================================
def rainbow():
    a = input("What does this clue means ?\n:")
    a = a.lower()
    if ('shirt') in a or ('shirts') in a:
        space()
        hp()
        rainbowseq()
    else:
        space()
        hp()
        print("You are wrong\nTry another clue")
        time.sleep(2)
        clue1()
    return
# rainbowseq lv2 ===========================================================================================================================
def rainbowseq():
    print("Write sequence of colors in rainbow using first letter of colors")
    a = input(":")
    a = a.lower()
    if 'roygbiv' in a:
        space()
        hp()
        shirtcolors()
    else:
        space()
        hp()
        print("Wrong")
        print("Try again\n1.Yes\n2.No")
        b = int(input(":"))
        if b == 1:
            space()
            hp()
            rainbowseq()
        elif b == 2:
            space()
            hp()
            print("Then try clue")
            clue1()
    return
# shirt colors lv2 =========================================================================================================================
def shirtcolors():
    print("Now tell the colors of shirts of all people inside room")
    yourshirt()
    return
# Your shirt lv2 ===========================================================================================================================
def yourshirt():
    a = input("Color of your shirt : ")
    a = a.lower()
    if 'orange' in a:
        print("\n")
        ericshirt()
    else:
        space()
        hp()
        print("Wrong !!! Try again or Use key on door")
        b = input(":")
        b = b.lower()
        if "try again" in b:
            space()
            hp()
            yourshirt()
        elif 'key' in b:
            space()
            hp()
            key()
    return
# eric shirt lv2 ===========================================================================================================================
def ericshirt():
    a = input("Color of Eric Methews shirt : ")
    a = a.lower()
    if 'yellow' in a:
        print("\n")
        xaviershirt()
    else:
        space()
        hp()
        print("Wrong !!! Try again or Use key on door")
        b = input(":")
        b = b.lower()
        if 'tryagain' in b or 'try again' in b:
            space()
            hp()
            ericshirt()
        elif 'key' in b:
            space()
            hp()
            key()
    return
# xaviershirt lv2 ==========================================================================================================================
def xaviershirt():
    a = input("Color of Xavier shirt : ")
    a = a.lower()
    if 'green' in b:
        print("\n")
        amandahirt()
    else:
        space()
        hp()
        print("Wrong !!! Try again or Use key on door")
        b = input(":")
        b = b.lower()
        if 'tryagain' in b or 'try again' in b:
            space()
            hp()
            xaviershirt()
        elif 'key' in b:
            space()
            hp()
            key()
    return
# amanda shirt lv2 =========================================================================================================================
def amandashirt():
    a = input("Color of Amanda Young shirt : ")
    a = a.lower()
    if 'indigo' in a:
        print("\n")
        petershirt()
    else:
        space()
        hp()
        print("Wrong !!! Try again or Use key on door")
        b = input(":")
        b = b.lower()
        if b == 'tryagain' in a or 'try again' in a:
            space()
            hp()
            amandashirt()
        elif 'key' in a:
            space()
            hp()
            key()
    return
# petershirt lv2 ===========================================================================================================================
def petershirt():
    a = input("Color of Peter shirt : ")
    a = a.lower()
    if 'red' in a:
        print("\n")
        harryshirt()
    else:
        space()
        hp()
        print("Wrong !!! Try again or Use key on door")
        b = input(":")
        b = b.lower()
        if 'tryagain' in a or 'try again' in a:
            space()
            hp()
            petershirt()
        elif 'key' in a:
            space()
            hp()
            key()
    return
# harry shirt lv2 ==========================================================================================================================
def harryshirt():
    a = input("Color of Harry shirt : ")
    a = a.lower()
    if 'blue' in a:
        print("\n")
        markshirt()
    else:
        space()
        hp()
        print("Wrong !!! Try again or Use key on door")
        b = input(":")
        b = b.lower()
        if 'tryagain' or 'try again' in a:
            space()
            hp()
            harryshirt()
        elif 'key' in a:
            space()
            hp()
            key()
    return
# mark shirt lv2 ===========================================================================================================================
def markshirt():
    a = input("Color of Mark Hoffman shirt : ")
    a = a.lower()
    if 'violet' in a:
        print("\n")
        time.sleep(2)
        print("Good.there are numbers written on the shirts by arranging the shirts in rainbow color order a number combination is found that is 8434149")
        tryonlocker()
    else:
        space()
        hp()
        print("Wrong !!! Try again or Use key on door")
        b = input(":")
        b = b.lower()
        if 'tryagain' or 'try again' in a:
            space()
            hp()
            markshirt()
        elif 'key' in a:
            space()
            hp()
            key()
    return
# try on locker ============================================================================================================================
def tryonlocker():
    print("Try this code on locker")
    a = input(":")
    a = a.lower()
    if 'yes' in a or 'y' in a:
        space()
        hp()
        print("A letter is found saying there is tunnel under the locker so push the locker to escape")
        push()
    elif 'no' in a or 'n' in a:
        space()
        hp()
        print("Then try another clue")
        clue1()
    else:
        space()
        hp()
        tryonlocker()
    return
# push lv2 =================================================================================================================================
def push():
    a = input("Push the locker ?\n:")
    a = a.lower()
    if 'yes' in a or 'y' in a:
        space()
        print("You are free now you escaped this room")
        lv3()
    elif 'no' in a or 'n' in a:
        space()
        hp()
        print("You are dying.Check your Hp be quick and now try key on door")
        key()
    else:
        space()
        hp()
        push()
    return
# LEVEL3 ###################################################################################################################################
# checker lv3 ==============================================================================================================================
def checker():
    if key1==True and key2==True and key3==True and key4==True:
        space()
        unlocking()
    else:
        return
    return
# chitchat
def chitchat():
    print("are u tired and need a break ;)\nyes\nno\n ?")
    a = (input(":"))
    a = a.lower()
    if 'yes' in a or 'y'in a:
        space()
        print("lets have some riddles in this break")
        b = input("press ENTER tocontinue")
        space()
        riddle1()
    elif 'no' in a or 'n' in a:
        space()
        lv3()
    else:
        chitchat()
    return
# riddle1()
def riddle1():
    global p
    global s
    while p > 0:
        print("What ends everything always.")
        a = input(":")
        a = a.lower()
        if 'g' in a:
            space()
            s = s + 1
            print("You scored")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tscore = ",s)
            b = input("press ENTER to continue...")
            p = 2
            riddle2()
        else:
            space()
            print("Wrong")
            time.sleep(1)
            print("Wan't hint\n1.Yes\n2.No")
            b = int(input(":"))
            if a == 1:
                space()
                print("Answer is just an alphabet")
                riddle1()
            elif a == 2:
                space()
                riddle1()
            else:
                space()
                print("invalid input")
                riddle1()
        return
# riddle2()
def riddle2():
    global p
    global s
    while p > 0:
        print("What is the center of gravity?")
        a = input(":")
        a = a.lower()
        if 'v' in a:
            space()
            s = s + 1
            print("You scored")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tscore = ",s)
            b = input("press ENTER to continue...")
            p = 2
            riddle3()
        else:
            space()
            print("Wrong")
            time.sleep(1)
            print("Wan't hint\n1.Yes\n2.No")
            b = int(input(":"))
            if a == 1:
                space()
                print("Answer is just an alphabet")
                riddle2()
            elif a == 2:
                space()
                riddle2()
            else:
                space()
                print("invalid input")
                riddle2()
        return
#riddle3
def riddle3():
    global p
    global s
    while p > 0:
        print("What word becomes shorter when you add two letters to it?")
        a = input(":")
        a = a.lower()
        if 'short' in a:
            space()
            s = s + 1
            print("You scored")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tscore = ",s)
            b = input("press ENTER to continue...")
            p = 2
            riddle4()
        else:
            space()
            print("Wrong")
            time.sleep(1)
            print("Wan't hint\n1.Yes\n2.No")
            b = int(input(":"))
            if a == 1:
                space()
                print("Answer is an english word.")
                riddle3()
            elif a == 2:
                space()
                riddle3()
            else:
                space()
                print("invalid input")
                riddle3()
        return
#riddle4()
def riddle4():
    global p
    global s
    while p > 0:
        print("You can see me in water. but i never get wet.who am I?")
        a = input(":")
        a = a.lower()
        if 'reflection' in a:
            space()
            s = s + 1
            print("You scored")
            print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tscore = ",s)
            b = input("press ENTER to continue...")
            p = 2
            lv3()
        else:
            space()
            print("Wrong")
            time.sleep(1)
            print("Wan't hint\n1.Yes\n2.No")
            b = int(input(":"))
            if a == 1:
                space()
                print("Answer is an english word.")
                riddle4()
            elif a == 2:
                space()
                riddle4()
            else:
                space()
                print("invalid input")
                riddle4()
        return    
# level 3 ==================================================================================================================================
def lv3():
    print("You are not free yet. You enter a new room.There are four lockers in the room and\na escape door infront of you.THe door have 2 key holes and a letter is hanging in the door.\nLocker 1 is at South-West corner of room\nLocker 2 is at North-West corner of the room\nLocker 3 is at North-East corner of the room\nLocker 4 is at South-East corner of the room")
    a = input("press ENTER to continue ...")
    space()
    go1()
    return
# go1 lv3 ==================================================================================================================================
def go1():
    print("Where you want to go ?\nnorth : The escape door\nwest : locker 1\neast : locker 4")
    a = input(":")
    a = a.lower()
    if a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Locker 4\n")
        locker4()
    elif a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Locker 1\n")
        locker1()
    elif a == ("north" or "n"):
        space()
        print("                                                         Current  Position : Exit door\n")
        escapedoor()
    else:
        space()
        print("Cant go that side")
        go1()
    return
# locker4 lv3 ==============================================================================================================================
def locker4():
    a = input("Try to open ?\n: ")
    a = a.lower()
    if a == ("yes" or "y"):
        space()
        print("Nothing happened")
        go2()
    elif a == ("no" or "n"):
        space()
        go2()
    else:
        space()
        print("                                                          Current  Position : Locker 4\n")
        locker4()
    return
# go2 lv3 ==================================================================================================================================
def go2():
    print("Now where you want to go ?\nwest : The door from which you entered\nnorth : locker 3")
    a = input(":")
    a = a.lower()
    if a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Enterence door\n")
        go1()
    elif a == ("north" or "n"):
        space()
        print("                                                          Current  Position : Locker 3\n")
        locker(3)
    else:
        space()
        print("                                                          Current  Position : Locker 4\n")
        go2()
    return
# locker 3 lv3 =============================================================================================================================
def locker3():
    a = input("Try to open ?")
    a = a.lower()
    if a == ("yes" or "y"):
        space()
        print("Nothing happened")
        go3()
    elif a == ("no" or "n"):
        space()
        go3()
    else:
        space()
        print("                                                          Current  Position : Locker 3\n")
        locker3()
    return
# go3 lv3 ==================================================================================================================================
def go3():
    print("Where you want to go ?\nsouth : locker 4\nwest : door with hanging letter")
    a = input(":")
    a = a.lower()
    if a == ("south" or "s"):
        space()
        print("                                                          Current  Position : Locker 4\n")
        locker4()
    elif a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Exit door\n")
        escapedoor()
    else:
        print("Cant go that way")
        print("                                                          Current  Position : Locker 3\n")
        go3()
    return
# escapedoor lv3 ===========================================================================================================================
def escapedoor():
    print("You can read letter or try to unlock the door")
    a = input("Now you can read letter or try to unlock door or go somewhere else. What to do?\n :")
    a = a.lower()
    if a == ("door" or "unlock"):
        space()
        print("Nothing happened")
        escapedoor()
    elif a == "go":
        space()
        go4()
    elif a == ("letter"):
        space()
        letter2()
    else:
        space()
        print("                                                          Current  Position : Exit Door\n")
        escapedoor()
    return
# go4 lv3 ==================================================================================================================================
def go4():
    print("Where you want to go ?")
    a = input("east : locker 3\nsouth : door from which you entered the room\nwest : Locker 2")
    a = a.lower()
    if a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Locker 3\n")
        locker3()
    elif a == ("south" or "s"):
        space()
        print("                                                          Current  Position : Enterence door\n")
        go1()
    elif a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Locker 2\n")
        locker2()
    else:
        space()
        print("Cant go there")
        print("                                                          Current  Position : Exit door\n")
        go4()
    return
# locker1 lv3 ==============================================================================================================================
def locker1():
    print("Try to open it?")
    a = input(":")
    a = a.lower()
    if a == ("yes" or "y"):
        space()
        print("Nothing Happened")
        print("                                                          Current  Position : Locker 1\n")
        go5()
    elif a == ("no" or "n"):
        space()
        print("                                                          Current  Position : Locker 1\n")
        go5()
    else:
        space()
        print("                                                          Current  Position : Locker 1\n")
        locker1()
    return
# Go5 lv3 ==================================================================================================================================
def go5():
    print("Where you want to go?\neast : door from which you entered the room\nnorth : locker 2")
    a = input(":")
    a = a.lower()
    if a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Enterence door\n")
        go1()
    elif a == ("north" or "n"):
        space()
        print("                                                          Current  Position : Locker 2\n")
        locker2()
    else:
        space()
        print("cant go in that direction")
        print("                                                          Current  Position : Locker 1\n")
        go5()
    return
# locker2 lv3 ==============================================================================================================================
def locker2():
    print("Try to open?")
    a = input(":")
    a = a.lower()
    if a == ("yes" or "y"):
        space()
        print("Nothing Happened")
        print("                                                          Current  Position : Locker 2\n")
        go6()
    elif a == ("no" or "n"):
        space()
        print("                                                          Current  Position : Locker 2\n")
        go6()
    else:
        space()
        print("                                                          Current  Position : Locker 2\n")
        locker2()
    return
# go6 lv3 ==================================================================================================================================
def go6():
    print("Where you want to go?")
    a = input("south : The door from which you entered\neast : The escape door")
    if a == ("south" or "s"):
        space()
        print("                                                          Current  Position : Locker 1\n")
        locker1()
    elif a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Exit door\n")
        escapedoor()
    else:
        space()
        print("Cant go that side")
        print("                                                          Current  Position : Locker 2\n")
        go6()
    return
# letter2 lv3 ==============================================================================================================================
def letter2():
    print("hello This is me again.This is the last room after escaping this room you will be absolutely free.I want to tell you that all of these lockers contain keys so use your mind to open them.After escapin this room go to the room infront of you to save your daughter.")
    print("Now you have to open the lockers")
    a = input("press ENTER to continue...")
    space()
    print("                                                          Current  Position : Exit door\n")
    go7()
    return
# go7 lv3 ==================================================================================================================================
def go7():
    print("Where you want to go?\neast : locker 3\nwest : locker 2\nsouth : the door from which you entered the room")
    a = input(":")
    a = a.lower()
    if a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Locker 3\n")
        lock3()
    elif a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Locker 2\n")
        lock2()
    elif a == ("south" or "s"):
        space()
        print("                                                          Current  Position : Enterence door\n")
        dr()
    else:
        space()
        print("                                                          Current  Position : Exit door\n")
        go7()
    return
# dr lv3 ===================================================================================================================================
def dr():
    print("                                                          Current  Position : Enterence door\n")
    go8()
    return
# go8 lv3 ==================================================================================================================================
def go8():
    print("Where to go?\neast : Locker 4\nnorth : Infront of escape door\nwest : locker1")
    a = input(":")
    a = a.lower()
    if a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Locker 4\n")
        lock4()
    elif a == ("north" or "n"):
        space()
        print("                                                          Current  Position : Exit Door\n")
        go7()
    elif a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Locker 1\n")
        lock1()
    else:
        space()
        print("You cant go there")
        print("                                                          Current  Position : Enterence Door\n")
        go8()
    return
# lock3 lv3 ================================================================================================================================
def lock3():
    global key3
    global inv
    if key3 == True:
        space()
        print("                                                          Current  Position : Locker 3\n")
        go9()
    else:
        print("Answer this to unlock the locker 3")
        print("0,5,10,15,___?")
        a = int(input(":"))
        if a == 20:
            key3 = True
            inv.append('key3')
            print("                                     inventory",inv)
            checker()
            print("                                                          Current  Position : Locker 3\n")
            go9()
        else:
            space()
            print("Try again")
            print("                                                          Current  Position : Locker 3\n")
            lock3()
    return
# go9 lv3 ==================================================================================================================================
def go9():
    print("Where you want to go?\nsouth : locker 4\nwest : Escape door")
    a = input(":")
    a = a.lower()
    if a == ("south" or "s"):
        space()
        print("                                                          Current  Position : Locker 4\n")
        lock4()
    elif a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Exit door\n")
        go7()
    else:
        space()
        print("Cant go there")
        print("                                                          Current  Position : Locker 3\n")
        go9()
    return
# lock4 lv3 ================================================================================================================================
def lock4():
    global key4
    if key4 == True:
        space()
        print("                                                          Current  Position : Locker 4\n")
        go10()
    else:
        print("Answer the question to get the key from the locker 4")
        print("First prime number after 1000")
        a = int(input(":"))
        if a == 1009:
            key4 = True
            checker()
            print("                                                          Current  Position : Locker 4\n")
            go10()
        else:
            print("Try again?")
            b = input(":")
            b = b.lower()
            if b == ("yes" or "y"):
                space()
                print("                                                          Current  Position : Locker 4\n")
                lock4()
            elif b == ("no" or "n"):
                space()
                print("                                                          Current  Position : Locker 4\n")
                go10()
            else:
                space()
                print("                                                          Current  Position : Locker 4\n")
                go10()
    return
# go10 lv 3 ================================================================================================================================
def go10():
    print("Now where to go\nnorth : locker 3\nwest : locker2")
    a = input(":")
    a = a.lower()
    if a == ("north" or "n"):
        space()
        print("                                                          Current  Position : Locker 3\n")
        lock3()
    elif a == ("west" or "w"):
        space()
        print("                                                          Current  Position : Locker 2\n")
        lock2()
    else:
        space()
        print("You cant go there")
        print("                                                          Current  Position : Locker \n")
        go10()
    return
# lock2 lv3 ================================================================================================================================
def lock2():
    global key2
    global inv
    if key2 == True:
        space()
        print("                                                          Current  Position : Locker 2\n")
        go11()
    else:
        print("Answer the question to unlock locker2")
        a = int(input("4x5-10+15/5="))
        if a == 7:
            key2 = True
            inv.append('key2')
            print("                                     inventory",inv)
            checker()
            print("                                                          Current  Position : Locker 2\n")
            go11()
        else:
            print("Try again")
            a = input(":")
            a = a.lower()
            if a == ("yes" or "y"):
                space()
                print("                                                          Current  Position : Locker 2\n")
                lock2()
            elif a == ("no" or "n"):
                space()
                print("                                                          Current  Position : Locker 2\n")
                go11()
            else:
                space()
                print("                                                          Current  Position : Locker 2\n")
                lock2()
    return
# go11 lv3 =================================================================================================================================
def go11():
    print("Where you want to go ?\neast : escape door\nsouth : locker1")
    a = input(":")
    a = a.lower()
    if a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Exit Door\n")
        go7()
    elif a == ("south" or "s"):
        space()
        print("                                                          Current  Position : Locker 1\n")
        lock1()
    else:
        space()
        print("You cant go that way")
        print("                                                          Current  Position : Locker 2\n")
        go11()
    return
# lock1 lv3 ================================================================================================================================
def lock1():
    global inv
    global key1
    if key1 == True:
        space()
        print("                                                          Current  Position : Locker 1\n")
        go12()
    else:
        print("Answer the folowing question to get key1")
        a = int(input("first prime number before 1000"))
        if a == 997:
            key1 = True
            inv.append('key1')
            print("                                     inventory",inv)
            checker()
            print("                                                          Current  Position : Locker 1\n")
            go12()
        else:
            print("Try Again")
            b = input(":")
            b = b.lower()
            if b == ("yes" or "y"):
                space()
                print("                                                          Current  Position : Locker 1\n")
                lock1()
            elif b == ("no" or "n"):
                space()
                print("                                                          Current  Position : Locker 1\n")
                go12()
            else:
                space()
                print("                                                          Current  Position : Locker 1\n")
                lock1()
    return
# go12 lv3 =================================================================================================================================
def go12():
    print("Where to go?\nnorth : locker2\neast : locker3")
    a = input(":")
    a = a.lower()
    if a == ("north" or "n"):
        space()
        print("                                                          Current  Position : Locker 2\n")
        lock2()
    elif a == ("east" or "e"):
        space()
        print("                                                          Current  Position : Locker 3\n")
        lock3()
    else:
        space()
        print("                                                          Current  Position : Locker 1\n")
        go12()
    return
# unlocking lv3 ============================================================================================================================
def unlocking():
    global key1
    global key2
    global key3
    global key4
    global w
    global inv
    inv = []
    print("NOW YOU HAVE ALL THE KEYS . A COMBINATION OF TWO KEYS WILL OPEN THE DOOR . DOOR HAVE 2 KEY HOLES SO ENTER THE KEY ORDER CORRECTLY BECAUSE 12 DOES NOT MEANS 21.yOU HAVE ONLY",w,"TRIES OR YOU WILL STUCK HERE FOREVER")
    a = int(input(":"))
    if a == 42:
        space()
        print("You escaped the room")
        key1 = False
        key2 = False
        key3 = False
        kay4 = False
        start()
    else:
        space()
        print("Wrong!!!")
        if w < 1:
            space()
            print("The game is over.You are out of turns")
            print("You are locked here forever ...")
            os._exit()
        else:
            space()
            print("Try again")
            w = w - 1
            unlocking()
    return
# LEVEL 4 ##################################################################################################################################
# start ====================================================================================================================================
def start():
    print ("The house where your dad is in front of you. You have to cross the road to reach there.")
    a = input("press ENTER to continue...")
    go_1()
    return
# go_1 =====================================================================================================================================
def go_1():
    space()
    print ("Where you want to go?\nNorth : House door")
    a = input(":")
    a = a.lower()
    if "west" or "east" in a:
        space()
        print ("You want to save your father?")
        b = input(":")
        b = b.lower()
        if "no" in b:
            space()
            print ("Game over you escaped but your dad died in that house.")
            os._exit(1)
        elif "yes" in b:
            space()
            print ("Then go north\n")
            go_1()
    elif "north" in a:
        space()
        print ("You are in front of the house door. There is door bell and the door is unlocked and there is an axe at side of door")
        a = input("press ENTER to continue...")
        what_to_do()
    else:
        space()
        print ("Can't go in that direction.\n")
        go_1()
    return
# what_to_do ===============================================================================================================================
def what_to_do():
    global axe
    print ("what to do?")
    a = input(":")
    a = a.lower()
    if "ring" or "bell" in a:
        space()
        print ("Nothing happened. Try again\n")
        what_to_do()
    elif "open" or "door" in a:
        space()
        print ("Door opened and you saw a wolf running towards you.")
        time.sleep(1)
        b = input("Type kill to kill him")
        b = b.lower()
        if "kill" in b:
            if axe == True:
                space()
                print ("You killed him by hitting him with axe")
                rooms()
                c = input("press ENTER to continue...")
                space()
            else:
                space()
                print ("You was not able to kill the wolf because you don't had the axe and the wolf killed you")
                os._exit(1)
        else:
            space()
            print ("The wolf killed you")
            os._exit(1)
    elif axe == False:
        if "axe" in a:
            space()
            axe = True
            print ("You picked up the axe")
        else:
            space()
            print ("You already have the axe")
            what_to_do()
    else:
        space()
        print ("invalid input!")
        what_to_do()
    return
# rooms ====================================================================================================================================
def rooms():
    print ("Now you are inside the house and there are seven rooms in the house. Room 4 is in front of you. Room 1, 2 and 3 are at the East where as room 5, 6 and 7 are in the West opposite to room 1, 2 and 3 respectively. Each room door is of different color\nRoom 1 = Door color : Blue\nRoom 2 = Door color : Yellow\nRoom 3 = Door color : Indigo\nRoom 4 = Door color : Red\nRoom 5 = Door color : Green\nRoom 6 = Door color : Orange\nRoom 7 = Door color : Violet")
    a = input("press ENTER to continue...")
    space()
    go_2()
    return
# go_2 =====================================================================================================================================
def go_2():
    print ("North : Room 1(Blue door) + Room 7(Violet door)")
    a = input("Where you want to go?")
    a = a.lower()
    if "north" in a:
        space()
        room17()
    else:
        space()
        print ("Can't go there. Try again")
        go_2()
    return
# room17 ===================================================================================================================================
def room17():
    print ("want to open doors or go some where else")
    a = input(":")
    a = a.lower()
    if "open" or "door" or "doors" in a:
        space()
        open1()
    elif "go" or "somewhere" or "else" in a:
        space()
        go_3()
    else:
        space()
        print ("invalid input. Try again")
        room17()
    return
# go_3 =====================================================================================================================================
def go_3():
    print ("North : Room 2(Yellow) and room6(Orange)\nSouth : Entrance door\nWHere to go?")
    a = input(":")
    a = a.lower()
    if "north" in a:
        space()
        room26()
    elif "south" in a:
        space()
        go_2()
    else:
        space()
        print ("Can't go there try again")
        go_3()
    return
# room26 ===================================================================================================================================
def room26():
    print ("Open rooms or go some where else?")
    a = input(":")
    a = a.lower()
    if "open" or "room" or "rooms" in a:
        space()
        open2()
    elif "go" or "somewhere" or "else":
        space()
        go_4()
    else:
        space()
        print ("invalid input. Try again")
        room26()
    return
# go_4 =====================================================================================================================================
def go_4():
    print ("North : room3(Indigo) and room4(Red) and room5(Green)\nSouth : Room2(Yellow) and Room6(Orange)")
    a = input("Where to go ?")
    a= a.lower()
    if "north" in a:
        space()
        room345()
    elif "south" in a:
        space()
        room17()
    else:
        space()
        print ("invalid input. Try again")
        go_4()
    return
# room345 ==================================================================================================================================
def room345():
    print ("Go some where or open doors?")
    a = input(":")
    a = a.lower()
    if "go" or "somewhere" or "else" in a:
        space()
        go_5()
    elif "open" or "door" or "doors" in a:
        space()
        open3()
    else:
        space()
        print ("invalid input. Try again")
        room345()
    return
# go_5 =====================================================================================================================================
def go_5():
    print ("South : Room2(Yellow) and Room6(Orange)")
    a = input("Where to go?")
    a = a.lower()
    if "south" in a:
        space()
        room26()
    else:
        space()
        print ("invalid input. Try again")
        go_5()
    return
# open1 ====================================================================================================================================
def open1():
    print ("Which room you want to open?\n1. Room 1 : Blue\n2. Room 7 : Violet")
    a = int(input(":"))
    if a == 1:
        space()
        room1()
    elif a == 2:
        space()
        room7()
    else:
        space()
        print ("invalid input. Try again")
        open1()
    return
# room1 ====================================================================================================================================
def room1():
    if key3 == False:
        if r3 == True:
            space()
            ques1()
        else:
            space()
            print ("Can't go at this time")
            room17()
    else:
        space()
        print (inv)
        print ("You already have key3")
        room17()
    return
# ques1 ====================================================================================================================================
def ques1():
    print ("5+5-5x5/5=?")
    a = int(input(":"))
    if a == 5:
        space()
        d1()
    else:
        space()
        a = input("try again")
        a = a.lower()
        if "yes" or "try again" in a:
            space()
            ques1()
        elif "no" in a:
            space()
            room17()
    return
# d1 =======================================================================================================================================
def d1():
    global key3
    global inv
    print ("There are 6 drawers in the room. Open drawer to search for keys.")
    a = int(input("Open which one? 1,2,3,4,5,6"))
    if a == 4:
        space()
        key3 = True
        inv.append('key3')
        print("                                     inventory",inv)
        print ("You get the key")
        room17()
    else:
        space()
        print ("Try again")
        d1()
    return
# open 2 ===================================================================================================================================
def open2():
    print ("Which room you want to open?\n1. Room 2 : Yellow\n2. Room 6 : Orange")
    a = int(input(":"))
    if a == 1:
        space()
        room2()
    elif a == 2:
        space()
        room6()
    else:
        space()
        print ("invalid input. Try again")
        open2()
    return
# room2 ====================================================================================================================================
def room2():
    if key2 == False:
        if key1 == True:
            space()
            ques2()
        else:
            space()
            print ("Can't go at this time")
            room26()
    else:
        space()
        print (inv)
        print ("You already have key3")
        room26()
    return
# ques2 ====================================================================================================================================
def ques2():
    print ("square table of length 5 if 9 tables are brought together they make a new square big table what is its perimeter")
    a = int(input(":"))
    if a == 60:
        space()
        d2()
    else:
        space()
        a = input("try again")
        a = a.lower()
        if "yes" or "try again" in a:
            space()
            ques2()
        elif "no" in a:
            space()
            room26()
    return
# d2 =======================================================================================================================================
def d2():
    global key2
    global inv
    print ("There are 6 drawers in the room. Open drawer to search for keys.")
    a = int(input("Open which one? 1,2,3,4,5,6"))
    if a == 6:
        space()
        key2 = True
        inv.append('key2')
        print("                                     inventory",inv)
        print ("You get the key")
        room26()
    else:
        space()
        print ("Try again")
        d2()
    return
# open3 ====================================================================================================================================
def open3():
    print ("Which room you want to open?\n1. Room 3 : Indigo\n2. Room 4 : Red\n3. Room 5 : Green")
    a = int(input(":"))
    if a == 1:
        space()
        room3()
    elif a == 2:
        space()
        room4()
    elif a == 3:
        space()
        room5()
    else:
        space()
        print ("invalid input. Try again")
        open3()
    return
# room3 ====================================================================================================================================
def room3():
    if key4 == False:
        if key3 == True:
            space()
            ques3()
        else:
            space()
            print ("Can't go at this time")
            room345()
    else:
        space()
        print (inv)
        print ("You already have key3")
        room345()
    return
# ques3 ====================================================================================================================================
def ques3():
    global t
    r = randint(1,11)
    print ("tell the number from 1 to 10 in 5 turns or u will stuck here forever.")
    while t > 1:
        a = int(input(":"))
        if a == r:
            space()
            d3()
        else:
            t = t - 1
    print ("Your father is locked for ever . You escaped.")
    os._exit(1)
    return
# d3 =======================================================================================================================================
def d3():
    global key4
    global inv
    print ("There are 6 drawers in the room. Open drawer to search for keys.")
    a = int(input("Open which one? 1,2,3,4,5,6"))
    if a == 1:
        space()
        key4 = True
        inv.append('key4')
        print("                                     inventory",inv)
        print ("You get the key")
        room345()
    else:
        space()
        print ("Try again")
        d3()
    return
# room3 ====================================================================================================================================
def room_3():
    if key4 == False:
        if key3 == True:
            space()
            ques3()
        else:
            space()
            print ("Can't go at this time")
            room345()
    else:
        space()
        print (inv)
        print ("You already have key3")
        room345()
    return
# rOOM
def room_m():
    def room_3():
    if key4 == True:
        if key3 == False:
            space()
            ques3()
        else:
            space()
            print ("Can't go at this time")
            room345()
    else:
        space()
        print (inv)
        print ("You already have key3")
        room345()
    return
    return
# ques3 ====================================================================================================================================
def ques_3():
    global t
    r = randint(1,11)
    print ("tell the number from 1 to 10 in 5 turns or u will stuck here forever.")
    while t > 1:
        a = int(input(":"))
        if a == r:
            space()
            d_3()
        else:
            t = t - 1
    print ("Your father is locked for ever . You escaped.")
    os._exit(1)
    return
# d3 =======================================================================================================================================
def d_3():
    global key4
    global inv
    print ("There are 6 drawers in the room. Open drawer to search for keys.")
    a = int(input("Open which one? 1,2,3,4,5,6"))
    if a == 1:
        space()
        key4 = True
        inv.append('key4')
        print("                                     inventory",inv)
        print ("You get the key")
        room345()
    else:
        space()
        print ("Try again")
        d_3()
    return
# room7 ====================================================================================================================================
def room7():
    global k
    if (key1 == True) and (key2 == True) and (key3 == True) and (key4 == True):
        print ("Now a combination of two keys will open the door. Try combinations. You have 5 chances. After 5 chances your father will die")
        while k > 0:
            print("Chances left : ",k)
            a = int(input(":"))
            if a == 43:
                space()
                print ("The door unlocked and you found your father fatal.")
                b = input("press ENTER to continue...")
                space()
                last1()
            else:
                space()
                k = k - 1
    else:
        space()
        print ("You dont have all the keys. Check inventory and try again")
        room17()
    return
# last1 ====================================================================================================================================
def last1():
    print ("Now you can escape the house with your father or take revenge first from the person")
    a = input(":")
    a = a.lower()
    if "revenge" in a:
        space()
        revenge()
    elif "escape" in a:
        space()
        escape()
    else:
        space()
        print ("invalid input. Try again")
        last1()
    return
# room6 ====================================================================================================================================
def room6():
    if key1 == False:
        if jigsaw == True:
            space()
            ques4()
        else:
            space()
            print ("Can't go at this time")
            room26()
    else:
        space()
        print (inv)
        print ("You already have key3")
        room26()
    return
# ques4 ====================================================================================================================================
def ques4():
    global key1
    print ("Enter the code")
    a = int(input(":"))
    if a == 8434149:
        space()
        d4()
    else:
        space()
        print ("Do you want to try again?")
        b = input(":")
        b = b.lower()
        if "yes" or "y" in a:
            space()
            ques4()
        elif "no" or "n" in a:
            space()
            room26()
        else:
            space()
            ques4()
    return
# d4 =======================================================================================================================================
def d4():
    global key1
    global inv
    print ("There are 6 drawers in the room. Open drawer to search for keys.")
    a = int(input("Open which one? 1,2,3,4,5,6"))
    if a == 5:
        space()
        key1 = True
        inv.append('key1')
        print("                                     inventory",inv)
        print ("You get the key")
        room26()
    else:
        space()
        print ("Try again")
        d4()
    return
# room4 ====================================================================================================================================
def room4():
    global jigsaw
    print ("You saw a person sitting on the chair. He is a old guy. There is a table in front of him and a gun on the table on your side.")
    a = input("press Enter to continue...")
    space()
    print ("Guy says : Hello! you might be wondering who am i. So im gonna tell you every thing but just be patient.\nI am the one who did all this to you and other people which died out there. So i am the killer of all.\n there is a room out there in which your father is . he might be in a bad condition dying or else...\n Now you have to save him. Just remember the past chalanges.\nNow you can kill me with this gun but i don't recommend you to do this.")
    a = input("press ENTER to continue...")
    print ("Save your dad or Get gun")
    a = input(":")
    a = a.lower()
    if "save" and "dad" in a:
        space()
        print ("Then search")
        jigsaw = True
        room345()
    elif "gun" in a:
        space()
        print ("You got the gun")
        jigsaw = True
        gun()
    else:
        space()
        print ("incalid input . Try again")
        room4()
    return
# gun ======================================================================================================================================
def gun():
    print ("Now what to do ? kill jigsaw or search for your father")
    a = input(":")
    a = a.lower()
    if "kill" or "jigsaw" in a:
        space()
        killjigsaw()
    elif "search" or "father" in a:
        space()
        print ("Then search")
        room345()
    else:
        space()
        print ("invalid input. Try again")
        gun()
    return
# kill Jigsaw ==============================================================================================================================
def killjigsaw():
    print ("You killed the jigsaw . A bomb explodes in the house and all three of you die in that explosion")
    time.sleep(2)
    print ("He said it before that sometimes hearts become the reason of death. Heart of jigsaw is connected with the bomb and when his heart stopped beating the bomb exploded")
    time.sleep(2)
    print ("Thats why he asked to be patient")
    time.sleep(2)
    space()
    print ("THE GAME OF LIFE .... Let the game begin's")
    os._exit(1)
    return
# room5 ====================================================================================================================================
def room5():
    if key2 == True:
        space()
        ques5()
    else:
        space()
        print (inv)
        print ("You already have key3")
        room345()
    return
# ques5 ====================================================================================================================================
def ques5():
    print ("Enter the first five prime numbers")
    a = int(input(":"))
    b = int(input(":"))
    c = int(input(":"))
    d = int(input(":"))
    e = int(input(":"))
    if (a == 2) and (b == 3) and (c == 5) and (d == 7) and (e == 11):
        space()
        d5()
    else:
        space()
        a = input("try again")
        a = a.lower()
        if "yes" or "try again" in a:
            space()
            ques5()
        elif "no" in a:
            space()
            room345()
        else:
            space()
            print ("invalid")
            ques5()
    return
# d5 =======================================================================================================================================
def d5():
    global r3
    print ("There are 6 drawers in the room. Open drawer to search for keys.")
    a = int(input("Open which one? 1,2,3,4,5,6"))
    r3 = True
    space()
    print ("didn't get any thing. Try again ?")
    b = input(":")
    b = b.lower()
    if "yes" or "y" in b:
        space()
        d5()
    elif "no" or "n" in b:
        space()
        room345()
    else:
        space()
        print ("invalid input try again")
        d5()
    return
# revenege =================================================================================================================================
def revenge():
    print ("Kill him yes or no")
    a = input(":")
    a = a.lower()
    if "yes" or "y" in a:
        space()
        killjigsaw()
    elif "no" or "n" in a:
        space()
        escape()
    else:
        space()
        print ("invalid input")
        revenge()
    return
# escape ===================================================================================================================================
def escape():
    space()
    print ("You escaped the room and saved your dad.")
    es()
    return
# LEVEL 5 ##################################################################################################################################
# After escaping ===========================================================================================================================
def es():
    space()
    print("Your father is in a very bad condition.")
    print("Take him to hospital?")
    a = input(":")
    a = a.lower()
    if 'yes' in a or 'y' in a:
        space()
        print ("There is a car infront of you")
        car()
    elif 'no' in a or 'n' in a:
        space()
        print ('Your father might die in this condition.')
        print ("Want to take him to hospital?")
        b = input(":")
        b = b.lower()
        if 'yes' in b or 'y' in b:
            space()
            print ("There is a car infront of you")
            car()
        elif 'no' in b or 'n' in b:
            space()
            print ("You both escaped the situation")
            police()
        else:
            space()
            print('invalid input')
            es()
    else:
        space()
        print ("invalid input")
        es()
    return
# car ======================================================================================================================================
def car():
    print ("Go there?")
    a = input(":")
    a = a.input()
    if 'yes' in a or 'y' in a:
        space()
        print ("You are infront of the car")
        icar()
    elif 'no' in a or 'n' in a:
        space()
        print ("Then go home")
        time.sleep(1)
        print ('After 2 days your father died because of his bad condition.')
        time.sleep(1.5)
        print ("Game Over")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        time.sleep(0.5)
        print("\n")
        os._exit(1)
    else:
        space()
        print("invalid input")
        time.sleep(1)
        car()
    return
# infront of car ===========================================================================================================================
def icar():
    print ("WHat to do ?")
    a = input (":")
    a = a.lower()
    if "unlock" in a:
        space()
        print("Nothing happened. The door is not openeing")
        time.sleep(1)
        icar()
    elif "open" in a or "open door" in a:
        space()
        print ("Nothiong Happened . The door is locked")
        sleep.time(1)
        icar()
    elif "break" in a:
        space()
        print ("Window is broken Now what")
        time.sleep(1)
        icar1()
    else:
        space()
        print ("invalid input")
        time.sleep(1)
        icar()
    return
# After breaking window icar1
def icar1():
    print ("Now what to do?")
    a = input(":")
    if "unlock" in a:
        space()
        print ("The door is unlocked")
        openthedoor()
    else:
        space()
        print("invalid input")
        icar1()
    return
# Open the door
def openthedoor():
    space()
    print("You open the door and make you dad sit at the front seat and you sat")
    drive()
    return
# drive
def drive():
    space()
    print ("Drive him to the hospital or home?")
    a = input(":")
    a = a.lower()
    if "hospital" in a:
        space()
        print("You reached the hospital. Now your dad is in ICU")
        next_1()
    elif "home" in a:
        space()
        print("You reached home .... After two days your dad died because of bad condition")
        os._exit(1)
    else:
        space()
        print("invalid input")
        time.sleep(1)
        drive()
    return
# after reching hospital
def next_1():
    print ("Call police???")
    a = input(":")
    a = a.lower()
    if "yes" in a or "y" in a:
        space()
        print("Phone is ringing")
        policecall()
    elif "no" or "n" in a:
        space()
        print("Game ends")
        os._exit(1)
    else:
        space()
        print("Invalid input")
        time.sleep(1)
        next_1()
    return
# police call
def policecall():
    print("Police Officer : Hello! Who is speaking?")
    a = input(":")
    print("Hi ",a,"Can i help you")
    a = input(":")
    if "yes" in a or "y" in a:
        space()
        policecall1()
    elif "no" in a or "n" in a:
        space()
        print("Police Man : Are you Sure?")
        a = input(":")
        a = a. lower()
        if "yes" in a or "y" in a:
            space()
            print("Police Man : You don't have to be afraid of anyone.Now tell me is there any problem?")
            a = input(":")
            a = a.lower()
            if "yes" in a or "y" in a:
                space()
                policecall1()
            elif "no" in a or "n" in a:
                space()
                print("Police man cut the call.Game ends")
                os._exit(1)
        elif "no" in a or "n" in a:
            space()
            policecall1()
    else:
        space()
        print("invalid input")
        time.sleep(1)
        policecall()
    return
# police call 1
def policecall1():
    print("Police man what is the problem?")
    a = input(":")
    a = a.lower()
    print("Police Man : Sir please can you mention the place again")
    a = input(":")
    print("police man : Thanku sir for informing us ... now we will handle the situation...")
    time.sleep(1)
    print("After 3 hours the man named Jigsaw is arrested by the police")
    time.sleep(1)
    print("GAME ENDS")
    o = 10
    while o > 0:
        print("\n")
        time.sleep(0.5)
        o = o - 1
    return
# Game Starting ############################################################################################################################
# Group Info ===============================================================================================================================
groupinfo()
# How To Play ==============================================================================================================================
time.sleep(3)
howtoplay()
# Introduction =============================================================================================================================
space()
print ("You wake up in a dark and smelly room. There are no lights. You cant see anything")
intro()
# 78 =======================================================================================================================================
name = input(":")
space()
print ("You : My name is",name,"and I am a doctor")
time.sleep(2)
print ("You : What is your name ?")
time.sleep(2)
print ("Boy : My name is Adam")
# Whats Happening ==========================================================================================================================
whatshappening()
# 99 101 ===================================================================================================================================
print("Adam : I think he is dead.\n")
a = input("Adam : What do you think?\n : ")
space()
print("Adam : (Frightently) I think we are kidnapped and the kidnappers had removed our kidney's. I have seen this before.")
# Scars on body ============================================================================================================================
scarsonbody()
# 240 ======================================================================================================================================
print("Hi",name,"!")
print("Many times you became the cause of someones life. Today you might become the cause of someone's death.\nYou have to kill Adam in 5 miniutes and your time had already started.If you don't kill Adam in time your dad will die.\nThere is a connection between your dad and Adams heart.That connection is bomb.There is a timebomb where you dad is and\nto swich off the timer you have to kill Adam or you should escape this room.There are clues hidden in room.\nJust remember that X marks the spot for treasure in dark.Just follow your heart.Now you can use 2 things in this room.\nOhhh i forgot (Laughing...) You can also use toilet but there is no water and tissues ;D.")
a = input("\nPress ENTER to continue after reading ...")
haveyoulistenedtoadamtape()
# HP code LEVEL2 ===========================================================================================================================
now = round(time.time())
t = now + 300
lv2()