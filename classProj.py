# Dennis Dayan
# ClassProject.py
import time  # Imports time


class ITTeacher:  # defines IT Teacher  class
    def __init__(self, health, age, strength):
        self.health = health
        self.age = age
        self.strength = strength


class Student:  # defines Student class
    def __init__(self, health, age, strength, grade):
        self.health = health
        self.age = age
        self.strength = strength
        self.grade = grade

    def youDied(self):  # Prints out YOU DIED message when players health goes below limit
        if DennisDayan.health < 30:
            print('''

___    ___ ________  ___  ___          ________  ___  _______   ________
|\  \  /  /|\   __  \|\  \|\  \        |\   ___ \|\  \|\  ___ \ |\   ___ \
\ \  \/  / | \  \|\  \ \  \\\  \       \ \  \_|\ \ \  \ \   __/|\ \  \_|\
\ \    / / \ \  \\\  \ \  \\\  \       \ \  \ \\ \ \  \ \  \_|/_\ \  \ \\
 \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \_\\ \ \  \ \  \_|\ \ \  \_\\
__/  / /      \ \_______\ \_______\       \ \_______\ \__\ \_______\ \_______
|\___/ /        \|_______|\|_______|        \|_______|\|__|\|_______|\|_______|
\|___|/

          ''')

        if ArielleMadeam.health < 40:
            print('''

___    ___ ________  ___  ___          ________  ___  _______   ________
|\  \  /  /|\   __  \|\  \|\  \        |\   ___ \|\  \|\  ___ \ |\   ___ \
\ \  \/  / | \  \|\  \ \  \\\  \       \ \  \_|\ \ \  \ \   __/|\ \  \_|\
\ \    / / \ \  \\\  \ \  \\\  \       \ \  \ \\ \ \  \ \  \_|/_\ \  \ \\
 \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \_\\ \ \  \ \  \_|\ \ \  \_\\
__/  / /      \ \_______\ \_______\       \ \_______\ \__\ \_______\ \_______
|\___/ /        \|_______|\|_______|        \|_______|\|__|\|_______|\|_______|
\|___|/

          ''')
        if LukeChrampanis.health < 50:
            print('''

___    ___ ________  ___  ___          ________  ___  _______   ________
|\  \  /  /|\   __  \|\  \|\  \        |\   ___ \|\  \|\  ___ \ |\   ___ \
\ \  \/  / | \  \|\  \ \  \\\  \       \ \  \_|\ \ \  \ \   __/|\ \  \_|\ \
\ \    / / \ \  \\\  \ \  \\\  \       \ \  \ \\ \ \  \ \  \_|/_\ \  \ \\
 \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \_\\ \ \  \ \  \_|\ \ \  \_\\
__/  / /      \ \_______\ \_______\       \ \_______\ \__\ \_______\ \_______
|\___/ /        \|_______|\|_______|        \|_______|\|__|\|_______|\|_______|
\|___|/

          ''')
        if Murph.health < 55:
            print('''

___    ___ ________  ___  ___          ________  ___  _______   ________
|\  \  /  /|\   __  \|\  \|\  \        |\   ___ \|\  \|\  ___ \ |\   ___ \
\ \  \/  / | \  \|\  \ \  \\\  \       \ \  \_|\ \ \  \ \   __/|\ \  \_|\
\ \    / / \ \  \\\  \ \  \\\  \       \ \  \ \\ \ \  \ \  \_|/_\ \  \ \\
 \/  /  /   \ \  \\\  \ \  \\\  \       \ \  \_\\ \ \  \ \  \_|\ \ \  \_\\
__/  / /      \ \_______\ \_______\       \ \_______\ \__\ \_______\ \_______
|\___/ /        \|_______|\|_______|        \|_______|\|__|\|_______|\|_______|
\|___|/

          ''')

    def watsonfightenter(self):  # defines Mr. Watsons room level
        print('YOU SEE CHRISTOPHER WATSON WITH A BASKETBALL')
        print('---------------------------{}')
        print('CHRISTOPHER WASTON:  HELLO DENNIS, PREPARE TO MEET THY WRATH')
        print('WHAT WILL YOU DO?(Fight, Run)')
        gameinp = (input('ENTER YOUR SELECTION:'))  # user input within
        if gameinp == 'fight' or gameinp == 'Fight':
            print("MR WATSON LIGHTLY HITS YOU WITH A BASKETBALL")
            DennisDayan.health -= 30  # takes off 30 health
            Student.youDied(Student)  # refers back to youDied
        if gameinp == 'Run' or gameinp == 'run':
            Student.watsonrun(Student)  # Goes to next level sequence if user chooses

    def walkbywatson(self):  # bonus mr wilkins level if student walks away from wastons room
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")

    def watsonrun(self):  # When user chooses to run from watson
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")
        DennisDayan.health += 10 and DennisDayan.strength + 2  # buffs character health 10 and strength 2
        print("YOUR HEALTH INCREASED BY 10 AND STRENGTH BY 2")
        print("THANKS MR. WILKINS!")
        Student.milofight(Student)  # jumps to boss fight

    def milofight(self):  # final boss fight with Mr. Milonas
        print('-----------------------------------------------------------------------------------------{}')
        print("YOU SEE A DARK AND LONG-CLOSED ROOM WITH A MYSTERIOUS FIGURE IN IT ")
        time.sleep(1.5)  # gives boss fight a dramatic effect, with lines being delayed when printed
        print("MYSTERIOUS FIGURE: IS THAT A KNIGHT I SEE?")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: IF SO, YOU SURELY WILL BE CRUSHED!")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: FOR I AM THE IRON MILO, THE EVENTUAL CRUSHER OF THE KNIGHTS OF DARWINIAN SILK")
        time.sleep(1.5)
        print("IRON MILO: GOOD LUCK EVADING ME FOR I HAVE CLOSED ALL THE EXITS!")
        time.sleep(1.5)
        print("YOU HAVE NO ESCAPE!")
        time.sleep(1.5)
        print("THE IRON MILO USED TUESDAY CYBERPATRIOT PRACTICE")
        import random  # imports random
        x = random.randint(0, 100)  # sets x to random number 0, 100
        if x > 50:  # if the random number is above 50
            DennisDayan.health -= 15  # Decreases Dennis health by 15
        else:
            DennisDayan.health -= 10000000  # If the number is below 50, Mr Milonas automatically destroys student
            Student.youDied(Student)
            sys.exit(0)  # graceful exit
        print("AAHHHH, MY ARM!")
        print("ATTACK? (attack)")
        miloinp = (input('ENTER YOUR SELECTION'))
        if miloinp == 'attack' or miloinp == 'Attack':
            if x > 25:  # if x is above 25
                JeremiahMilonas.health -= 15  # takes off 15 health
            if x < 75:  # if x is below 75
                JeremiahMilonas.health -= 30  # takes off 30 health
            if x == 13:  # if x equals 13, lucky number
                JeremiahMilonas.health -= 50  # takes off 50 health
            print("IRON MILO: YOUR ATTACK DID NEXT TO NOTHING, YOU PATHETIC KNIGHT!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: NOT SO FAST, JEREMIAH!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: FOR IT IS I, ADAS IRWIN LINK!")
            time.sleep(1.5)
            print(
                "ADAS IRWIN LINK: INITIATE MORPHING SEQUENCE!")  # MR WILKINS IS ABOUT TO DESTROY MR. MILONAS WITH FACTS AND LOGIC(not really)
            time.sleep(1.5)
            AdrianWilkins.health += 999999999  # Gives Mr. Wilkins almost infinite health
            AdrianWilkins.strength += 9999999999  # Gives Mr. Wilkins almost infinite strength
            AdrianWilkins.age -= 10  # Takes off 10 years from Mr. Wilkins
            print("IRON MILO: IMPOSSIBLE, YOUR STRENGTH CANNOT BE {}!".format(AdrianWilkins.strength))
            time.sleep(1.5)
            print("ADAS IRWIN LINK: MY STATS ARE EXTREME, AS IS MY DESIRE TO DESTROY YOU!")
            time.sleep(1.5)
            print("IRON MILO: NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK USED SOUL DECIMATOR")
            print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!")
            time.sleep(1.5)
            JeremiahMilonas.strength -= 99999999  # DECIMATES MR MILONAS STRENGTH
            JeremiahMilonas.health -= 99999999  # DECIMATES MR MILONAS HEALTH
            JeremiahMilonas.age = 0  # Sets age to 0
            print(
                "ADAS IRWIN LINK: MY HUMBLE KNIGHT AND STUDENT, THANK YOU FOR DEFENDING THESE SACRED WALLS. MY KNIGHT, HEAL.")
            DennisDayan.health += 100  # Sets user health to 100
            DennisDayan.strength += 99  # Sets user strength to 1 99
            print("YOU: I FEEL AMAZING!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK: YES MY KNIGHT, YOU SHALL FEEL INVIGORATED WITH STRENGTH AND HEALTH")
            time.sleep(1.5)
            print(
                "ADAS IRWIN LINK: MY KNIGHT, I MUST GO. I CANNOT ROAM THESE HALLS AS FOR THE SIGHT OF MY RAW POWER TO A FRESHMAN WOULD SURELY DECIMATE THEM.")
            time.sleep(1.5)
            print("ADAS IRWIN LINK VANISHED IN A LIGHT CLOUD")
            time.sleep(1.5)
            print('''


    ____  ____  ____  ____  ____  ____  _________  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____
   ||T ||||h ||||a ||||n ||||k ||||s ||||       ||||f ||||o ||||r ||||       ||||P ||||l ||||a ||||y ||||i ||||n ||||g ||||! ||
   ||__||||__||||__||||__||||__||||__||||_______||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||
   |/__\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|


   BE SURE TO CHECK OUT OUR OTHER OFFERINGS {}!








           ''')
            sys.exit(0)  # graceful exit
        else:
            print("INVALID INPUT, EXITING!")
            sys.exit(0)  # error detection

    def watsonfightenter2(
            self):  # SEE ABOVE wastonfightenter, walkbywatson, watsonrun, milofight comments, as this segment is duplicated.
        print('YOU SEE CHRISTOPHER WATSON WITH A BASKETBALL')
        print('---------------------------{}')
        print('CHRISTOPHER WASTON:  HELLO STUDENT, PREPARE TO MEET THY WRATH')
        print('WHAT WILL YOU DO?(Fight, Run)')
        gameinp = (input('ENTER YOUR SELECTION:'))
        if gameinp == 'fight' or gameinp == 'Fight':
            print("MR WATSON LIGHTLY HITS YOU WITH A BASKETBALL")
            ArielleMadeam.health -= 30
            Student.youDied(Student)
        if gameinp == 'Run' or gameinp == 'run':
            Student.watsonrun2(Student)

    def walkbywatson2(self):
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")

    def watsonrun2(self):
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")
        ArielleMadeam.health += 10 and ArielleMadeam.strength + 2
        print("YOUR HEALTH INCREASED BY 10 AND STRENGTH BY 2")
        print("THANKS MR. WILKINS!")
        Student.milofight2(Student)

    def milofight2(self):
        print('-----------------------------------------------------------------------------------------{}')
        print("YOU SEE A DARK AND LONG-CLOSED ROOM WITH A MYSTERIOUS FIGURE IN IT ")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: IS THAT A KNIGHT I SEE?")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: IF SO, YOU SURELY WILL BE CRUSHED!")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: FOR I AM THE IRON MILO, THE EVENTUAL CRUSHER OF THE KNIGHTS OF DARWINIAN SILK")
        time.sleep(1.5)
        print("IRON MILO: GOOD LUCK EVADING ME FOR I HAVE CLOSED ALL THE EXITS!")
        time.sleep(1.5)
        print("YOU HAVE NO ESCAPE!")
        time.sleep(1.5)
        print("THE IRON MILO USED TUESDAY CYBERPATRIOT PRACTICE")
        import random
        x = random.randint(0, 100)
        if x > 50:
            ArielleMadeam.health -= 15
        else:
            ArielleMadeam.health -= 10000000
            Student.youDied(Student)
            sys.exit(0)
        print("AAHHHH, MY ARM!")
        print("ATTACK? (attack)")
        miloinp = (input('ENTER YOUR SELECTION'))
        if miloinp == 'attack' or miloinp == 'Attack':
            if x > 25:
                JeremiahMilonas.health -= 15
            if x < 75:
                JeremiahMilonas.health -= 30
            if x == 13:
                JeremiahMilonas.health -= 50
            print("IRON MILO: YOUR ATTACK DID NEXT TO NOTHING, YOU PATHETIC KNIGHT!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: NOT SO FAST, JEREMIAH!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: FOR IT IS I, ADAS IRWIN LINK!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK: INITIATE MORPHING SEQUENCE!")
            time.sleep(1.5)
            AdrianWilkins.health += 999999999
            AdrianWilkins.strength += 9999999999
            AdrianWilkins.age -= 10
            print("IRON MILO: IMPOSSIBLE, YOUR STRENGTH CANNOT BE {}!".format(AdrianWilkins.strength))
            time.sleep(1.5)
            print("ADAS IRWIN LINK: MY STATS ARE EXTREME, AS IS MY DESIRE TO DESTROY YOU!")
            time.sleep(1.5)
            print("IRON MILO: NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK USED SOUL DECIMATOR")
            print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!")
            time.sleep(1.5)
            JeremiahMilonas.strength -= 99999999
            JeremiahMilonas.health -= 99999999
            JeremiahMilonas.age = 0
            print(
                "ADAS IRWIN LINK: MY HUMBLE KNIGHT AND STUDENT, THANK YOU FOR DEFENDING THESE SACRED WALLS. MY KNIGHT, HEAL.")
            ArielleMadeam.health += 100
            ArielleMadeam.strength += 99
            print("YOU: I FEEL AMAZING!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK: YES MY KNIGHT, YOU SHALL FEEL INVIGORATED WITH STRENGTH AND HEALTH")
            time.sleep(1.5)
            print(
                "ADAS IRWIN LINK: MY KNIGHT, I MUST GO. I CANNOT ROAM THESE HALLS AS FOR THE SIGHT OF MY RAW POWER TO A FRESHMAN WOULD SURELY DECIMATE THEM.")
            time.sleep(1.5)
            print("ADAS IRWIN LINK VANISHED IN A LIGHT CLOUD")
            time.sleep(1.5)
            print('''


       ____  ____  ____  ____  ____  ____  _________  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____
      ||T ||||h ||||a ||||n ||||k ||||s ||||       ||||f ||||o ||||r ||||       ||||P ||||l ||||a ||||y ||||i ||||n ||||g ||||! ||
      ||__||||__||||__||||__||||__||||__||||_______||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||
      |/__\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|


      BE SURE TO CHECK OUT OUR OTHER OFFERINGS {}!








              ''')
            sys.exit(0)
        else:
            print("INVALID INPUT, EXITING!")
            sys.exit(0)

    def watsonfightenter3(
            self):  # SEE ABOVE wastonfightenter, walkbywatson, watsonrun, milofight comments, as this segment is duplicated.
        print('YOU SEE CHRISTOPHER WATSON WITH A BASKETBALL')
        print('---------------------------{}')
        print('CHRISTOPHER WASTON:  HELLO STUDENT, PREPARE TO MEET THY WRATH')
        print('WHAT WILL YOU DO?(Fight, Run)')
        gameinp = (input('ENTER YOUR SELECTION:'))
        if gameinp == 'fight' or gameinp == 'Fight':
            print("MR WATSON LIGHTLY HITS YOU WITH A BASKETBALL")
            LukeChrampanis.health -= 30
            Student.youDied(Student)
        if gameinp == 'Run' or gameinp == 'run':
            Student.watsonrun3(Student)

    def walkbywatson3(self):
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")

    def watsonrun3(self):
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")
        LukeChrampanis.health += 10 and LukeChrampanis.strength + 2
        print("YOUR HEALTH INCREASED BY 10 AND STRENGTH BY 2")
        print("THANKS MR. WILKINS!")
        Student.milofight3(Student)

    def milofight3(self):
        print('-----------------------------------------------------------------------------------------{}')
        print("YOU SEE A DARK AND LONG-CLOSED ROOM WITH A MYSTERIOUS FIGURE IN IT ")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: IS THAT A KNIGHT I SEE?")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: IF SO, YOU SURELY WILL BE CRUSHED!")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: FOR I AM THE IRON MILO, THE EVENTUAL CRUSHER OF THE KNIGHTS OF DARWINIAN SILK")
        time.sleep(1.5)
        print("IRON MILO: GOOD LUCK EVADING ME FOR I HAVE CLOSED ALL THE EXITS!")
        time.sleep(1.5)
        print("YOU HAVE NO ESCAPE!")
        time.sleep(1.5)
        print("THE IRON MILO USED TUESDAY CYBERPATRIOT PRACTICE")
        import random
        x = random.randint(0, 100)
        if x > 50:
            LukeChrampanis.health -= 15
        else:
            LukeChrampanis.health -= 10000000
            Student.youDied(Student)
            sys.exit(0)
        print("AAHHHH, MY ARM!")
        print("ATTACK? (attack)")
        miloinp = (input('ENTER YOUR SELECTION'))
        if miloinp == 'attack' or miloinp == 'Attack':
            if x > 25:
                JeremiahMilonas.health -= 15
            if x < 75:
                JeremiahMilonas.health -= 30
            if x == 13:
                JeremiahMilonas.health -= 50
            print("IRON MILO: YOUR ATTACK DID NEXT TO NOTHING, YOU PATHETIC KNIGHT!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: NOT SO FAST, JEREMIAH!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: FOR IT IS I, ADAS IRWIN LINK!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK: INITIATE MORPHING SEQUENCE!")
            time.sleep(1.5)
            AdrianWilkins.health += 999999999
            AdrianWilkins.strength += 9999999999
            AdrianWilkins.age -= 10
            print("IRON MILO: IMPOSSIBLE, YOUR STRENGTH CANNOT BE {}!".format(AdrianWilkins.strength))
            time.sleep(1.5)
            print("ADAS IRWIN LINK: MY STATS ARE EXTREME, AS IS MY DESIRE TO DESTROY YOU!")
            time.sleep(1.5)
            print("IRON MILO: NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK USED SOUL DECIMATOR")
            print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!")
            time.sleep(1.5)
            JeremiahMilonas.strength -= 99999999
            JeremiahMilonas.health -= 99999999
            JeremiahMilonas.age = 0
            print(
                "ADAS IRWIN LINK: MY HUMBLE KNIGHT AND STUDENT, THANK YOU FOR DEFENDING THESE SACRED WALLS. MY KNIGHT, HEAL.")
            LukeChrampanis.health += 100
            LukeChrampanis.strength += 99
            print("YOU: I FEEL AMAZING!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK: YES MY KNIGHT, YOU SHALL FEEL INVIGORATED WITH STRENGTH AND HEALTH")
            time.sleep(1.5)
            print(
                "ADAS IRWIN LINK: MY KNIGHT, I MUST GO. I CANNOT ROAM THESE HALLS AS FOR THE SIGHT OF MY RAW POWER TO A FRESHMAN WOULD SURELY DECIMATE THEM.")
            time.sleep(1.5)
            print("ADAS IRWIN LINK VANISHED IN A LIGHT CLOUD")
            time.sleep(1.5)
            print('''


       ____  ____  ____  ____  ____  ____  _________  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____
      ||T ||||h ||||a ||||n ||||k ||||s ||||       ||||f ||||o ||||r ||||       ||||P ||||l ||||a ||||y ||||i ||||n ||||g ||||! ||
      ||__||||__||||__||||__||||__||||__||||_______||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||
      |/__\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|


      BE SURE TO CHECK OUT OUR OTHER OFFERINGS {}!








              ''')
            sys.exit(0)
        else:
            print("INVALID INPUT, EXITING!")
            sys.exit(0)

    def watsonfightenter4(
            self):  # SEE ABOVE wastonfightenter, walkbywatson, watsonrun, milofight comments, as this segment is duplicated.
        print('YOU SEE CHRISTOPHER WATSON WITH A BASKETBALL')
        print('---------------------------{}')
        print('CHRISTOPHER WASTON:  HELLO STUDENT, PREPARE TO MEET THY WRATH')
        print('WHAT WILL YOU DO?(Fight, Run)')
        gameinp = (input('ENTER YOUR SELECTION:'))
        if gameinp == 'fight' or gameinp == 'Fight':
            print("MR WATSON LIGHTLY HITS YOU WITH A BASKETBALL")
            Murph.health -= 30
            Student.youDied(Student)
        if gameinp == 'Run' or gameinp == 'run':
            Student.watsonrun4(Student)

    def walkbywatson4(self):
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")

    def watsonrun4(self):
        print("YOU SEE ADRIAN WILKINS IN HIS ROOM")
        print("ADRIAN WILKINS: AH, MY FAVORITE STUDENT! WHAT DO YOU NEED?")
        print("ADRIAN WILKINS: HERE, HAVE A HEALTH PACK!")
        Murph.health += 10 and Murph.strength + 2
        print("YOUR HEALTH INCREASED BY 10 AND STRENGTH BY 2")
        print("THANKS MR. WILKINS!")
        Student.milofight4(Student)

    def milofight4(self):
        print('-----------------------------------------------------------------------------------------{}')
        print("YOU SEE A DARK AND LONG-CLOSED ROOM WITH A MYSTERIOUS FIGURE IN IT ")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: IS THAT A KNIGHT I SEE?")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: IF SO, YOU SURELY WILL BE CRUSHED!")
        time.sleep(1.5)
        print("MYSTERIOUS FIGURE: FOR I AM THE IRON MILO, THE EVENTUAL CRUSHER OF THE KNIGHTS OF DARWINIAN SILK")
        time.sleep(1.5)
        print("IRON MILO: GOOD LUCK EVADING ME FOR I HAVE CLOSED ALL THE EXITS!")
        time.sleep(1.5)
        print("YOU HAVE NO ESCAPE!")
        time.sleep(1.5)
        print("THE IRON MILO USED TUESDAY CYBERPATRIOT PRACTICE")
        import random
        x = random.randint(0, 100)
        if x > 50:
            Murph.health -= 15
        else:
            Murph.health -= 10000000
            Student.youDied(Student)
            sys.exit(0)
        print("AAHHHH, MY ARM!")
        print("ATTACK? (attack)")
        miloinp = (input('ENTER YOUR SELECTION'))
        if miloinp == 'attack' or miloinp == 'Attack':
            if x > 25:
                JeremiahMilonas.health -= 15
            if x < 75:
                JeremiahMilonas.health -= 30
            if x == 13:
                JeremiahMilonas.health -= 50
            print("IRON MILO: YOUR ATTACK DID NEXT TO NOTHING, YOU PATHETIC KNIGHT!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: NOT SO FAST, JEREMIAH!")
            time.sleep(1.5)
            print("ADRIAN WILKINS: FOR IT IS I, ADAS IRWIN LINK!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK: INITIATE MORPHING SEQUENCE!")
            time.sleep(1.5)
            AdrianWilkins.health += 999999999
            AdrianWilkins.strength += 9999999999
            AdrianWilkins.age -= 10
            print("IRON MILO: IMPOSSIBLE, YOUR STRENGTH CANNOT BE {}!".format(AdrianWilkins.strength))
            time.sleep(1.5)
            print("ADAS IRWIN LINK: MY STATS ARE EXTREME, AS IS MY DESIRE TO DESTROY YOU!")
            time.sleep(1.5)
            print("IRON MILO: NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK USED SOUL DECIMATOR")
            print("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!")
            time.sleep(1.5)
            JeremiahMilonas.strength -= 99999999
            JeremiahMilonas.health -= 99999999
            JeremiahMilonas.age = 0
            print(
                "ADAS IRWIN LINK: MY HUMBLE KNIGHT AND STUDENT, THANK YOU FOR DEFENDING THESE SACRED WALLS. MY KNIGHT, HEAL.")
            Murph.health += 100
            Murph.strength += 99
            print("YOU: I FEEL AMAZING!")
            time.sleep(1.5)
            print("ADAS IRWIN LINK: YES MY KNIGHT, YOU SHALL FEEL INVIGORATED WITH STRENGTH AND HEALTH")
            time.sleep(1.5)
            print(
                "ADAS IRWIN LINK: MY KNIGHT, I MUST GO. I CANNOT ROAM THESE HALLS AS FOR THE SIGHT OF MY RAW POWER TO A FRESHMAN WOULD SURELY DECIMATE THEM.")
            time.sleep(1.5)
            print("ADAS IRWIN LINK VANISHED IN A LIGHT CLOUD")
            time.sleep(1.5)
            print('''


       ____  ____  ____  ____  ____  ____  _________  ____  ____  ____  _________  ____  ____  ____  ____  ____  ____  ____  ____
      ||T ||||h ||||a ||||n ||||k ||||s ||||       ||||f ||||o ||||r ||||       ||||P ||||l ||||a ||||y ||||i ||||n ||||g ||||! ||
      ||__||||__||||__||||__||||__||||__||||_______||||__||||__||||__||||_______||||__||||__||||__||||__||||__||||__||||__||||__||
      |/__\||/__\||/__\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/_______\||/__\||/__\||/__\||/__\||/__\||/__\||/__\||/__\|


      BE SURE TO CHECK OUT OUR OTHER OFFERINGS {}!








              ''')
            sys.exit(0)
        else:
            print("INVALID INPUT, EXITING!")
            sys.exit(0)

    def play(self):  # Actual game and player selection
        print('WELCOME PLAYER. CHOOSE A CHARACTER,')  # prompts user to choose a character
        print('''
      1: Dennis Dayan
      Health: 30
      Age: 16
      Strength: 2
      Grade: 10
      2: Arielle Madeam
      Health: 40
      Age: 15
      Strength: 5
      Grade: 10
      3: Luke Chrampanis
      Health: 50
      Age: 16
      Strength: 7
      Grade: 10
      4: Murph
      Health: 55
      Age: 15
      Strength: 4
      Grade: 10
      ''')
        chrslctinp = int(input('Choose a Character(number)'))  # char input
        if chrslctinp == 1:  # Picked character corresponding to number
            print('YOU PICKED DENNIS DAYAN!')
            print('YOU ARE WALKING IN THE HALLS AND YOU SEE A DARK AND OPEN ROOM. WHAT WILL YOU DO?(Enter, Walk By')
            gameinp = (input('ENTER YOUR SELECTION: '))  # Game input, different then char input
            if gameinp == 'Enter' or gameinp == 'enter':
                Student.watsonfightenter(Student)  # Starts wastonfightenter level
            if gameinp == 'Walk by' or gameinp == 'walk by':
                Student.walkbywatson(Student)  # Starts walkbywatson level
                Student.milofight(Student)  # Starts milofight level
        if chrslctinp == 2:  # CODE STATEMENT DUPLICATED, SEE COMMENTS ABOVE
            print('YOU PICKED ARIELLE MADEAM')
            print('YOU ARE WALKING IN THE HALLS AND YOU SEE A DARK AND OPEN ROOM. WHAT WILL YOU DO?(Enter, Walk By')
            gameinp = (input('ENTER YOUR SELECTION: '))
            if gameinp == 'Enter' or gameinp == 'enter':
                Student.watsonfightenter2(Student)
            if gameinp == 'Walk by' or gameinp == 'walk by':
                Student.walkbywatson2(Student)
                Student.milofight2(Student)
        if chrslctinp == 3:  # CODE STATEMENT DUPLICATED, SEE COMMENTS ABOVE
            print('YOU PICKED LUKE CHRAMPANIS')
            print('YOU ARE WALKING IN THE HALLS AND YOU SEE A DARK AND OPEN ROOM. WHAT WILL YOU DO?(Enter, Walk By')
            gameinp = (input('ENTER YOUR SELECTION: '))
            if gameinp == 'Enter' or gameinp == 'enter':
                Student.watsonfightenter3(Student)
            if gameinp == 'Walk by' or gameinp == 'walk by':
                Student.walkbywatson3(Student)
                Student.milofight3(Student)
        if chrslctinp == 4:  # CODE STATEMENT DUPLICATED, SEE COMMENTS ABOVE
            print('YOU PICKED MURPH(my man)')
            print('YOU ARE WALKING IN THE HALLS AND YOU SEE A DARK AND OPEN ROOM. WHAT WILL YOU DO?(Enter, Walk By')
            gameinp = (input('ENTER YOUR SELECTION: '))
            if gameinp == 'Enter' or gameinp == 'enter':
                Student.watsonfightenter4(Student)
            if gameinp == 'Walk by' or gameinp == 'walk by':
                Student.walkbywatson4(Student)
                Student.milofight4(Student)


