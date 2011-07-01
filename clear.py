#clearscreen file. Tested and working on windowsNT+ and linux-based systems
import os
def clrscr():
  if os.name == 'nt':
    os.system('cls')
  else:
    os.system('clear')
