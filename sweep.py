def validate( block_data ):
  bombcount = 0
  result = ""
  if block_data [1][1] == -1:
    result = "I'm a BOMB!"
    
  if block_data [0][0] == -1:
      bombcount = bombcount + 1
  elif: block_data [0][1] == -1:
    bombcount = bombcount + 1
  elif block_data [0][2] == -1:
    bombcount = bombcount + 1
  elif block_data [1][0] == -1:
    bombcount = bombcount + 1
  elif block_data [1][2] == -1:
    bombcount = bombcount + 1
  elif block_data [2][0] == -1:
    bombcount = bombcount + 1
  elif block_data [2][1] == -1:
    bombcount = bombcount + 1
  elif block_data [2][2] == -1:
    bombcount = bombcount + 1

    if block_data[1][1] == bombcount: 
      result = "Valid Bomb" 

      if block_data[0][0] == -1 and block_data[0][1] == 1 and block_data[0][2] == 0 and block_data[1][0] == 1 and block_data[1][1] ==1 and block_data[1][2] ==0 and block_data[2][0] ==0 and block_data[2][1] ==0 and block_data[2][2] ==0:
        result = result + " and board is valid"
      elif block_data[0][1] == -1 and block_data[0][0] == 1 and block_data[0][2] == 1 and block_data[1][0] == 1 and block_data[1][1] ==1 and block_data[1][2] ==1 and block_data[2][0] ==0 and block_data[2][1] ==0 and block_data[2][2] ==0:
          result = result + " and board is valid"
      elif block_data[0][2] == -1 and block_data[0][1] == 1 and block_data[0][0] == 0 and block_data[1][0] == 0 and block_data[1][1] ==1 and block_data[1][2] ==1 and block_data[2][0] ==0 and block_data[2][1] ==0 and block_data[2][2] ==0:
          result = result + " and board is valid"
      elif block_data[1][0] == -1 and block_data[0][0] == 1 and block_data[0][1] == 1 and block_data[0][2] == 0 and block_data[1][1] ==1 and block_data[1][2] ==0 and block_data[2][0] ==1 and block_data[2][1] ==1 and block_data[2][2] ==0:
          result = result + " and board is valid"
      elif block_data[1][1] == -1 and block_data[0][0] == 1 and block_data[0][1] == 1 and block_data[0][2] == 1 and block_data[1][0] ==1 and block_data[1][2] ==1 and block_data[2][0] ==1 and block_data[2][1] ==1 and block_data[2][2] ==1:
          result = result + " and board is valid"
      elif block_data[1][2] == -1 and block_data[0][0] == 0 and block_data[0][1] == 1 and block_data[0][2] == 1 and block_data[1][0] ==0 and block_data[1][1] ==1 and block_data[2][0] ==0 and block_data[2][1] ==1 and block_data[2][2] ==1:
          result = result + " and board is valid"
      elif block_data[2][0] == -1 and block_data[0][0] == 0 and block_data[0][1] == 0 and block_data[0][2] == 0 and block_data[1][0] ==1 and block_data[1][1] ==1 and block_data[1][2] ==0 and block_data[2][1] ==1 and block_data[2][2] ==0:
          result = result + " and board is valid"
      elif block_data[2][1] == -1 and block_data[0][0] == 0 and block_data[0][1] == 0 and block_data[0][2] == 0 and block_data[1][0] ==1 and block_data[1][1] ==1 and block_data[1][2] ==1 and block_data[2][0] ==1 and block_data[2][2] ==1:
          result = result + " and board is valid"
      elif block_data[2][2] == -1 and block_data[0][0] == 0 and block_data[0][1] == 0 and block_data[0][2] == 0 and block_data[1][0] ==0 and block_data[1][1] ==1 and block_data[1][2] ==1 and block_data[2][0] ==0 and block_data[2][1] ==1:
          result = result + " and board is valid"        
      else:
        result = "Invalid Board"

    return result


grid = [
  [1,-1,1],
  [1,1,1],
  [0,0,0]
]
print (validate(grid))



