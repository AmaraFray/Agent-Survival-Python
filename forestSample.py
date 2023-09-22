class ForestSample():
  '''
  size : Set forest size 
  initial_fire_pos : First tree to set on fire
  initial_monkey_pos : Place where monkey spawns

  #=========================#
  #  High Level Operations  #
  #=========================#

  renderFrame(direction)  to move monkey, spread fire, and display the render
  direction:
    0 to move up
    1 to move down
    2 to move left
    3 to move right

  #=========================#
  #  Low Level Operations   #
  #=========================#
  
  use move(direction) to move the monkey
  direction:
    0 to move up
    1 to move down
    2 to move left
    3 to move right

  use spreadFire() to render the next stages of fire spreading


  #=========================#
  #      Test Use Case      #
  #=========================#

  f = ForestSample(size=10)
  f.renderFrame(2)
  f.renderFrame(1)
  f.renderFrame(1)
  f.renderFrame(1)


  '''
  def __init__(self, size=10, initial_fire_pos = (2,3), initial_monkey_pos = (3,2)):
    self.board = [['🌲' for i in range(size)] for i in range(size)]
    self.board_size = size

    self.player_pos = list(initial_monkey_pos)

    self.fire_positions = {initial_fire_pos}
    
    self.player_token = '🐒'
    self.fire_token = '🔥'

    self.spawnPlayer()
    self.setFireToObject()
  
  # === RENDERING CODE === #

  def createBoard(self):
    self.board = [['🌲' for i in range(self.board_size)] for i in range(self.board_size)]

  def spawnPlayer(self):
    self.board[self.player_pos[0]][self.player_pos[1]] = self.player_token

  def setFireToObject(self):
    for fire_pos in self.fire_positions:
      self.board[fire_pos[0]][fire_pos[1]] = self.fire_token

  def renderBoard(self):
    self.createBoard()
    self.spawnPlayer()
    self.setFireToObject()
  
  def displayBoard(self):
    self.renderBoard()
    print('\n')
    for i in self.board:
      for j in i:
        print(j, end ='  ')
      print('\n')
  
  # ==== FIRE MATH ===== #
  
  def newPoints(self, position):
    a = max(0, position[0]-1)
    b = min(self.board_size - 1, position[0]+1)
    c = max(0, position[1]-1)
    d = min(self.board_size - 1, position[1]+1)

    return {
        (a, position[1]), 
         (b, position[1]),
          (position[0], c), 
           (position[0], d)}

  def spreadFire(self):
    curr_positions = self.fire_positions
    new_positions = set()
    new_positions.update(curr_positions)
    for i in curr_positions:  
      new_positions.update(self.newPoints(i))
    
    self.fire_positions = new_positions
    self.setFireToObject()

  # ==== MONKEY MATH ===== #

  def moveMonkey(self, direction):
    # direction : 0 up, 1 down, 2 left 3 right

    if (direction == 0):
      self.player_pos[0] = max(0, self.player_pos[0]-1)
    elif (direction == 1):
      self.player_pos[0] = min(self.board_size - 1, self.player_pos[0]+1)
    elif (direction == 2):
      self.player_pos[1] = max(self.player_pos[1]-1, 0)
    elif (direction == 3):
      self.player_pos[1] = min(self.player_pos[1]+1, self.board_size - 1)
    else:
      "INCORRECT DIRECTION"

  # ====== TICK TIME ====== #

  def renderFrame(self, direction):
    self.moveMonkey(direction)
    self.spreadFire()
    self.displayBoard()
  
  def bfs(self):
    currentBoard = self.board
    currentFirePos = self.fire_pos
    playerPos = self.player_pos

    ## ADD YOUR CODE HERE ##

    direction = 0
    return direction # a number from 0 to 3
