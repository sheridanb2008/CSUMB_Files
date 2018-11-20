# Brian Sheridan
# CST 205
# Module 2 Lab 5

# Warm Up:

def imageBigger():
  pic = makePicture(pickAFile())
  newPic = makeEmptyPicture(getWidth(pic) * 2, getHeight(pic) * 2)
  centerWidth = getWidth(newPic) / 2
  centerHeight = getHeight(newPic) / 2
  startWidth = centerWidth - getWidth(pic) / 2
  startHeight = centerHeight - getHeight(pic) / 2
  endWidth = centerWidth + getWidth(pic) / 2
  endHeight = centerHeight + getHeight(pic) / 2
  for x in range(startWidth, endWidth):
    for y in range(startHeight, endHeight):
      picPixel = getPixel(pic,x - startWidth, y - startHeight)
      newPixel = getPixel(newPic,x, y)
      color = getColor(picPixel)
      setColor(newPixel,color)
  repaint(newPic)
#  writePictureTo(newPic,r"A:\Users\sheridanb2008\Documents\CSMB\CST 205\PY flies\Module_2_Lab_5\imageBigger.png")
  return newPic
  
  
# Problem 1
  
def pyCopy(source, target, targetX, targetY):
  for x in range(0, getWidth(source)):
    for y in range(0, getHeight(source)):
      picPixel = getPixel(source,x, y)
      newPixel = getPixel(target,targetX + x ,targetY + y)
      color = getColor(picPixel)
      setColor(newPixel,color)
  return target
  
def testProblem1():
  pic = makePicture(pickAFile())
  newPic = makeEmptyPicture(getWidth(pic) * 2, getHeight(pic) * 2)
  centerWidth = getWidth(newPic) / 2
  centerHeight = getHeight(newPic) / 2
  startWidth = centerWidth - getWidth(pic) / 2
  startHeight = centerHeight - getHeight(pic) / 2
  pyCopy(pic, newPic, startWidth, startHeight)
  repaint(newPic)
  
# Problem 2

def makeCollage():
# Get image and modify the picture
  collage = makeEmptyPicture(2550,3300)
  root = r'A:\Users\sheridanb2008\Documents\CSMB\CST 205\PY flies\Module_2_Lab_5'
  pic1 = halfVertical(makePicture(os.path.join(root,"1.jpg")))
  pic2 = halfHorzTop(makePicture(os.path.join(root,'2.jpg')))
  pic3 = halfHorzBottom(makePicture(os.path.join(root,'3.jpg')))
  pic4 = makeSepia(makePicture(os.path.join(root,'4.jpg')))
  pic5 = Artify(makePicture(os.path.join(root,'5.jpg')))
  pic6 = makePicture(os.path.join(root,'6.jpg'))
  pic7 = rotate90(makePicture(os.path.join(root,'7.jpg')))
  pic8 = fourSquare(makePicture(os.path.join(root,'8.jpg')))
  pic9 = makePicture(os.path.join(root,'9.jpg'))
# Place image on collage 
  pyCopy(pic1,collage,0,0)  
  pyCopy(pic2,collage,0,825)  
  pyCopy(pic3,collage,0,1650)  
  pyCopy(pic4,collage,0,2475)  
  pyCopy(pic5,collage,1275,0)
  pyCopy(pic6,collage,1275,825)  
  pyCopy(pic7,collage,1275,1650)
  pyCopy(pic8,collage,1275,2475)  
  greenScreen(collage,pic9,424,1410)
  greenScreen(collage,pic9,1274,585)
  greenScreen(collage,pic9,1274,2235)
# Write to file      
  writePictureTo(collage,r"A:\Users\sheridanb2008\Documents\CSMB\CST 205\PY flies\Module_2_Lab_5\collage.jpg")

# Makes vertical mirror
def halfVertical(source):
  for x in range(0,getWidth(source)/2):
    for y in range(0,getHeight(source)):
      p = getPixel(source,x,y)
      n = getPixel(source,(getWidth(source)- x - 1),y)
      c = getColor(p)
      setColor(n, c)
  return source

