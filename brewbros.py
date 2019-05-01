# the brew brothers

# 20 june 2017
# now 30 april 2019

# by mike bruno

# inspired by phil klemmer

# borrwed from all over.  for example:
# https://github.com/jeremydosborn/lemonade_brwry
# and
# a million different google searches, which mostly lead to stackoverflow

# thank you, sincerely


import random
import os
from prettytable import PrettyTable



class brewery:

    def __init__(self):

        self.day = 0
        self.cash = 100
        self.beer = 0
        self.beer_cost = random.randrange(1, 100)
        self.weather = random.randrange(45, 110)
        # adding supplies here
        self.malt = 0
        self.malt_cost = 20
        self.hops = 0
        self.hops_cost = 10
        self.yeast = 0
        self.yeast_cost = 5


    def next_day(self):
        raw_input("Press ENTER to advance to the next day. . . ")
        os.system('clear')


    def buy_supplies(self):

        sell_table = PrettyTable([" Item ", " Cost "])
        sell_table.add_row(["Malt", "$20"])
        sell_table.add_row(["Hops", "$10"])
        sell_table.add_row(["Yeast", "$5"])
        sell_table.add_row(["Item Not", "$25"])
        sell_table.add_row(["Box of Bottles - 150ct", "$35"])
        sell_table.reversesort = True

        while True:
            try:
                print("\n\nYou need to purchase supplies in order to brew beer.\n")
                print(sell_table)

                malt = int(raw_input("\nHow many bags of malt? "))
                if malt in range(0, 10, 1):
                    break
                else:
                    print("Please choose a smaller amount. ")
                    continue
            except ValueError:
                    print("Please choose an actual number. ")
                    continue
        self.malt += malt
        self.cash -= malt * (float(self.malt_cost))

        while True:
            try:
                hops = int(raw_input("How many bags of hops? "))
                if hops in range(0, 10, 1):
                    break
                else:
                    print("Please choose a smaller amount. ")
                    continue
            except ValueError, e:
                print("Please choose an actual number. ")
                continue
        self.hops += hops
        self.cash -= hops * (float(self.hops_cost))


        while True:
            try:
                yeast = int(raw_input("How many packages of yeast? "))
                if yeast in range(0, 10, 1):
                    break
                else:
                    print("Please choose a smaller amount. ")
                    continue
            except ValueError, e:
                print("Please choose a real number. ")
                continue
        self.yeast += yeast
        self.cash -= yeast * (float(self.yeast_cost))

        self.weather = random.randrange(45, 110)

        print("Supplies successfully purchased!  Total Cost: ${0}\n".format(
            float((malt * self.malt_cost) + (hops * self.hops_cost) + (yeast * self.yeast_cost))))

        raw_input("Press ENTER to return to previous screen. . . ")
        os.system('clear')





    """
    def brew_beer(self):


    # this is selling beeerrrr!!

        while True:
            try:
                price = int(raw_input("How much will you charge for a bottle of beer? "))
                if price in range(0, 1001):
                    break
                else:
                    print("Please pick an amount amount between 1 and 1000.")
                    continue
            except ValueError, e:
                print("Please pick an amount between 1 and 1000, thank you.")
                continue

        bottles_sold = random.randrange(1, 1000)
        price_factor = float(100 - price) / 100 # was 1000 inside
        heat_factor = 1 - (((100 - self.weather) * 2) / float(100))

        if price == 0:
            self.beer = 0
            print("All of your beer sold for nothing, because you gave it all away for free!")
            self.day += 1
            self.weather = random.randrange(50, 100)
            self.beer_cost = random.randrange(1, 10)
        demand = int(round(bottles_sold * price_factor * heat_factor))
        if demand > self.beer:
            print(
                "You only have {0} bottles of beer, but there was demand for {1}".format(self.beer, demand))
            demand = self.beer
        revenue = demand * round((float(price) / 100), 2)
        self.beer -= demand
        self.cash += revenue
        self.day += 1
        self.weather = random.randrange(50, 100)
        print("You sold {0} bottles of beer and earned ${1} dollars!\n".format(demand, revenue))
        self.next_day()
    """





    def brew_beer(self):

        brew_tab = PrettyTable(["Selection Number", "Beer", "Required Ingredients"])
        brew_tab.add_row(["1", "Lager", "2 Malt, 1 Hops, 1 Yeast"])
        brew_tab.add_row(["2", "Ale", "1 Malt, 2 Hops, 1 Yeast"])
        brew_tab.add_row(["3", "IPA", "2 Malt, 3 Hops, 1 Yeast"])
        brew_tab.add_row(["4", "Hefeweizen", "2 Malt, 1 Yeast"])
        brew_tab.add_row(["5", "Stout", "3 Malt, 1 Hops, 1 Grain, 1 Yeast"])
        brew_tab.add_row(["6", "Cherry Wheat Ale", "2 Malt, 1 Hops, 1 Grain, \n1 Cherries, 1 Yeast"])
        brew_tab.add_row(["7", "Saison", "2 Malt, 1 Hops, 3 Grains, 1 Yeast"])
        brew_tab.add_row(["8 (EXIT)", "", ""])
        brew_tab.reversesort = True
        print(brew_tab)

        def lager(self):
            self.malt -= 2
            self.hops -= 1
            print('This lager recipe filled up 100 bottles. ')

        def ale(self):
            self.malt -= 1
            self.hops -= 2
            print('A yield of 100 bottles of ale! ')

        def ipa(self):
            self.malt -= 2
            self.hops -= 3
            print('100 bottles of IPA, coming right up! ')

        def hefe(self):
            self.malt -= 2
            print('This recipe filled up 100 bottle of crisp hefeweizen ')

        def stout(self):
            self.malt -= 3
            self.hops -= 1
            #self.grain -= 1
            print('100 bottle of stout.')

        def cwa(self):
            self.malt -= 2
            self.hops -= 1
            #self.grain -= 1
            #self.fruit -= 1
            print('This recipe made 100 bottles of CWA. ')

        def saison(self):
            self.malt -= 2
            self.hops -= 1
            print('This is a saison, all 100 bottles. ')
            #self.grain -= 3

        def exit(self):
            self.yeast += 1
            self.day -= 1
            self.beer -= 100
            pass
            # not sure how to skip the changes after the 'if-statement belowwwww...'

        brewing = raw_input("What would you like to brew? ")

        beers = {
        '1' : lager,
        '2' : ale,
        '3' : ipa,
        '4' : hefe,
        '5' : stout,
        '6' : cwa,
        '7' : saison,
        '8' : exit,}

        if brewing in beers:
            beers[brewing](self)

            self.beer += 100            
            self.yeast -= 1
            self.day += 1
            self.weather = random.randrange(45, 110)
            self.next_day()


    def sell_beer(self):
        while True:
            try:
                price = int(raw_input("How much will you charge for a bottle of beer? "))
                if price in range(0, 1001, 1):
                    break
                else:
                    print("Choose an amount between 1 and 1000")
                    continue
            except ValueError, e:
                print("Please pick an amount between 1 and 1000.")
                continue

