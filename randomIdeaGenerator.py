## Random-Game-Idea-Geanerator
#This is a Random Game Idea generator that I made because I was running out of Ideas, (If you don't know how to code in Python I'll show you how you can add more categories in the TXT provided).
#
#//////////////////////////
#1. HOW TO ADD CATEGORIES:/
#//////////////////////////
#  
#  go to the line that says "print" ON LINE 60 (AT BOTTOM)
#  go inside of the parentheses and copy this code sample into the end with a space at the beginning:
#    
#    + ' PROMPT ' + YOURSTANDIN[f / 2 + r / 2]       
#    
##    YOURSTANDIN should be replaced with the stand in that you're using, LATER (REFER TO CUSTOM CATEGORIES SECTION):
#    
##  Then you want to enter your Prompt, to do this, replace the feild that says PROMPT, Example -------- ' they don't like to '
#                                                                                                       ' the character is  '
#                                                                                                       ' they are motivated by '
#                                                       
## // CUSTOM CATEGORIES //
# 
# # First you need to enter 20 words / Phrases that could go at the end of the Prompt that you entered before in the quotations in either of the categories labelled first through     tenth EXAMPLE: 'dance', 'sing', 'live', 'grind' ETCETERRA 
#                
#  
##  After that you should be good to go!

import  random
n = random.randint(0, 20)
f = random.randint(0, 20)
l = random.randint(0, 20)

r = random.randint(0, 20)
u = random.randint(0, 20)
t = random.randint(0, 20)

firstStandIn = ['boy', 'man', 'girl', 'women', 'dog', 'cat', 'dragon', 'koala', 'snake', 'rabbit', 'unicorn', 'pirate', 'game developer', 'fashion designer', 'nutritionist', 'doctor', 'pilot', 'park ranger', 'murderer', 'police officer']
secondStandIn = ['conquer the world', 'save the world', 'save someone close to him', 'survive in the streets', 'kill someone', 'heard animals', 'save his dog', 'Warn someone about something', 'give someone something', 'throw something away', 'lie', 'tell the truth', 'live on another planet', 'deliver a message', 'write a book', 'make it big', 'learn how to grow their own crops', 'repaint their walls', 'make a bed and breakfast', 'save a princess', '']
thirdStandIn = ['happy', 'sad', 'worried', 'frightened', 'scared', 'lively', 'over-joyed', 'dead inside', 'depressed', 'secluded', 'ignored', 'selfish', 'like their the best', 'like a well established person', 'like a new person', 'used', 'deserted', 'wasted', 'amazing', 'like the embodiment of a hangover']

#######################
## CREATE CATEGORIES ##
#######################

# First new Category #

customStandIn1 = ('money','power','kindness','love','wealth','opposition','fame','Mastery','proving others wrong','Security','Control','Change','Impact','Enlightenment','competition','lifestyle','teamwork','fear','anger','deadlines')

# Sedond new Category #

customStandIn2 = ('a banana','a revolver','dental floss','their fists','love','kindness','a rocket launcher','a metal bar','a rusty pipe','a rusty suecher','a rope','a book','a katana','light','technology','a giant fan','a box','copious amounts of salt','a wire','a sewing needle')

# Third new Category #

customStandIn3 = ('a horse','an alien','a dog','a cat','a polar bear','a jaguar','a rock','a human slave','an elephant','a hippopotomus','a floating robot','a robot','a ferret','a flock of birds','a dragon','a monkey','copious amounts of salt','a piece of lettuce','a car','a talking puppet')

# Fourth new Category #

customStandIn4 = ('','','','','','','','','','','','','','','','','','','','')

# Fifth new Category #

customStandIn5 = ('','','','','','','','','','','','','','','','','','','','')

# Sixth new Category #

customStandIn6 = ('','','','','','','','','','','','','','','','','','','','')

# Seventh new Category #

customStandIn7 = ('','','','','','','','','','','','','','','','','','','','')

# eigth new Category #

customStandIn8 = ('','','','','','','','','','','','','','','','','','','','')

# nineth new Category #

customStandIn9 = ('','','','','','','','','','','','','','','','','','','','')

# tenth new Category #

customStandIn10 = ('','','','','','','','','','','','','','','','','','','','')

#######################

print('This game is about a ' + firstStandIn[n] + ' that is trying to ' + secondStandIn[f] + ', this in turn makes them feel ' + thirdStandIn[l] + ', they are motivated by ' + customStandIn1[f] + ' and by ' + customStandIn1[u] + '. their weapon of choice is ' + customStandIn2[r] + ' and their companion of choice is ' + customStandIn3[t])