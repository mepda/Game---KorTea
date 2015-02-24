from random import randint
from sys import exit
str = randint(1,6)
int = randint(1,6)
hp = randint(1,6)
print """ ____  __.          ___________            
|    |/ _|__________\__    _______ _____   
|      < /  _ \_  __ \|    |_/ __ \\__  \  
|    |  (  <_> |  | \/|    |\  ___/ / __ \_
|____|__ \____/|__|   |____| \___  (____  /
        \/                       \/     \/"""
print "Hello Teacher. Welcome to your first day at work..."
nothing = raw_input("...")
print "What's your name?"
name = raw_input(">> ")
print "Hello", name, "teacher. You were written about in our prophecies."
print "The one who will bring peace in the classroom. Are you ready?"
choice1 = raw_input(">> ")
if choice1 in ("yes", "Yes", "Yeah", "Sure", "Okay", "go"):
	print "Very well..."
else:
	print "Too bad. Let's start"
print "You have a", str, "strength and a", int, "intelligence. Not bad!"
print "You only have", hp, "hit points, so be careful!"
nothing2 = raw_input("...")
print """You walk into a narrow, brightly lit office. 
You hear the beat of a drum. The teachers are coming. """
nothing3 = raw_input("...")
print """Suddenly you are surrounded by co-teachers! They are asking
you embarrassing overly personal questions!
How do you respond? (strength or intelligence?)"""
choice2 = raw_input(">> ")
if choice2 in ("int", "intelligence", "smarts", "head"):
	kortea = randint(1,4)
	print "The teachers rolled a", kortea, "for intelligence!"
	if kortea > int:
		hp -= kortea
		print "Your HP is down to", hp, "!!!"
	else: print "You dodged their questions using your wit!"
elif choice2 in ("strength", "str", "strong", "muscles"):
	kortea = randint(1,6)
	print "The teachers rolled a", kortea, "for strength!"
	if kortea > str:
		hp -= kortea
		print "Your hp is down to", hp, "!!!"
	else: print "You flexed your muscles and impressed everyone! Noice!"
else:
	print "That makes no sense! Take damage!"
	dmg = randint(1,4)
	hp -= dmg
	print "You take", dmg,"damage! Your HP is currently", hp, "!!"
print "After your first encounter, your HP is", hp
if hp <= 0:
	print "You are dead!"
	print """  _____                ____              
 / ______ ___ _ ___   / __ \_  _____ ____
/ (_ / _ `/  ' / -_) / /_/ | |/ / -_/ __/
\___/\_,_/_/_/_\__/  \____/|___/\__/_/   
                                         """
	exit(0)
else:
	print "You live to see another class!"
print "The first bell rings. It's time to go to meet the students. Are you ready?"
choice3 = raw_input(">> ")
if choice3 in ("Yes", "yes", "Sure", "Okay", "Go", "Let's go", "Alright"):
	print "Good! You make your way to the second floor."
else:
	ouch = randint(1,3)
	hp -= ouch
	print """Your boss starts yelling at you to go to class. 
She takes out her hurt stick and hits you for %d damage!""" % ouch
	if hp < 1:
		print "Your boss criticals you over the head!"
		print """  _____                ____              
 / ______ ___ _ ___   / __ \_  _____ ____
/ (_ / _ `/  ' / -_) / /_/ | |/ / -_/ __/
\___/\_,_/_/_/_\__/  \____/|___/\__/_/   
                                         """
		exit(0)
	else:
		print "You only have %d hp left!" % hp

print """You walk into a small classroom. Scratches and Korean swears 
are all over the walls and desks. A smell of snack food lingers in the air.
You hear many foot steps outside in the hallway. Students."""
print "Do you take a defensive or offensive measure?"
choice4 = raw_input(">> ")
if choice4 in ("defensive", "defense", "defensive measure", "def"):
	print "You create a barricade with desks in the back of the class"
	bonus = randint(1,4)
	hp += bonus
	print "You get a bonus to your HP. Your current HP is", hp, "!"
elif choice4 in ("offensive", "offense", "offensive measures"):
	print "You take the hitting cane out of the drawer. It glows with power."
	bonus = randint(1,4)
	str += bonus
	print "You get a strength bonus. Your strength is now", str,"!!"
else:
	ouch = randint(1,4)
	hp -= ouch
	print "You panic and run around in circles taking", ouch, "damage"
	print "You now have", hp, "remaining!"
	