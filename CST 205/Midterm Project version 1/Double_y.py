
def test():
  root = r'Z:\Csumb\CST 205\Labs\Midterm Project version 1'
  pic1 = makePicture(os.path.join(root,"1.jpg"))
  pic2 = makePicture(os.path.join(root,"2.jpg"))
  pic3 = makeEmptyPicture(getWidth(pic1),getHeight(pic1))
  D(pic1,pic3,0)
  D(pic2,pic3,1)
  show(pic3)

def D(source,target,startY):
  for y in range(startY, getHeight(source), 2):
    for x in range(0, getWidth(source)):
      color = getColor(getPixel(source,x,y))
      setColor(getPixel(target,x,y),color)
  return source