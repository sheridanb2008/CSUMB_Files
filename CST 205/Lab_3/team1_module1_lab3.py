#Northwestern Technology
#Kevin Bentley
#Craig Calvert
#Brian Sheridan
#Samuel Pearce

#CST 205
#Module 1, Lab 3

def get_pic():
  return makePicture(pickAFile())

#Problem 1
def halfRed():
  lessRed(50)  
  
def lessRed(pct):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * ((100-pct) / 100.0))
  repaint(pic)
  
#Problem 2
# It could potentially be a problem if the increase caused the red value
# to be greater than 255. Inside JES it seems to clip it to 255 (there is no
# visible difference between setting it to 255 max, or just letting it get
# set higher than 255.
def moreRed(amt):
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    setRed(p, r * (amt/100.0))
  repaint(pic)

#Problem 3
# There are a lot of ways to make things look pinker. This is one of them
def roseColoredGlasses():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p,g * 1.25)
    setGreen(p,g * 0.5)
    setBlue(p,b * 0.5)
  repaint(pic)
  
#Problem 4
def lightenUp():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    oldColor = getColor(p)
    newColor = makeLighter(oldColor)
    setColor(p,newColor)
  repaint(pic)

#Problem 5
def makeNegative():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p,255 - r)
    setGreen(p,255 - g)
    setBlue(p,255 - b)
  repaint(pic)

#Problem 6

def BnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    gray = (r + g + b) / 3.0
    setRed(p,gray)
    setGreen(p,gray)
    setBlue(p,gray)
  repaint(pic)

def betterBnW():
  pic = get_pic()
  pixels = getPixels(pic)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = r*0.299 + g*0.587 + b*0.114
    setRed(p,luminance)
    setGreen(p,luminance)
    setBlue(p,luminance)
  repaint(pic)
