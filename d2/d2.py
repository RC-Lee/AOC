with open('input.txt') as f:
  lines = f.readlines()

f.close()

hor = 0
depth = 0
aim = 0

for line in lines:
  s = line.split()
  if s[0] == 'forward':
    hor += int(s[1])
    depth += (aim * int(s[1]))
  if s[0] == 'up':
    aim -= int(s[1])
  if s[0] == 'down':
    aim += int(s[1])

print(hor)
print(depth)
print(aim)
print(hor*depth)

print(len(lines))