with open('input.txt') as f:
  lines = f.readlines()

x = 0
prev = lines[0]
for line in lines:
  if line < prev:
    x = x + 1
  prev = line

print(2000 - x)

y = 0
print(len(lines))
i = 0
print(y)
while i < len(lines):
  prev = lines[i]
  if (i + 3) < len(lines):
    compare = lines[(i+3)]
    if prev >= compare:
      y +=1
  i +=1

print(y)
print(2000 - y)
    
