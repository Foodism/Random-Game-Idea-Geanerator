
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
customStandIn1 = ('money','power','kindness','love','wealth','opposition','fame','Mastery','proving others wrong','Security','Control','Change','Impact','Enlightenment','competition','lifestyle','teamwork','fear','anger','deadlines')
customStandIn2 = ('a banana','a revolver','dental floss','their fists','love','kindness','a rocket launcher','a metal bar','a rusty pipe','a rusty suecher','a rope','a book','a katana','light','technology','a giant fan','a box','copious amounts of salt','a wire','a sewing needle')
customStandIn3 = ('a horse','an alien','a dog','a cat','a polar bear','a jaguar','a rock','a human slave','an elephant','a hippopotomus','a floating robot','a robot','a ferret','a flock of birds','a dragon','a monkey','copious amounts of salt','a piece of lettuce','a car','a talking puppet')

print('This game is about a ' + firstStandIn[n] + ' that is trying to ' + secondStandIn[f] + ', this in turn makes them feel ' + thirdStandIn[l] + ', they are motivated by ' + customStandIn1[f] + ' and by ' + customStandIn1[u] + '. their weapon of choice is ' + customStandIn2[r] + ' and their companion of choice is ' + customStandIn3[t])