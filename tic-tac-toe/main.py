def draw():
   # empty board
   board = ""
   for i in range(5):
     if i%2 == 0:
       board += "|    " *4
     else:
       board += " --- " *3
     board += "\n"
   print(board)

draw()
