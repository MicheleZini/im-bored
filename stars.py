from random import randrange
import time

#DBG = True
DBG = False

delay = 0.187

global lup
global j
global space
global home
pos= 240
home =["🌍","🌎","🌏"]
lup = True
j = 234
space = "             "

def body_color():
  global lup
  global j

  if (j == 255) or (j == 232):
    lup = not lup

  if lup: # == True:
    j += 1
  else:
    j -= 1

  #range    = "\x1B[38;5;130m"
  a = 38
  b = 5
  c = j

  if DBG:
    print("[dbg] a=%i b=%i c=%i" % (a,b,c))
    print("[dbg] lup=%s" % (lup))

  return "\x1B[%i;%i;%im" % (a,b,c)

def head_color():
  #range    = "\x1B[38;5;130m"
  a = 38
  b = 5
  c = 130

  if DBG:
    print("[dbg] a=%i b=%i c=%i" % (a,b,c))
    print("[dbg] lup=%s" % (lup))

  return "\x1B[%i;%i;%im" % (a,b,c)

from sys import stdout

def stars():
  lol = ""
  for i in range(40):
   bob = " "

   chance = randrange(200000)
   if chance < 7000:
    moveto = randrange(200000)
    if moveto < 150000:
     bob = "*"
    if moveto > 50000:
     bob = "+"
   lol += body_color() + bob

   if len(lol) > 2: # easter eggs
    if chance < 470:
      ggg = "  "
      moveto = randrange(200000)
      if moveto < 100000:
        ggg = "✨"
      if moveto < 80000:
        ggg = "🚀"
      if moveto < 40000:
        ggg = "💥"
      if moveto < 20000:
        ggg = "👾"
      if moveto < 15000:
        ggg = "👽"

      lol = lol[:len(lol)-24] + body_color() + ggg
  return lol

def spin():
  global home
  now = home[:1]
  home = home[1:] + now
  return now[0]

b = str(stars())
h = b[:pos] + spin() + b[pos+12:]

while True:
  #print(pos)
  #pos+=1
  #stdout.flush()
  stdout.write("\r%s" % h)

  time.sleep(delay)
  bb=b
  b = str(stars())
  h = b[:pos] + spin() + b[pos+12:]
  #stdout.flush()

  stdout.write("\r%s\n" % bb)


