import appJar
import random


def randomnum():
    if random.random() < 0.85:
        return 0
    elif random.random() < 0.9:
        return 1
    elif random.random() < 0.95:
        return 2
    elif random.random() < 1.0:
        return 3


# Character Initialization!

# Character Names
fbnames = ["Donald", "James", "Max", "Steve", "Olly", "Jack", "Harry", "George", "Jacob", "Charlie", "Noah", "William", "Leo", "Alfie", "Henry", "Josh", "Freddie", "Archie", "Ethan", "Alex", "Joe", "Sam", "Max", "Logan", "Lucas", "Daniel", "Theo", "Arthur", "Adam", "Dylan", "Ruben", "Jake", "Luca", "Matthew", "Harvey", "Luke"]
fgnames = ["Charlotte", "Lucy", "Fiona", "Ellie", "Olivia", "Amelia", "Emily", "Isla", "Isabella", "Isabel", "Lily", "Jessica", "Ella", "Mia", "Sophia", "Sophie", "Poppy", "Grace", "Evie", "Alice", "Freya", "Florence", "Daisy", "Chloe", "Phoebe", "Tilly", "Ruby", "Sienna", "Sofia", "Eva", "Elsie", "Willow", "Millie", "Esme", "Rosie"]
lnames = ["Richardson", "Trump", "McCarthy", "Johnston", "Terry", "Smith", "Jones", "Williams", "Taylor", "Davies", "Brown", "Wilson", "Evans", "Thomas", "Johnson", "Roberts", "Walker", "Wright", "Robinson", "Thompson", "White", "Hughes", "Edwards", "Green", "Lewis", "Wood", "Harris", "Martin", "Jackson", "Clarke"]
msex = ["Male", "Gay Male", "Transgender Boy", "Pansexual", "Bisexual"]
fsex = ["Female", "Lesbian Female", "Transgender Girl", "Pansexual", "Bisexual"]
country = ["United Kingdom", "United States of America", "Spain", "North Korea", "South Korea", "Japan", "Wales", "France", "Germany", "Canada", "Ireland", "Mexico", "Brazil", "China", "India", "Russia"]


# Parents Setup
mum = fgnames[random.randint(0, len(fgnames) - 1)] + " "
dad = fbnames[random.randint(0, len(fbnames) - 1)] + " " 

#Classes

# Colour 
class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Character Boilerplate
class Character(object):
    def __init__(self):
        self.dead = False
        self.canHouse = False
        self.canDrive = False
        self.canDrink = False
        self.hasKids = False
        self.kids = []
        self.money = 0
        self.age = 0
        self.country = country[random.randint(0, len(country) - 1)]

        genselect = random.randint(0, 1)
        if genselect == 0:
            gender = "male"
        else:
            gender = "female"
        self.gender = gender
        if gender == "male":
            sexrandom = random.randint(0,300)
            if sexrandom < 20:
                sexselect = 1
            elif sexrandom < 30:
                sexselect = 2
            elif sexrandom < 50:
                sexselect = 3
            elif sexrandom < 70:
                sexselect = 4
            else:
                sexselect = 0
            self.sex = msex[sexselect]
            self.first = fbnames[random.randint(0, len(fbnames) - 1)]
        else:
            sexrandom = random.randint(0,300)
            if sexrandom < 20:
                sexselect = 1
            elif sexrandom < 30:
                sexselect = 2
            elif sexrandom < 50:
                sexselect = 3
            elif sexrandom < 70:
                sexselect = 4
            else:
                sexselect = 0
            self.sex = fsex[sexselect]
            self.first = fgnames[random.randint(0, len(fgnames) - 1)]
        self.last = lnames[random.randint(0, len(lnames) - 1)]
        self.mum = mum + self.last
        self.dad = dad + self.last
        while self.mum == self.first + " " + self.last:
            self.mum = mum + self.last
        while self.dad == self.first + " " + self.last:
            self.dad = dad + self.last

# World Boilerplate
class World(object):
    def __init__(self):
        self.war = False
        self.warBetween = ["", ""]

# Variable Setup

d_attendance = ""
welcome_message = "Hello and Welcome to InstLife:Python Edition!"

char = Character() 
world = World()


# Main Code


def start():
    app.startTabbedFrame("InstLife")
    app.startTab("Life")
    app.startScrollPane("s1")
    app.addLabel("output", welcome_message)
    app.stopScrollPane()
    app.setStretch("column")
    app.setSticky("ew")
    app.addButton("Age Up!", begin)
    app.stopTab()

