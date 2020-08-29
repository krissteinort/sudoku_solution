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
        print(i,j)
        return (i, j)

