# Credit goes to Tech With Tim for project tutorial/ideas. 

board = [
[8, 0, 0, 2, 0, 0, 0, 4, 6], 
[0, 0, 7, 9, 0, 0, 0, 0, 0], 
[1, 0, 0, 0, 0, 0, 5, 0, 0], 
[0, 0, 0, 5, 0, 0, 0, 3, 2], 
[4, 0, 8, 0, 0, 0, 7, 0, 1], 
[3, 2, 0, 0, 0, 7, 0, 0, 0], 
[0, 0, 6, 0, 0, 0, 0, 0, 9], 
[0, 0, 0, 0, 0, 3, 2, 0, 0], 
[2, 8, 0, 0, 0, 6, 0, 0, 3]
]

def solve(bo):
  print(bo)
  find = find_empty_square(bo)
  if not find:
    return True
  else:
    row, col = find
  
  for i in range(1,10):
    if valid(bo, i, (row,col)):
      bo[row][col] = i

      if solve(bo):
        return True

      bo[row][col] = 0

  return False



def valid(bo, num, pos):
  # Check rows 
  for i in range(len(bo[0])):
    # Checks each column in row is equal to whatever number we just input and ignores number we just input.
    if bo[pos[0]][i] == num and pos[1] != i:
      return False
  # Checks column
  for i in range(len(bo)):
    if bo[i][pos[1]] == num and pos[0] != i:
      return False
  
  # Checks 3x3 box
  box_x = pos[1] // 3
  box_y = pos[0] // 3
  
  for i in range(box_y * 3, box_y * 3 + 3):
    for j in range(box_x * 3, box_x * 3 + 3):
      # Loops through box
      if bo[i][j] == num and (i, j) != pos:
        return False
  
  return True



def print_board(bo):
  for i in range(len(bo)):
    if i % 3 == 0 and i != 0:
      print("- - - - - - - - - - - -")

    for j in range(len(bo[0])):
      if j % 3 == 0 and j != 0:
        # "end =" to make sure we stay on the same line
        print("|", end ="")

      if j == 8:
        print(bo[i][j])
      else:
        print(str(bo[i][j]) + " ", end ="")


def find_empty_square(bo): 
  for i in range(len(bo)):
    for j in range(len(bo[0])):
      if bo[i][j] == 0:
        # returns row/column (y, x)
        return (i, j)

  return None

print("Original Board")
print_board(board)
solve(board)
print("___________________________")
print("Completed Board")
print_board(board)