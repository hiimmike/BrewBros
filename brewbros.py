# the brew brothers

# started on:
# 20 june 2017

# latest edit on:
# 03 may 2019

# by mike bruno

# inspired by phil klemmer

# thank you john finn.  even if you don't know already... I am going to be asking you for help  lol

# borrwed from all over.  for example:
# https://github.com/jeremydosborn/lemonade_stand
# and
# a million different google searches, which mostly lead to stackoverflow

# thank you, sincerely
# thank you Stephanie for letting me work on this, even when we should be spending time together  ;)  love you

# this is a learning experience, and an enjoyable one at that



import random
import os
from prettytable import PrettyTable
# above I have imported the modules that I will be using for this project


# nearly everything for my project is either in this class, or in the 'main' function below it.
# I am not sure that one class is necessary or appropriate...  this was based on the lemonade brewery

class brewery:
    def __init__(self):
        self.day = 0
        self.cash = 100
        self.beer = 0
        self.weather = random.randrange(45, 110)
        # adding supplies here
        self.malt = 0
        self.malt_cost = 15
        self.hops = 0
        self.hops_cost = 5
        self.yeast = 0
        self.yeast_cost = 5
# i have used the initialize function above to outline basic starting variables
# the values or amounts of the above variables will change as one plays the game...
# days will advance, your cash will fluctuate, you can set beer cost, outside temperate will change, the amount of supplies you have will change 

    def next_day(self):
        input("Press ENTER to advance to the next day. . . ")
        os.system('clear')
# after doing something, whether that is buying or selling supplies, etc., i want to advance to the next day
# also i am interested in keeping the terminal neat and clean, with only the needed information displayed

    def go_back(self):
        input("Press ENTER to return to the previous screen . . . ")
        os.system('clear')    

    def buy_supplies(self):
        sell_table = PrettyTable([" Item ", " Cost "])
        sell_table.add_row(["Malt", "$20"])
        sell_table.add_row(["Hops", "$10"])
        sell_table.add_row(["Yeast", "$5"])
        sell_table.add_row(["Item Not Found", "$25"])
        sell_table.add_row(["Box of Bottles - 150ct", "$35"])
        sell_table.reversesort = True
# using pretty table to display infomation in a neat way
# items on the left have their prices set in the init function at the beginning of the class

        while True:
            try:
                print("\n\nYou need to purchase supplies in order to brew beer.\n")
                print(sell_table)

                malt = int(input("\nHow many bags of malt? "))
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
# when buying supplies, it will first ask you to purchase malt.  as long as the input is a real number, you can purchase that amount
# eventually I would really like it to stop you from buying supplies if you have insufficient funds

        while True:
            try:
                hops = int(input("How many bags of hops? "))
                if hops in range(0, 10, 1):
                    break
                else:
                    print("Please choose a smaller amount. ")
                    continue
            except ValueError:
                print("Please choose an actual number. ")
                continue
        self.hops += hops
        self.cash -= hops * (float(self.hops_cost))
# after malt the program asks you to purchase hops (think bags of hops, and eventually different types)
# i have used 'valueerror' here, and in the other blocks of code in which it asks you to purchase supplies
# i do not know why that is necessary, but it was used the example lemonade brewery, so I am following that example...

        while True:
            try:
                yeast = int(input("How many packages of yeast? "))
                if yeast in range(0, 10, 1):
                    break
                else:
                    print("Please choose a smaller amount. ")
                    continue
            except ValueError:
                print("Please choose a real number. ")
                continue
        self.yeast += yeast
        self.cash -= yeast * (float(self.yeast_cost))
# last item i ask you to purchase is the yeast (packets)
# eventually I would like to add the ability to buy beer bottles, caps, and fruit and specialty grains, etc.

        self.weather = random.randrange(45, 110)
# setting the weather temperature.  it is a number between 45* and 110 degrees.  
# I think I am going to use the 'weather' value to determine how well the beer sells 
# warmer should equal more beer sold

        print("Supplies successfully purchased!  Total Cost: ${0}\n".format(
            float((malt * self.malt_cost) + (hops * self.hops_cost) + (yeast * self.yeast_cost))))
# the total cost is equal to the amount of malt, hops, and yeast purchased, times their respective prices

        input("Press ENTER to return to previous screen. . . ")
        os.system('clear')
# this ends the function in the brewery class, and should bring you back to the 'main' function.  which is basically the home screen


    def brew_beer(self):
        brew_tab = PrettyTable(["Selection Number", "Beer", "Required Ingredients"])
        brew_tab.add_row(["1", "Lager", "2 Malt, 1 Hops, 1 Yeast"]) # cost = 40
        brew_tab.add_row(["2", "Ale", "1 Malt, 2 Hops, 1 Yeast"]) # cost = 30
        brew_tab.add_row(["3", "IPA", "2 Malt, 3 Hops, 1 Yeast"]) # cost = 50
        brew_tab.add_row(["4", "Hefeweizen", "2 Malt, 1 Yeast"]) # cost = 35
        brew_tab.add_row(["5", "Stout", "3 Malt, 1 Hops, 1 Grain, 1 Yeast"]) # no price for grain yet
        brew_tab.add_row(["6", "Cherry Wheat Ale", "2 Malt, 1 Hops, 1 Grain, \n1 Cherries, 1 Yeast"]) # no price for gain or cherries
        brew_tab.add_row(["7", "Saison", "2 Malt, 1 Hops, 3 Grains, 1 Yeast"]) # no price for grains yet
        brew_tab.add_row(["8 (EXIT)", "", ""])
        brew_tab.reversesort = True
        print(brew_tab)