#   Education Tab

    app.startTab("Education")
    app.addLabel("edu", "This is the Education Tab!")
    app.stopTab()

#   Job Tab

    app.startTab("Job")
    app.addLabel("job", "This is the Job Tab!")
    app.stopTab()

#   Relationship Tab

    app.startTab("Relationship")
    app.addLabel("relations", "Welcome to the Relationships Tab!")
    app.stopTab()

#   The Car and House Tab

    app.startTab("Cars and Houses")
    app.addLabel("CandH", "Welcome to the Cars and Houses Tab!")
    app.addEmptyLabel("CandH_output1")
    app.addEmptyLabel("CandH_output2")
    app.stopTab()

#   ME Tab

    app.startTab("Me")
    app.addLabel("Me", "Welcome to the Me Tab!")
    app.stopTab()

#   Settings

    app.startTab("Settings")
    app.addLabel("options", "Welcome to the Settings Tab!")
    app.addButton("Exit", kill)
    app.stopTab()

    app.stopTabbedFrame()

# Start Up
def begin(name):
    output = app.getLabel("output")
    if output == welcome_message:
        char.age = 0
        app.clearLabel("output")
        app.setLabel("output", "You are born a " + char.sex + " called " + char.first + " " + char.last + " by\n" + char.mum + " & " + char.dad + " from " + char.country)
        age_up()
    else:
        age_up()


# Situations
def age_up():
    if char.dead is False:
        # Death Algorithm
        random_number = random.randint(0, 2000)
        death_chance = 1000 - char.age
        if world.war == True and char.country == world.warBetween[0] or char.country == world.warBetween[1] and random_number <100:
            death("the war in " + char.country)
        elif char.age > 80:
            death_chance = 500
            if death_chance > 50:
                death("natural causes!")
        elif world.war == False and random.randint(0, death_chance) < 5:
            death("natural causes (1)!")
        
        #Adulthood Setting
        if char.age > 18:
            app.setLabel("CandH_output2", "You can House!!")
            char.canHouse = True
            char.canDrink = True
            if char.canDrive is False:
                output = app.getLabel("output")
                app.setLabel("output", "You attempted your Driving Test\n" + output)
                drive_test = random.randint(0, 100)
                if drive_test < 25:
                    if drive_test < 75:
                        output = app.getLabel("output")
                        app.setLabel("output", "You Passed your Driving Test!\n" + output)
                        char.canDrive = True
                        app.setLabel("CandH_output1", "You can Car!")
                    else:
                        output = app.getLabel("output")
                        app.setLabel("output", "You Failed your Driving Test\n" + output)

        #Random Wars
        if random_number < 50 and world.war == True:
            world.war = False
            output = app.getLabel("output")
            app.setLabel("output", "The War Between " + world.warBetween[0] + " and " + world.warBetween[1] + " has ended!" + "\n" + output) 
            world.warBetween[0] = ""
            world.warBetween[1] = ""
        elif random_number < 50 and world.war == False:
            world.war = True
            world.warBetween[0] = random.choice(country)
            world.warBetween[1] = random.choice(country)
            while world.warBetween[0] == world.warBetween[1]:
                world.warBetween[1] = random.choice(country)
            output = app.getLabel("output")
            app.setLabel("output", "A War Has Broken Out Between " + world.warBetween[0] + " and " + world.warBetween[1] + "\n" + output )
            

# AGE TITLE STUFF

    output = app.getLabel("output")
    if char.age == 1:
        app.setLabel("output", "\n" + str(char.age) + " Year Old" + "\n" + output)
        char.age = char.age + 1
    else:
        app.setLabel("output", "\n" + str(char.age) + " Years Old" + "\n" + output)
        char.age = char.age + 1

#Exits The GUI
def kill(name):
    app.stop()

#Kills The Character
def death(reason):
    char.dead = True
    app.disableEnter()
    app.setLabel("output", "You Died because of " + reason + "\nYour Funeral was attended by :\n" + char.mum + "\n" + char.dad)



#Setup
app = appJar.gui("InstLife", "600x600")
# app.showSplash("InstLife : Python Edition", fill='red', stripe='black',  fg='white', font=44)
app.enableEnter(begin)
app.bindKey("<Escape>", kill)
start()
app.go()