ChristopherWatson = ITTeacher(58, 29, 5)  # Defines Christopher Watson
AdrianWilkins = ITTeacher(64, 36, 10)  # Defines Adrian Wilkins
JeremiahMilonas = ITTeacher(100, 46, 15)  # Defines Jeremiah Milonas

DennisDayan = Student(30, 16, 2, 11)  # Defines Dennis Dayan
ArielleMadeam = Student(40, 15, 5, 11)  # Defines Arielle Madeam
LukeChrampanis = Student(50, 16, 7, 11)  # Defines Luke Chrampanis
Murph = Student(55, 15, 4, 11)  # Defines Murph

print('WELCOME TO ANOTHER, ')
print('''

 ,._., ._                                   ,.-:~:-.                                         _   ‘             ,.-:~:-.                     .:':'`:·          ,:´'`;' ‘
/::::::::::'/:/:~-.,                       /':::::::::'`,                .·:¯:`/';            /::/'; ‘           /':::::::::'`,                 /:::::::/`·,      /::::/;‘
/:-·:;:-·~·';/:::::::::`·-.               /;:-·~·-:;':::',              /:::::/:::\          /::/: ';          /;:-·~·-:;':::',               /:·*'`·:/:::::' , /·´'`;/::';'
';           '`~-:;:::::::::'`,          ,'´          '`:;::`,           /·´¯'`·;::::\      ,·´¯'`;::/        ,'´          '`:;::`,           ,'         `:;::::'`i    ';:::';
',.                 '`·-:;:::::'i'‘      /                `;::\         ;         \:::/`:, .'      ';/'        /                `;::\          ;            '`;:::'i    'i::::i
  `'i      ,_            '`;:::'¦‘    ,'                   '`,::;       ';          \/::::,'    '   /        ,'                   '`,::;        i               `;:';    'i:::i'
   'i      ;::/`:,          i'::/    i'       ,';´'`;         '\:::', ‘    \          `'·:,:'´      /'        i'       ,';´'`;         '\:::', ‘    i      ,          \|     '|:::i°
  _;     ;:/;;;;:';        ¦'/    ,'        ;' /´:`';         ';:::'i‘     '`,                  ,'´'       ,'        ;' /´:`';         ';:::'i‘    |     ,'`,                i:;'' ‚
 /::';   ,':/::::::;'       ,´     ;        ;/:;::;:';         ',:::;        `,             ,'´:'*:^;    ;        ;/:;::;:';         ',:::;    'i    'i:::i',             ';/'
,/-:;_i  ,'/::::;·´        ,'´     'i        '´        `'         'i::'/         `;         ,/::::::::/'   'i        '´        `'         'i::'/    'i     ;::/ \           ;/'
'`·.     `'¯¯     '   , ·'´        ¦       '/`' *^~-·'´\         ';'/'‚        ,·'         '¯ '`*^;:/‘    ¦       '/`' *^~-·'´\         ';'/'‚     \    'i/    '`·,      ,''
  `' ~·- .,. -·~ ´             '`., .·´              `·.,_,.·´  ‚       ';                 ,'/'      '`., .·´              `·.,_,.·´  ‚      '`~´         '`·–·'´'
         '                                                                 '`*^~·–-·~^*'´‘                                                                   ‘
                __  '                      ,.-:^*:*:^:~,'                      _               °          ,.-~·-.,__,.-::^·- .,'   ‘
          ,·:'´/::::/'`;·.,              ,:´:::::::::::::::/_‚          ,·~:-·´::/:`:;_.-~^*/'^;         /:::::::::::::::::::::::::/'; '
      .:´::::/::::/:::::::`;           /::;:-·^*'*'^~-;:/::/`;   '    /::::::_:/::::::::::::/:::'i       /;:·–– :;:::::_ ;: – .,/::;i'‘
     /:;:· '´ ¯¯'`^·-;::::/' ‘        /:´    ,. –.,_,.'´::/:::';' '  /·~-·´     `:;_,:·-~^*'`^:;      /´          ¯¯           ';::/
    /·´           _   '`;/‘        ,/    ,:´';         ;'´¯`,:::'i'  'i                            i/    ,:                          ,:/
   'i            ;::::'`;*       ' ,'     ';:::`,       ,:     ';::i‘   `·,                     ,.·´      ';_,..–-.,_     _    _,.·´‘
    `;           '`;:::::'`:,     ;      ';:::/:`::^*:´;      i::';'‘     `;         ,-·~:^*'´/;                 ,·´'    '`·;'i¯
      `·,           '`·;:::::';   i       `;/::::::::,·´      ';:/'‘       ';        ;-· ~·-;/:/'                 i         'i:i'       ’
    ,~:-'`·,           `:;::/'   ';         '` *^*'´         .'/‘         ';       ,.,      ,'/                   ';        ';:i'     ’
   /:::::::::';           ';/      '\                         /            ;      ';:/`'*'*´                       i        i:/'
 ,:~·- . -·'´          ,'´          `·,                ,-·´ '             ';     ;/'                               ;      i/    °
 '`·,               , ·'´               '`*~·––·~^'´  '                  \    /                                  \   '/'
      '`*^·–·^*'´'           ‘              '                                `'´             '                        ¯               °


''')
print('PRODUCTION')


