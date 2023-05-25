# hamburger group project
# team 14

import random

# SYDNEY
# order class (this whole thing works :)
class Order():
    # constructor
    def __init__(self):
        self.burger_count = 0
        # calling the method and assigning the results to this variable
        self.burger_count = self.randomBurgers()

    # method that gets random count of burgers
    def randomBurgers(self):
        self.burger_count = random.randint(1,20)
        return self.burger_count
# stuff used to test to see if works
# burger object
# oBurger = Order()
# object calling the method
# oBurger.randomBurgers
# printing results
# print(oBurger.burger_count)

#HANNAH
#Create a Person class
class Person():
    #Create a constructor that defines an instance variable called customer_name
    def __init__(self):
        self.customer_name = self.randomName()
    #Create a method called randomName() that contains a list of 9 names:
    def randomName(self):
        self.asCustomers = ["Jefe", "El Guapo", "Lucky Day", "Ned Nederlander", "Dusty Bottoms", "Harry Flugleman", "Carmen", "Invisible Swordsman", "Singing Bush"]
        return random.choice(self.asCustomers)

#CAMERON
#Create the customer class, which inherits the Person class
class Customer(Person):
    #Call on the parent class
    def __init__(self):
        super().__init__()
        #Create the Order object as an instance variabe
        self.order = Order()

# variable for queue
queueCustomers =  []

# defining the dictionary variable
dictCustomers = {}

# setting all the counters to 0 
# before we start using them to keep track of how many burgers each person has bought in total
totalJefeBurgers = 0
totalElGuapoBurgers = 0
totalLuckyBurgers = 0
totalNedBurgers = 0
totalDustyBurgers = 0
totalHarryBurgers = 0
totalCarmenBurgers = 0
totalInvisibleBurgers = 0
totalSingingBurgers = 0

# queue stuff
for iCount in range (0, 100):
    # add one so that we get the full range since python goes until the last number not including it
    sName = Customer().customer_name
    # calling customer class which runs to order class and grabs burger count
    iBurgersOrdered = Customer().order.burger_count
    # we are adding out customer that is a list of attributes (ticket number and name) to our queue
    queueCustomers.append([iBurgersOrdered, sName])

    # adding the burgers ordered to the counters for each of the 9 names
    if sName == "Jefe":
        totalJefeBurgers += iBurgersOrdered
    elif sName == "El Guapo":
        totalElGuapoBurgers += iBurgersOrdered
    elif sName == "Lucky Day":
        totalLuckyBurgers += iBurgersOrdered
    elif sName == "Ned Nederlander":
        totalNedBurgers += iBurgersOrdered
    elif sName == "Dusty Bottoms":
        totalDustyBurgers += iBurgersOrdered
    elif sName == "Harry Flugleman":
        totalHarryBurgers += iBurgersOrdered
    elif sName == "Carmen":
        totalCarmenBurgers += iBurgersOrdered
    elif sName == "Invisible Swordsman":
        totalInvisibleBurgers += iBurgersOrdered
    else: 
        totalSingingBurgers += iBurgersOrdered

    #for iCount in range (0, len(queueCustomers)):
       # print(str(queueCustomers[iCount][0]) , queueCustomers[iCount][1], sep="\t")

    while len(queueCustomers) > 0:
        # gets rid of the customer at the top of the queue
        # so now customer 2 will be at the top and so on...
        queueCustomers.pop(0)


#Create the dictionary items by combining the sum total of each person's burger and the specific names
dictCustomers =  {Person().asCustomers[0]: totalJefeBurgers,
                  Person().asCustomers[1]: totalElGuapoBurgers,
                  Person().asCustomers[2]: totalLuckyBurgers,
                  Person().asCustomers[3]: totalNedBurgers,
                  Person().asCustomers[4]: totalDustyBurgers,
                  Person().asCustomers[5]: totalHarryBurgers,
                  Person().asCustomers[6]: totalCarmenBurgers,
                  Person().asCustomers[7]: totalInvisibleBurgers,
                  Person().asCustomers[8]: totalSingingBurgers}

#creates list that sorts the values in the dictionary in order from most purchased burgers to least purchased burgers
listSortedCustomers = sorted(dictCustomers.items(), key=lambda x: x[1], reverse=True) 

#creates a for loop to print the names and total burgers of each customer as stored in the sorted list
for customer in listSortedCustomers:
    print(customer[0].ljust(19) + "\t" + str(customer[1]).ljust(19))
