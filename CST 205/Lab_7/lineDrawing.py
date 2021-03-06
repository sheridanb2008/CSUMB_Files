# Brian Sheridan
# CST 205
# Line Drawing

# Select picture and run through functions
def Main():
  root = r'Z:\Csumb\CST 205\Labs\Lab_7'
  pic = lineDrawing(betterBnW(makePicture(os.path.join(root,"orig.jpg"))))
  show(pic)
  
# Make the Picture Black and White
def betterBnW(source):
  pixels = getPixels(source)
  for p in pixels:
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = r*0.299 + g*0.587 + b*0.114
    setRed(p,luminance)
    setGreen(p,luminance)
    setBlue(p,luminance)
  return source
  
# Look at the pixel to the right and below
# if distance is great enough make pixel
# Black else make White.  
def lineDrawing(source):
  for x in range(0, getWidth(source) - 1):
    for y in range(0, getHeight(source)- 1):
      right = getColor(getPixel(source,x + 1, y))
      below = getColor(getPixel(source,x, y + 1))
      current = getColor(getPixel(source,x, y))
      if distance(current,right) > 15 and distance(current,below) > 15:
        setColor(getPixel(source,x,y),black)
      else:
        setColor(getPixel(source,x,y), white)
  return source
            
    