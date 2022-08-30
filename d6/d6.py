def total_fish(numberArray, days=80):
  fish_map = {}

  def add_map(label, days, fish_map):
    # if somehow there was a wrong day input
    # there shouldn't be any fish for days < 0
    if days < 0:
      return 0

    # if key already has value in the map
    # return the value, don't have to count again
    if (label, days) in fish_map:
      return fish_map[(label, days)]

    # counting the initial fishes
    if label > days or days == 0:
      fish_map[(label, days)] = 1
      return fish_map[(label, days)]
    
    # if label is equal to days, 
    # it will give birth to a baby next day
    # for now the fish count is at 1 (just itself)
    if label == days:
      fish_map[(label, days)] = 1

    elif days > 0:
      daysLeft = days - label - 1
      fish_map[(label, days)] = add_map(6, daysLeft, fish_map) + add_map(8, daysLeft, fish_map)
      # the current value for this key would be equal to 
      # its value when it split to itself and its baby
    
    return fish_map[(label, days)]
  
  total = 0
  for label in numberArray:
    total += add_map(int(label), days, fish_map)
  return total


with open ('input.txt') as f:
  numbers = f.read().split(',')

f.close()

# print(numbers)
print(total_fish(numbers, days=18))
print(total_fish(numbers, days=80))
print(total_fish(numbers, days=256))
    