# used PrettyTable again to display the different varieties you can brew, and how many of each ingredient it will cost

        def lager(self):
            self.malt -= 2
            self.hops -= 1
            print('This lager recipe filled up 100 bottles. ')
# could this be a dictionary or a set? would that be better for all of these?

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
            #self.grain -= 1 -----> coming up in the future
            print('100 bottle of stout.')

        def cwa(self):
            self.malt -= 2
            self.hops -= 1
            #self.grain -= 1 -----> this should be coming up in the future
            #self.fruit -= 1
            print('This recipe made 100 bottles of Cherry Wheat Ale. ')

        def saison(self):
            self.malt -= 2
            self.hops -= 1
            print('This is a saison, all 100 bottles. ')
            #self.grain -= 3
# on each of the beer types above, I have used a function to remove the number of supplies it takes to brew the beer, from you inventory
# not 100% sure that setting each beer as a separate function is the best way to do this, but it is how I figured it out so far...
# as of now all recipes brew 100 bottles.  would like for this to change and/or have some spoil in the future

        #def exit(self):
            #self.yeast += 1
            #self.day -= 1
            #self.beer -= 100
            #pass
            # not sure how to skip the changes after the 'if-statement below...'
# I think i am adding the yeast and removing 100 bottles of beer because of the previously mentioned 'if-statement'...
# for some reason it's always going to remove 1 yeast and add 100 bottles, so if you exit without brewing, it needs to be balanced
# I think this is because 'key' 8 has a value of 'exit'.  and since this is found in the dictionary, it is going to follow the code block

        brewing = input("What would you like to brew? ")

        beers = {
        '1' : lager,
        '2' : ale,
        '3' : ipa,
        '4' : hefe,
        '5' : stout,
        '6' : cwa,
        '7' : saison}

        if brewing in beers:
            beers[brewing](self)
# if the answer to the 'input' question above is found in the ... dictionary? just below it, then
# the answer to 'brewing' is a key, and that matches up to some value in the dictionary, it runs that value, which is a function.  
# that function is to brew that particular beer

            self.beer += 100            
            self.yeast -= 1
            self.day += 1
            self.weather = random.randrange(45, 110)
            self.go_back()
        else:
            self.go_back()
# so when that is all done, you gain 100 bottles of brewed beer, you use 1 yeast packet, and the day advances +1, then we run the next_day function


    def sell_beer(self):
        while True:
            try:
                price = int(input("How much will you charge for a bottle of beer? (in cents [25 = $0.25 per beer]) "))
                if price in range(0, 1001, 1):
                    break
                else:
                    print("Choose an amount between 1 and 1000")
                    continue
            except ValueError:
                print("Please pick an amount between 1 and 1000.")
                continue

        bottles_sold = random.randrange(1, 101) # how many bottles could have possibly been sold, without any other factors in play
        price_factor = float(100 - price) / 100 # less demand as price goes up
        heat_factor = 1 - (((110 - self.weather)) / float(100)) # lower temp means less of a demand, removing the * 2 after self.weather

        if price == 0:
            self.beer = 0
            print("All of your beer sold for nothing, because you gave it all away for free!")
            self.day += 1
            self.weather = random.randrange(45, 110) # guess we need to reset the weather temp before advancing to the next day?
        demand = int(round(bottles_sold * price_factor * heat_factor))
        if demand > self.beer:
            print("You only have {0} bottles of beer, but there was demand for {1} bottles!".format(self.beer, demand))
            demand = self.beer
        revenue = demand * round((float(price) / 100), 2)
        self.beer -= demand
        self.cash += round(revenue, 2)
        self.day += 1
        self.weather = random.randrange(45, 110)
        print("You sold {0} bottles of beer and earned ${1} dollars!\n".format(demand, round(revenue, 2)))
        self.next_day()
# i have had instances where I sell negative bottles of beer and earn negative money(a.k.a. lose)
# and when i sell negative bottles of beer, it adds to the amount I have... positive number minus a negative is like adding that number

    def display_data(self, name):
        if self.day == 0:
            print("\nWelcome to {0} !\n".format(name))
        print("Day: {0}".format(self.day))
        print("Weather: {0}*".format(self.weather))
        print("Cash: ${0}".format(round(self.cash, 2)))
        print("Bottles of Beer: {0}".format(self.beer))
        print("\n")

        print("Bags of Malt: {0}".format(self.malt))
        print("Bags of Hops: {0}".format(self.hops))
        print("Packs of Yeast: {0}".format(self.yeast))
        print("\n" + "=" * 50 + '\n')
# all the displat data for the 'home screen'
# maybe I will remake this to a PrettyTable.  guess we will see.



def main():
    os.system('clear')

    choice = " "
    while choice not in ['y', 'n']:
        choice = input("Create a new brewery? (y/n) ")
        if choice == 'y':
            name = input("Hey there!  What is the name of your BREWERY? ")
            brwry = brewery()
            brwry.display_data(name)
            while True:
                choose = input(
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
                    brwry.brew_beer() # run method that is in the class
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
# days should not advance when you exit the purchase screen
# sometimes you can sell a negative number of bottles, which removes money from you
# need all ingredients to brew
# opportunities to hire workers : workers give bonuses (new recipes, etc) 
# random chances to get supplies
# supplies spoil
# kegs?
#
# ------------------ TO DO LIST ------------------

