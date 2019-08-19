from random import randrange
import time

#DBG = True
DBG = False

BODY = [ " (_) " ]
HEAD = [ "(0_o)" ]

delay = 0.082

global lup
global j
global space

lup = True
j = 235
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

def snekBmoving():
  global space

  chance = randrange(200000)
  if chance < 80000:
    moveto = randrange(200000)
    if moveto < 100000:
      if len(space) > 0:
        space = space[:len(space)-1]
    if moveto > 100000:
      if len(space)+len(HEAD) < 48:
        space += " "


def snek_head():
  global space

  snekBmoving()

  lines = []
  for l in HEAD:
    lines.append(head_color() + space + l)

  return lines

def snek_body():
  global space

  lines = []
  for l in BODY:
    lines.append(body_color() + space + l)

  return lines

from sys import stdout

while True:
  head = snek_head()
  body = snek_body()
  for h in head:
    stdout.write("\r%s" % h)
    stdout.flush()
  time.sleep(delay)
  for b in body:
    stdout.write("\r%s\n" % b)
    stdout.flush()