# Makes Hoiz mirror of the top half     
def halfHorzTop(source):
  for y in range(0,getHeight(source)/2):
    for x in range(0,getWidth(source)):
      p = getPixel(source,x,y)
      n = getPixel(source,x,(getHeight(source)- y - 1))
      c = getColor(p)
      setColor(n, c)
  return source

# Makes Hoiz mirror of the bottom half 
def halfHorzBottom(source):
  for y in range(getHeight(source)/2,getHeight(source)):
    for x in range(0,getWidth(source)):
      p = getPixel(source,x,y)
      n = getPixel(source,x,((getHeight(source)\2) - y))
      c = getColor(p)
      setColor(n, c)
  return source

# Make a mirror of the top left quarter of the image
def fourSquare(source):
  for x in range(0,getWidth(source)/2):
    for y in range(0,getHeight(source)):
      p = getPixel(source,x,y)
      n = getPixel(source,(getWidth(source)- x - 1),y)
      c = getColor(p)
      setColor(n, c)
  for y in range(0,getHeight(source)/2):
    for x in range(0,getWidth(source)):
      p = getPixel(source,x,y)
      n = getPixel(source,x,(getHeight(source)- y - 1))
      c = getColor(p)
      setColor(n, c)
  return source

# rotates image 90 degrees to the left
def rotate90(source):
  target = makeEmptyPicture(getHeight(source), getWidth(source))
  for x in range (0, getWidth(source)):
    for y in range (0, getHeight(source)):
      oPixel = getPixel(source, x, y)
      nPixel = getPixel(target, y,getWidth(source) - x - 1) 
      color = getColor(oPixel)
      setColor(nPixel, color)
  return target  
  
# Adjusts colors to make Sepia
def makeSepia(source):
  pixels = getPixels(source)
  for x in range(0, getWidth(source)):
    for y in range (0, getHeight(source)):
      p = getPixel(source, x, y)
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
      luminance = r*0.299 + g*0.587 + b*0.114
      redMult = 1
      blueMult = 1
      if(r < 63):
        redMult = 1.1
        blueMult = 0.9
      elif(62 < r and r < 192):
        redMult = 1.15
        blueMult = 0.85
      else:
        redMult = 1.08
        blueMult = 0.93    
      r = redMult * luminance
      r = min(r,255)
      b = blueMult * luminance
      setRed(p,r)
      setGreen(p,luminance)
      setBlue(p,b)
  return source

# Adjusts colors for Artify
def Artify(source):
  pixels = getPixels(source)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    setRed(p,getArtifiedPixel(r))
    setGreen(p,getArtifiedPixel(g))
    setBlue(p,getArtifiedPixel(b))
  return source  

def getArtifiedPixel(p):
  #This is an ordered list of tuples. The first value is the 
  #upper range value to compare against. The second value is
  #the value to replace the original pixel with.
  colorSubstitutionTable = [(64,31),(128,95),(192,159),(256,223)]
  for tuple in colorSubstitutionTable:
    #If this pixel's value is less than the first value
    #in the tuple, return the second value
    if(p < tuple[0]):
      return tuple[1]
  return p
  
# Greenscreen rendering  
def greenScreen(backGround, foreGround, targetX, targetY):
  greenScreen = makeColor(0,255,0)
  shadow = makeColor(33,29,22)
  for x in range(0, getWidth(foreGround)):
    for y in range(0, getHeight(foreGround)):
      picPixel = getPixel(foreGround,x, y)
      newPixel = getPixel(backGround,targetX + x ,targetY + y)
      color = getColor(picPixel)
      if distance(color,greenScreen) > 100:
        setColor(newPixel,color)
      if distance(color,greenScreen) > 100 and distance(color,greenScreen) < 150:
        setColor(newPixel,shadow)  
  return backGround
  