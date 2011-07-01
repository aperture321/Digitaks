#monster types, listed and stats 
##Todo - based on some random elements?

####self.user = [monster, name, health, power, defense, speed, luck]
####monsterstats= [name, health, power, defense, speed]

import random, clear, Data, time, datatext

class battle_mode:
  def __init__(self, adventure_type, user_stats):
    self.original_stats = user_stats[:]#hard copy
    self.mon_level = adventure_type
    self.user = user_stats

  def monster_pick(self):
    if self.mon_level == 1:
      self.mons = random.choice(beginner_monsters)
    elif self.mon_level == 2:
      self.mons = random.choice(moderate_monsters)
    elif self.mon_level == 3:
      self.mons = random.choice(hard_monsters)
    elif self.mon_level == 4:
      self.mons = random.choice(extreme_monsters)
    else: #5
      randomy = random.randint(1, 10)
      print "Number is " + str(randomy)
      if randomy == 1: #1/10 chance
        self.mons = bossmon2
      else:
        self.mons = bossmon1

  def mons_attack(self):
    luck_miss = random.randint(1, 20) #implement player luck amounts?
    hit = self.mons[2] - self.user[4] #attack - defense
    print "Monster attacks!"
    if luck_miss == 20: 
      print "MONSTER MISSED!!"
    elif hit <= 0:
      print "Did 1 damage!"
      self.user[2]-= self.user[2] - 1
    else:
      print "Did " + str(hit) + " damage!"
      self.user[2] = self.user[2] - hit

  def player_attack(self):
    print "Player attacks!"
    hit = (self.user[3] - self.mons[3])
    if hit <= 0:
      self.mons[1] -= 1
      print "Did only 1 damage!"
    else:
      self.mons[1] -= hit
      print "Did " + str(hit) + " damage!"

  def mons_defend(self): ##not useful, but needed for choices pick on ai_move function
    print "Monster defends!"
    return self.mons[3] * 2 #Too powerful?

  def mons_insult(self):
    print "Monster insulted you!"  
    choice = random.randint(1, 3)
    if choice == 1:
      print "Monster lowered your power!"
      self.user[3] -= self.user[3] - 2
    elif choice == 2:
      print "Monster lowered your defense!"
      self.user[4] -= self.user[4] - 2
    else:
      print "Monster lowered your speed!"
      self.user[5] -= self.user[5] - 2
  
  def player_insult(self):
    print "You insulted the monster!"
    print random.choice(datatext.insults)
    choice = random.randint(1, 3)
    if choice == 1:
      print "Power lowered!"
      self.mons[2]
    elif choice == 2:
      print "Defense lowered!"
      self.mons[3]
    else:
      print "Speed lowered!"
      self.mons[4]

  def ai_move(self):
    pick = random.randint(1, 3)
    if pick == 1:
      self.mons_attack()
    elif pick == 2:
      self.mons_defend()
    elif pick == 3:
      self.mons_insult()
    else:
      print "error?"
  def player_move(self):
    print '''What would you like to do?
    [1]attack
    [2]insult
    [3]run'''
    user_choice = raw_input("\n")
    try:
      user_choice = int(user_choice)
    except:
      print "invalid"
      clear.clrscr()
      self.player_move()
    if user_choice == 1:
      self.player_attack()
    elif user_choice == 2:
      self.player_insult()
    elif user_choice == 3:
      print "You ran!!"
      Data.start_game(self.original_stats)
    else:
      print "Not a valid choice."
      self.player_move()

  def checkend(self):
    if self.user[2] <= 0: #zero health!
      print "OH NO. You lost..."
      print "Going to main menu."
      time.sleep(3)
      Data.start_game(self.original_stats)
    if self.mons[1] <= 0:
      print "You won!"
      gain = random.randint(1, 5)
      if gain > 2:
        print "Gained stats!"
        self.original_stats[2] += gain ##todo: stat changing per level gain?
        self.original_stats[3] += gain
        self.original_stats[4] += gain
        self.original_stats[5] += gain
      time.sleep(2)
      Data.start_game(self.original_stats)

  def battle(self):
    clear.clrscr()
    self.monster_pick()
    print "You've encountered a " + self.mons[0]
    while 1:
      if self.user[5] > self.mons[4]:#check speed
        self.player_move()
        self.checkend()
        self.ai_move()
        self.checkend()
      else: #monster faster than player
        self.ai_move()
        self.checkend()
        self.player_move()
        self.checkend()


##Todo - luck for criticals???
#stats are: name, health, power, defense, speed
derp = ["derp",3, 1, 1, 1]
herp = ["herp",5, 2, 1, 2]
Fnuf = ["Fnuf",4, 1, 2, 2]
PastyPalt = ["PastyPalt",3, 3, 3, 3]
Fnoo = ["Fnoo",8, 5, 7, 3]
Icicla = ["Icicla",7, 3, 6, 9]
Burgernose = ["Burgernose",9, 4, 4, 8]
Snuffleplob = ["Suffleplob",8, 6, 4, 4]
Litterglue = ["Litterglue",9, 3, 9, 4]
Rainbear = ["Rainbear",2, 9, 9, 6]
Wanpuff = ["Wanpuff",12, 10, 11, 9]
Snarklepox = ["Snarklepox",14, 11, 10, 10]
Gargletart = ["Gargletart",13, 15, 10, 9]
Ninjacrumbs = ["Ninjacrumbs",14, 10, 12, 14]
Raorfester = ["Raorfester",16, 10, 14, 10]
Ninjapankakes = ["Ninjapankakes",19, 16, 17, 20]
Cobrahoof = ["Cobrahoof",18, 19, 16, 17]
Abaclabadar = ["Abaclabadar",20, 16, 17, 18]
Perkington = ["Perkington",17, 17, 20, 18]
Cryxo_the_Wonderhoof = ["Cryxo the Wonderhoof",30, 24, 20, 20]
fuckface = ["fuckface",100, 50, 50, 50] #My friend said I should implement it...
#tutorial_monsters = [derp, herp]

beginner_monsters = [
derp,
herp,
Fnuf,
PastyPalt]


moderate_monsters = [
Fnoo,
Icicla,
Burgernose,
Snuffleplob,
Litterglue,
Rainbear]

hard_monsters = [
Wanpuff,
Snarklepox,
Gargletart,
Ninjacrumbs,
Raorfester]


extreme_monsters = [
Ninjapankakes,
Cobrahoof,
Abaclabadar,
Perkington]

bossmon1 = Cryxo_the_Wonderhoof

bossmon2 = fuckface