# above is ascii art user sees upon starting the game

def userName():  # Nearly useless userName function, but cool nonetheless.
    username = str(input('Enter Your Name'))
    print('Thank you for registering {}!'.format(username))


userName()

import sys  # Below code snippet was found on StackOverflow by user John Vorcak
from time import sleep

words = "WELCOME  TO THE KNIGHTS OF DARWINIAN SILK,         "
for char in words:
    sleep(0.2)  # Prints individual character in a string
    sys.stdout.write(char)
    sys.stdout.flush()  # End of cited code snippet


def welcomeScreen():  # welcome screen function
    print('CHOOSE AN OPTION\n')
    print('''
  1: START
  2: LEARN ABOUT THE KNIGHTS OF DARWININAN SILK
  3: QUIT
  ''')
    wsusinput = int(input(''))
    running = True  # sets running to true
    while running:
        if wsusinput == 1:  # if user selects start
            Student.play(Student)  # Starts the game, (play)
            break
        if wsusinput == 2:  # Provides user the story
            print('''


          The Knights of Darwinian Silk is an ancient order founded on the current grounds of Red Bank Regional High School. They follow the
           words and teachings of the mysterious figure Adas Irwin Link who started the order in MCMXCIX AD. Not much is known about the order other than the fact that
           they are under attack by an ominous figure that is yet to be seen. It is now your quest to play as one of these such followers and finally destroy that evil spirit
           for all of our eternity.
''')
            wsusinput2 = str(input('Would you like to start? (Y/N)'))
            if wsusinput2 == 'Y' or 'y':  # Starts the game
                Student.play(Student)
                break  # breaks out of loop
            elif wsusinput2 == 'N' or 'n':
                print('INCORRECT, STARTING GAME')  # Who wouldn't want to play my game?
                Student.play(Student)
                break
        if wsusinput == 3:  # if user selects exit
            import sys
            sys.exit(0)  # Graceful exits


welcomeScreen()




