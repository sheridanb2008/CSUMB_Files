# Brian Sheridan
# CST 205 
# Lab 4

# Problem 1
def halfVertical():
  fileName = pickAFile()
  pic = makePicture(fileName)
  for x in range(0,getWidth(pic)/2):
    for y in range(0,getHeight(pic)):
      p = getPixel(pic,x,y)
      n = getPixel(pic,(getWidth(pic)- x - 1),y)
      c = getColor(p)
      setColor(n, c)
  repaint(pic)
#  writePictureTo(pic,'C://Users//sheri//Desktop//CST 205//PY flies//Module_2_Lab_4//HalfVertical.jpg')
  
def halfHorzTop():
  fileName = pickAFile()
  pic = makePicture(fileName)
  for y in range(0,getHeight(pic)/2):
    for x in range(0,getWidth(pic)):
      p = getPixel(pic,x,y)
      n = getPixel(pic,x,(getHeight(pic)- y - 1))
      c = getColor(p)
      setColor(n, c)
  repaint(pic)
#  writePictureTo(pic,'C://Users//sheri//Desktop//CST 205//PY flies//Module_2_Lab_4//halfHorzTop.jpg')

def halfHorzBottom():
  fileName = pickAFile()
  pic = makePicture(fileName)
  for y in range(getHeight(pic)/2,getHeight(pic)):
    for x in range(0,getWidth(pic)):
      p = getPixel(pic,x,y)
      n = getPixel(pic,x,((getHeight(pic)\2) - y))
      c = getColor(p)
      setColor(n, c)
  repaint(pic)
#  writePictureTo(pic,'C://Users//sheri//Desktop//CST 205//PY flies//Module_2_Lab_4//halfHorzBottom.jpg')

def fourSquare():
  fileName = pickAFile()
  pic = makePicture(fileName)
  for x in range(0,getWidth(pic)/2):
    for y in range(0,getHeight(pic)):
      p = getPixel(pic,x,y)
      n = getPixel(pic,(getWidth(pic)- x - 1),y)
      c = getColor(p)
      setColor(n, c)
  for y in range(0,getHeight(pic)/2):
    for x in range(0,getWidth(pic)):
      p = getPixel(pic,x,y)
      n = getPixel(pic,x,(getHeight(pic)- y - 1))
      c = getColor(p)
      setColor(n, c)
  repaint(pic)
#  writePictureTo(pic,'C://Users//sheri//Desktop//CST 205//PY flies//Module_2_Lab_4//fourSquare.jpg')
  
#Problem 2

def simpleCopy():
  fileName = pickAFile()
  pic = makePicture(fileName)
  newpic = makeEmptyPicture(getWidth(pic), getHeight(pic))
  for x in range (0, getWidth(newpic)):
    for y in range (0, getHeight(newpic)):
      oPixel = getPixel(pic, x, y)
      nPixel = getPixel(newpic, x, y) 
      color = getColor(oPixel)
      setColor(nPixel, color)
  show(newpic)
  return newpic
  
# Problem 3

def rotate90():
  fileName = pickAFile()
  pic = makePicture(fileName)
  show(pic)
  newpic = makeEmptyPicture(getHeight(pic), getWidth(pic))
  for x in range (0, getWidth(pic)):
    for y in range (0, getHeight(pic)):
      oPixel = getPixel(pic, x, y)
      nPixel = getPixel(newpic, y,getWidth(pic) - x - 1) 
      color = getColor(oPixel)
      setColor(nPixel, color)
  show(newpic)
#  writePictureTo(newpic,'C://Users//sheri//Desktop//CST 205//PY flies//Module_2_Lab_4//Rotate90.jpg')
  return newpic  
# Problem 4

def shrinkPic():
  filename = pickAFile()
  pic = makePicture(filename)
  show(pic)
  newpic = makeEmptyPicture(getWidth(pic) / 2, getHeight(pic) / 2)
  for x in range (0, getWidth(pic) -1 ,2):
    for y in range (0, getHeight(pic) - 1,2):
      oPixel = getPixel(pic, x, y)
      nPixel = getPixel(newpic, x / 2, y / 2) 
      color = getColor(oPixel)
      setColor(nPixel, color)
  show(newpic)
#  writePictureTo(newpic,'C://Users//sheri//Desktop//CST 205//PY flies//Module_2_Lab_4//shrinkPic.jpg')
  return newpic    
  