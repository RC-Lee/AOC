with open('input.txt') as f:
  lines = f.readlines()

f.close()

def checkLine(line, bitArray, index):
  rc = True
  i = 0
  while i < index:
    if int(line[i]) != int(bitArray[i]):
      rc = False
    i += 1
  return rc

def getBit(records, index, bitArray, countType, outNum):
  x = 0
  count = 0
  rc = True
  for record in records:
    ln = record.strip()
    if checkLine(ln, bitArray, index):
      if int(ln[index]) == 1 :
        x+= 1
      else:
        x-= 1

      count += 1
      outNum = ln
      print(outNum)

  print(count)

  if countType == 1:
    bitArray[index] = 1 if (x >= 0) else 0
  else:
    bitArray[index] = 0 if (x >= 0) else 1
  if count == 1:
    rc = False
  return rc, outNum

size = len(lines[0].strip())
numRecs = len(lines)

y = [0] * size

for line in lines:
  ln = line.strip()
  for i in range(0, size):
    y[i] += int(ln[i])

decGamma = 0
decEpsi = 0

for i in range (0, size):
  decGamma += (int(y[i] > (numRecs/2))) * ( 2 ** (size -i -1))
  decEpsi += (int(y[i] < (numRecs/2))) * ( 2 ** (size -i -1))

print(decEpsi*decGamma)

oxArray = [0] * size
o2Array = [0] * size
oxNum = lines[0].strip()
o2Num = lines[0].strip()
oxRecord = lines
o2Record = lines

i = 0
cont = True
while i < size and cont:
  cont, o2Num = getBit(lines, i, o2Array, 0, o2Num)
  i+= 1

j = 0
contj = True
while j < size and contj:
  contj, oxNum = getBit(lines, j, oxArray, 1, oxNum)
  j+= 1

# for i in range(0, size):
#   getBit(lines, i, oxArray, size, 1)
#   getBit(lines, i, o2Array, size, 0)

print(oxArray)
print(o2Array)
print(oxNum)
print(o2Num)

ox = 0
o2 = 0

for i in range (0, size):
  power = size -1 -i
  ox += int(oxNum[i]) * (2 ** power)
  o2 += int(o2Num[i]) * (2 ** power)

print(ox)
print(o2)
print(ox * o2)
      