# left off above!
        self.day += 1
        self.weather = random.randrange(45, 110)
        self.next_day()


    def display_data(self, name):
        if self.day == 0:
            print("\nWelcome to {0} !\n".format(name))
        print("Day: {0}".format(self.day))
        print("Weather: {0}*".format(self.weather))
        print("Cash: ${0}".format(self.cash))
        print("Bottles of Beer: {0}".format(self.beer))
        print("\n")

        print("Bags of Malt: {0}".format(self.malt))
        print("Bags of Hops: {0}".format(self.hops))
        print("Packs of Yeast: {0}".format(self.yeast))
        print("\n" + "=" * 50 + '\n')



def main():
    os.system('clear')

    choice = " "
    while choice not in ['y', 'n']:
        choice = raw_input("Create a new brewery? (y/n) ")
        if choice == 'y':
            name = raw_input("Hey there!  What is the name of your BREWERY? ")
            brwry = brewery()
            brwry.display_data(name)
            while True:
                choose = raw_input(
                "Enter 1 to buy supplies.\nEnter 2 to brew beer.\nEnter 3 to sell beer.\nEnter 4 to quit.\n> ")
                if choose == '1':
                    os.system('clear')
                    #if self.day == random.randrange(1, 3):
                        #print("You should hire a master brewer.  This is a great way to unlock new recpies.")
                    brwry.buy_supplies()
                    brwry.display_data(name)
                    continue
                elif choose == '2':
                    os.system('clear')
                    brwry.brew_beer()
                    brwry.display_data(name)
                    continue
                elif choose == '3':
                    os.system('clear')
                    brwry.sell_beer()
                    brwry.display_data(name)
                    continue
                elif choose == '4':
                    break
                else:
                    print("You must make a choice.  1 or 2 or 3 or 4. \n")
                    continue
        elif choice == 'n':
            print("Goodbye!")
            return




main()





# ------------------ TO DO LIST ------------------
# no more negatives - can't spend more than you have 
# need all ingredients to brew
# opportunities to hire workers : workers give bonuses (new recipes, etc) 
# random chances to get supplies
# supplies spoil
#
#
# ------------------ TO DO LIST ------------------

