#== comparison
#< less than
#<= less than equal to
#> greater than
#>= greater than equal to

# or One needs to be true
# and Both need be true to be true
# not oppisite of True or False

"""Build a story game with different scenarios using if statements.
Make sure you use the health variable to keep track of health and have the users health change
in different scenarios"""
health = 0
mana = 0
stamina = 0
gold = 0
damage = 0
defense = 0


classType = input("\nWhat class did you want to play? (1: Warrior, 2: Mage, 3: Rogue)\n")

if classType == "1":
    health = 200
    mana = 0
    stamina = 200
    damage = 100
    gold = 100

    print(f"You chose Warrior your health is {health}, Mana is {mana},and stamina is {stamina}. \n")

elif classType == "2":
    health = 100
    mana = 200
    damage = 300
    stamina = 100
    gold = 100
    print(f"You chose Mage your health is {health}, Mana is {mana},and stamina is {stamina}.\n")

elif classType == "3":
    health = 150
    mana = 0
    stamina = 150
    damage = 120
    gold = 200
    print(f"You chose Rogue your health is {health}, Mana is {mana},and stamina is {stamina}.\n")

print("\nYou enter a tavern and hear two adventurers behind you talking about a\n"
+ "dungeon that appeared in the fog that suddenly appeared in the local forest\n")

choice = input("Do you : \n" 
+"1:Ask to go with them to explore.\n"
+"2:Let them go themselves and go to the dungeon later on and continue drinking your beer.\n")

if choice == "1":
    print("You order a round of fresh ale for the three of you and start asking about this dungeon\n")
    print(" the adventurers tell you that there is supposedly losts of valuable treasure in this new place that appreared.\n")
    print("after many beers drank between the three of you you all decide to set off on the adventure in the morning.\n")

elif choice == "2":
    print("You finish your beer and listen to the two adventurers talk about the dungeon that appeared.\n")
    print("")
    print("you decide to leave in the morning towards the dungeon.\n")
    print("")
    print("as you leave the tavern the two adventerers ambush you and ask if you were eavesdropping on their conversation\n"
    + "about the dungeon and try to fight with you and mugg you.\n")

    choice = input("do you stay and fight or do you run? (fight/run)\n")
   
    if choice == "Fight".lower():
        print("You start brawling with the two adventurers")
        print("")
        print("you fight off the two adventurers as best you could and knock out one of them"
        + ", but the remaning one gets one good blow in and knocks you out.")
        print(f"You wake up in the morning and check your belongings you are left with {health - 30} health and {gold - gold} gold")
        print("")

    elif choice == "Run":
        print("You decide that you cant take both of them on and run away like a fucking coward.")
        print("")
        print("You find yourself safe and decide to leave for the dungeon in the morning.")
        print("")
        print("As you are walking into the forest the fog gets thicker and your vision becomes more "
        + "obscured as you continue through the fog.")
        print("")
        print("In the distance as far as you are able to see you can see two dark sillouettes on the ground motionless")

        choice1 = input("Do you approch the dark figures? (Y/N")
        if choice1 == "Y".lower():
            print("you approch the sillouettes with caution and find it is the bodies of the two adventurers you had "
            + "encountered at the tavern the previous night")
            print("you also see that their bodies were mauled by some kind of creature possibly lurking in the mist. The blood looks fresh")
            choice2 = input("check their belongings? (Y/N")
            if choice2 == "Y".lower():
                print("You find 100 gold on one of them and 120 on the other")
                print(f"You now have {gold + 100 + 120} gold")
                print("")
                print(f"you also found a weapon that deals 30 more damage than your previous weapon. {damage + 30} ")

                print("-------THIS IS THE END OF CHAPTER ONE--------")



    
