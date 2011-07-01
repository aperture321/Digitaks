#contains intro and menu screen intro!
import time
import clear
import Characters

class first_screens:
  def __init__(self):
    #nothing to do
    abcd = 0
  def printchoice1(self):
    print "[1] New Game"
    print "[2] Load Game"
    print "[3] Exit Game"
    print "[4] Tutorial?"
  def menu1(self):
    print "What would you like to do?"
    first_screens().printchoice1()
    u_input = raw_input("\n")
    try:
      u_input = int(u_input)
    except:
      print "Invalid. Please try again."
      self.menu1()
    if int(u_input) > 4 or int(u_input) < 1:
      print "Invalid choice."
      self.menu1()
    else:
      return int(u_input)

def title_screen():
  clear.clrscr() #ensures on program start terminal is not crowded or nasty
  x = '''
|-----------
| Monster
|  Digitaks
|-------------
'''
  for i in x:
    print i,
    time.sleep(.2)
  time.sleep(3)
  print '\n'
  #omit for design purposes?clear.clrscr()

def tutorial():
  clear.clrscr()
  print "Thank you for viewing the tutorial."
  time.sleep(3)
  print "This will attempt to show exactly how to fight a monster."
  time.sleep(3)
  print "However, this feature is not implemented yet. Sorry. Find someone who cares."
  time.sleep(2)
