class Vent():
  def __init__(self, xlen, ylen):
    self.ventArr = [ [0 for j in range(xlen)] for i in range(ylen)]

  def markRun(self, arr):
    if arr[0] == arr[2] or arr[1] == arr[3]:
      incx = 1
      incy = 1
      if(arr[1] > arr[3]):
        incy = -1
      if(arr[0] > arr[2]):
        incx = -1
      sx = arr[0]
      ex = arr[2] + incx
      sy = arr[1]
      ey = arr[3] + incy
      for i in range(sy, ey, incy):
        for j in range(sx, ex, incx):
          self.ventArr[i][j] += 1
    elif arr[0] != arr[2] and arr[1] != arr[3]:
      # print(arr[0], end = ", ")
      # print(arr[1], end = " - ")
      # print(arr[2], end = ", ")
      # print(arr[3])
      horizontal = arr[2] - arr[0]
      vertical = arr[3] - arr[1]
      sx = arr[0]
      sy = arr[1]
      inch = 1
      incv = 1
      if horizontal < 0:
        inch = -1
      if vertical < 0:
        incv = -1
      h = 0
      v = 0
      while(h != (horizontal + inch) and v != (vertical + incv)):      
        # print(sx + h, end = ", ")
        # print(sy + v)
        self.ventArr[sy+v][sx+h] += 1
        h += inch
        v += incv

  
  def printVent(self):
    for i in range(len(self.ventArr)):
      for j in range(len(self.ventArr[i])):
        print(self.ventArr[i][j], end = " ")
      print("")
  
  def count2(self):
    count = 0
    for i in range(len(self.ventArr)):
      for j in range(len(self.ventArr[i])):
        if self.ventArr[i][j] > 1:
          count += 1
    return count

def parsRec(line):
  points = line.split(' -> ')
  x1, y1 = points[0].split(",")
  x2, y2 = points[1].split(",")
  return [int(x1), int(y1), int(x2), int(y2)]

with open ('input.txt') as f:
  lines = f.read().split('\n')

f.close()

numRecs = len(lines)
testPoint = lines[0].split(" -> ")

a = [[0] * 4] * numRecs
minx = 0
miny = 0
maxx = 0
maxy = 0
for i in range(0, numRecs):
  if lines[i] != '':
    a[i] = parsRec(lines[i])
    if minx > a[i][0]:
      minx = a[i][0]
    if minx > a[i][2]:
      minx = a[i][2]
    if maxx < a[i][0]:
      maxx = a[i][0]
    if maxx < a[i][2]:
      maxx = a[i][2]
    if miny > a[i][1]:
      miny = a[i][1]
    if miny > a[i][3]:
      miny = a[i][3]
    if maxy < a[i][1]:
      maxy = a[i][1]
    if maxy < a[i][3]:
      maxy = a[i][3]

xlen = maxx - minx + 1
ylen = maxy - miny + 1


vent = Vent(xlen, ylen)
for i in range(numRecs):
  vent.markRun(a[i])

# vent.markRun(0,2,9,9)
# vent.markRun(9,3,4,4)
# vent.printVent()
pts = vent.count2()
print(pts)