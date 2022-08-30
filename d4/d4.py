class Board:  
  def fillBoard(self, inputs):
    lines = inputs.split("\n")
    for i in range(5):
      numbers = [int(number) for number in lines[i].split()]
      for j in range(5):
        self.theBoard_[i][j] = numbers[j]
        self.sum_ += numbers[j]
    self.countSums()

  def printBoard(self):
    for i in range(5):
      for j in range(5):
        print(self.theBoard_[i][j], end = ' ')
      print(self.rowSum_[i]) 
    
    for j in range(5):
      print(self.colSum_[j], end = " ")
    print('')
  
  def getSum(self):
    return self.sum_
  
  def getRowSum(self, index):
    return self.rowSum_[index]

  def getColSum(self, index):
    return self.colSum_[index]

  def countSums(self):
    self.diag1_ = 0
    self.diag2_ = 0
    for i in range(5):
      self.rowSum_[i] = 0
      self.colSum_[i] = 0
      self.diag1_ += self.theBoard_[i][i]
      self.diag2_ += self.theBoard_[i][(5-i-1)]
    for i in range(5):
      for j in range(5):
        self.rowSum_[i] += self.theBoard_[i][j]
        self.colSum_[j] += self.theBoard_[i][j]

  def crossOut(self, number):
    # print("crossing out number: ", end = " ")
    # print(number)
    i = 0
    j = 0
    while i < 5:
      for j in range(5):
        if self.theBoard_[i][j] == number:
          self.sum_ -= number
          self.theBoard_[i][j] = -1
          self.countSums()
      i +=1
          
  def checkWin(self):
    win = False
    # if self.diag1_ == -5:
    #   win = True
    # if self.diag2_ == -5:
    #   win = True
    win = -5 in self.colSum_
    if not win:
      win = -5 in self.rowSum_
    self.done_ = win
    return win
  
  def __init__(self, inputs):
    self.sum_ = 0
    self.rowSum_ = [0] * 5
    self.colSum_ = [0] * 5
    self.diag1_ = 0
    self.diag2_ = 0
    self.done_ = False
    self.theBoard_ = [ [0 for j in range(5)] for i in range(5)]
    self.fillBoard(inputs)


with open('input.txt') as f:
  lines = f.read().split("\n\n")

f.close()

# print(lines)
allnumbers = [int(number) for number in lines[0].split(',')]
# print(allnumbers)
boards = [None] * (len(lines) -1)

for i in range(1, len(lines)):
  boards[(i-1)] = Board(lines[i])

for i in range(0, len(boards)):
  boards[i].printBoard()
  print('')

# for i in range(0, len(boards)):
#   boards[i].printBoard()
#   print('')

# index = 0
# winner = False
# winnerSum = 0
# while index < len(allnumbers) and not winner:
#   i = 0
#   while i < len(boards) and not winner:
#     boards[i].crossOut(allnumbers[index])
#     winner = boards[i].checkWin()
#     if winner:
#       winnerSum = boards[i].sum_
#     i += 1
#   index += 1

index = 0
finished = False
lastSum = 0
boardcount = len(boards)
while index < len(allnumbers) and not finished:
  i = 0
  while i < len(boards) and not finished:
    if not boards[i].done_:
      boards[i].crossOut(allnumbers[index])
      if boards[i].checkWin():
        boardcount -= 1
      if boardcount == 0:
        finished = True
        lastSum = boards[i].sum_
    i += 1
  index += 1

# print(winner)
# print(winnerSum)
# print(allnumbers[index-1])
# print(winnerSum * allnumbers[index-1])

print(finished)
print(lastSum)
print(allnumbers[index -1])
print(lastSum * allnumbers[index -1])

# for i in range(0, len(boards)):
#   boards[i].printBoard()
#   print('')