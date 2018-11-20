# Brian Sheridan
# CST 205
# Lab 9

# Problem 1 
# Split a clip out of a wave file
def clip(source, start, end):
  rate = getSamplingRate(source)
  temp = makeEmptySound(end - start,int(rate))
  for sample in range(0,getLength(temp)):
    setSampleValueAt(temp,sample,getSampleValueAt(source,start + sample))
  return temp 
  

# Problem 2
# splice file into a larger file
def copy(source, target, start):
  maxLength = min(getLength(target) - start, getLength(source)) + start
  for sample in range(start,maxLength):
    setSampleValueAt(target,sample,getSampleValueAt(source,sample - start))
  return target
  
# Problem 4
# reverse play
def reverse(source):
  rate = getSamplingRate(source)
  temp = makeEmptySound(getLength(source),int(rate))
  for sample in range(0,getLength(temp)):
    setSampleValueAt(temp,sample,getSampleValueAt(source,getLength(source) - sample - 1))
  return temp 


# -----------------------------------------
# Testing Functions
# -----------------------------------------
# Test problem 1
def problem1Test():
  # FIND THE PATH TO THE CURRENT DIRECTORY AND ADD THE CLIPART FOLDER 
  root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Sound Files")
  sound = makeSound(os.path.join(root,"ateam.wav"))
  s = clip(sound,14960,getLength(sound))
  writeSoundTo(s, os.path.join(root,"Problem1.wav"))
  
# Test problem 2
def problem2Test():
  # FIND THE PATH TO THE CURRENT DIRECTORY AND ADD THE CLIPART FOLDER 
  root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Sound Files")
  sound1 = makeSound(os.path.join(root,"peabody.wav"))
  sound2 = makeSound(os.path.join(root,"Problem1.wav"))  
  s = copy(sound2,sound1,96292)
  writeSoundTo(s, os.path.join(root,"Problem2.wav"))  
  
# Trest Problem 3
def collage():
  root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Sound Files")
  s1 = makeSound(os.path.join(root,"meet_parents_bring_u_down2.wav"))
  s2 = makeSound(os.path.join(root,"shrek_tic_tacs2.wav"))
  s3 = makeSound(os.path.join(root,"stinky2.wav"))
  s4 = makeSound(os.path.join(root,"itsmyflap2.wav"))
  s5 = makeSound(os.path.join(root,"allen_crimes_disgusting2.wav"))
  sd1 = clip(s1,0,125928)
  sd2 = clip(s2,0,82176)
  sd3 = clip(s3,58420,237820)
  sd4 = clip(s4,0,96992)
  sd5 = clip(s5,104106,203280)
  totalLength = getLength(sd1) + getLength(sd2) + getLength(sd3) + getLength(sd4) + getLength(sd5)
  rate = getSamplingRate(sd1)
  target = makeEmptySound(totalLength,int(rate))
  copy(sd1,target,0)
  length = getLength(sd1)
  copy(sd2,target,length)
  length += getLength(sd2)
  copy(sd3,target,length)
  length += getLength(sd3)
  copy(sd4,target,length)
  length += getLength(sd4)  
  copy(sd5,target,length)
  writeSoundTo(target, os.path.join(root,"Problem3.wav"))  
  
# Test Problem4
def testProblem4():  
  root = os.path.join(os.path.dirname(os.path.realpath(__file__)),"Sound Files")
  target = reverse(makeSound(os.path.join(root,"shrek_tic_tacs2.wav")))
  writeSoundTo(target, os.path.join(root,"Problem4.wav"))    