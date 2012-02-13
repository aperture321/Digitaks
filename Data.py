#attempt for data variables for interface of monsters.
import Characters, random, time, datatext, clear, sys, Savecatch, Monsters
import intro


def create_monster(): #returning initial stats of monster...
  print "\n Welcome to the wonderful world of Digitaks!!"
  time.sleep(3)
  print "Creating monster for you..."
  time.sleep(2)
  print "DONE! Your monster is..."
  monster = random.choice(Characters.monster_picks)
  print str(monster)
  print "What would you like to name it?"
  namey = raw_input("Monster name:")
  i = 0
  base_stats = [monster, namey]
  while i < 5: #health, power, defense, speed, luck
    choice = random.randint(3, 10)
    base_stats.append(choice)
    i += 1
  print "Monster created!"
  time.sleep(2)
  clear.clrscr()
  return base_stats


def menu_choices1():
  print "What would you like to do?"
  print '''[1]adventure
[2]training
[3]status
[4]save game
[0]exit'''
  choice = raw_input()
  try:
    choice = int(choice)
  except:
    print "Invalid."
    clear.clrscr()
    menu_choices1()
  if choice > 4 or choice < 0:
    print "Invalid."
    clear.clrscr()
    menu_choices1()
  return choice

def status(m_s): #TODO fix this!
  clear.clrscr()
  print "Stats:"
  print "|                  "
  print "|----------------------\n\n"
  print "|Name: ",m_s[1],"HP: " + str(m_s[2]) + "|"
  print "|Power: ",m_s[3],"        "
  print "|Defense: ",m_s[4],"      "
  print "|Speed: ",m_s[5],"        "
  print "|Luck: ",m_s[6],"         \n\n"
  print "|----------------------"
  print "|                  "
  input = raw_input("Type q to quit\n")
  if input.lower().startswith('q'):
    clear.clrscr()
  else:
    clear.clrscr()
    status(m_s)

def start_game(mons_stats):
  #clear.clrscr() #DEBUG: comment out this line!
  print str(mons_stats[0])
  print random.choice(datatext.digi_status) + "\n\n"
  time.sleep(2)
  choice = menu_choices1()
  if choice == 0:
    clear.clrscr()
    game()
  elif choice == 1:
    mons_stats = menuchoices2(mons_stats)
    start_game(mons_stats)
  elif choice == 2:
    mons_stats = menuchoices3(mons_stats)
    start_game(mons_stats)
  elif choice == 3:
    status(mons_stats)
    start_game(mons_stats)
  elif choice == 4:
    Savecatch.Game_save(mons_stats).save_game()
    start_game(mons_stats)

def menuchoices2(mons_stats): #adventure mode
  clear.clrscr()
  totalmons = sum(mons_stats[2:]) #total value of monster attributes
  sorry = "Sorry, but you need more training!"
  print '''What would you like to do?
  [1]take a walk
  [2]take a stroll
  [3]take a hike
  [4]go mountain climbing
  [5]find a dimensional rift
  [9]go back'''
  activity = raw_input()
  try:
    activity = int(activity)
  except:
    print "Not a valid input."
    clear.clrscr()
    menuchoices3(mons_stats)
  if activity == 9:
    start_game(mons_stats)
  elif activity == 1:
    mons_stats = Monsters.battle_mode(1, mons_stats).battle()
  elif activity == 2:
    if totalmons >= 70: #Variable cap. May need stat adjustment
      mons_stats = Monsters.battle_mode(2, mons_stats).battle()
    else:
      print sorry
  elif activity == 3:
    if totalmons >= 80:
      mons_stats = Monsters.battle_mode(3, mons_stats).battle()
    else:
      print sorry
  elif activity == 4:
    if totalmons >= 90:
      mons_stats = Monsters.battle_mode(4, mons_stats).battle()
    else:
      print sorry
  elif activity == 5:
    if totalmons >= 100:
      mons_stats = Monsters.battle_mode(5, mons_stats).battle()
    else:
      print sorry
  else:
    print "Not a valid option"
    #menuchoices2(mons_stats) #strange bug, will refer to training!! o.O
  time.sleep(3)
  return mons_stats

def menuchoices3(mons_stats): ##training mode
  clear.clrscr()
  total_stat_gain = random.randint(1, 3) #TODO fix.
  print '''What would you like to do?
  [1]eat forbidden fruit
  [2]punch baby
  [3]argue with lawyer
  [4]jaywalk
  [5]hit grandma
  [9]go back'''
  activity = raw_input()
  try:
    activity = int(activity)
  except:
    print "Not a valid input."
    menuchoices3(mons_stats)
  if activity == 9:
    start_game(mons_stats)
  elif activity == 1: ####playerstats = [monster, name, health, power, defense, speed, luck]
    print str(random.choice(datatext.eat_fruits))
    mons_stats[2] += total_stat_gain
  elif activity == 2:
    print str(random.choice(datatext.baby_punching))
    mons_stats[3] += total_stat_gain
  elif activity == 3:
    print str(random.choice(datatext.lawyer_argues))
    mons_stats[4] += total_stat_gain
  elif activity == 4:
    print str(random.choice(datatext.jay_walking))
    mons_stats[5] += total_stat_gain
  elif activity == 5:
    print str(random.choice(datatext.grandma_punching))
    mons_stats[6] += total_stat_gain
  else:
    print "Not a valid option."
    menuchoices3(mons_stats)
  time.sleep(3)
  return mons_stats

def game():
    introscr = intro.first_screens()
    inputs = introscr.menu1() #will return integer value of choices.
    savechoices = Savecatch.Game_save()
    if inputs == 4:
      intro.tutorial()
      sys.exit()
    elif inputs == 3:
      print "Bye!!"
      time.sleep(2)
      sys.exit()
    elif inputs == 2:
      all_data = savechoices.load_game() #how to exit gracefully?
      time.sleep(2)
      clear.clrscr()
    elif inputs == 1: 
      clear.clrscr()
      all_data = create_monster()
    start_game(all_data)
    intro.title_screen(0)
    game()

intro.title_screen(1)
game()
